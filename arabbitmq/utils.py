from os import environ
from logging import getLogger
from json import JSONDecodeError, loads, dumps
from pydantic import ValidationError

from message_models import ReceivedMessage, Person, Message, Error, Result
from session_maker.session import SessionMaker
from exception import StatusCodeError, CaptchaError, ValidateSchemaError

env_exc = environ.get("RMQ_EXCHANGE", 'services')
env_queue = environ.get("RMQ_QUEUE", 'fms_agreement_in')
env_token = environ.get("RUCAPTCHA_TOKEN", 'SOME_TOKEN')
logger = getLogger(__name__)


async def callback(message):
    try:
        received_message = loads(message.body.decode("utf-8"))
        task = ReceivedMessage(
            action=received_message.get('action'),
            id=received_message.get('id'),
            rmq_from=received_message.get('from'),
            params=Person(**received_message.get('params')),
            resource=received_message.get('resource'),
            application=received_message.get('application'),
            bank_id=received_message.get('bank_id'),
            system_code=received_message.get('system_code'),
            project_id=received_message.get('project_id')
        )

    except JSONDecodeError:
        error_msg = f"Received message does not have json format: {message.body.decode('utf-8')}"
        logger.error(error_msg)
        error = Message(
            params=Error(
                status='fail',
                message=error_msg,
                description='Help or message of repair'
            )
        )
        await message.channel.basic_publish(exchange=env_exc,
                                            body=bytes(dumps(error.json()), 'utf-8'),
                                            routing_key="#.error.#")

    except ValidationError as exc_error:
        error_msg = f"Received message does not match the pattern: {message.body.decode('utf-8')}\nERROR: {exc_error}"
        logger.error(error_msg)
        error = Message(
            params=Error(
                status='fail',
                message=error_msg,
                description='Help or message of repair'
            )
        )
        await message.channel.basic_publish(exchange=env_exc,
                                            body=bytes(dumps(error.json()), 'utf-8'),
                                            routing_key="#.error.#")

    except ValidateSchemaError as exc_error:
        error_msg = f"Received message does not match the pattern: {message.body.decode('utf-8')}\nERROR: {exc_error.error}"
        logger.error(error_msg)
        error = Message(
            params=Error(
                status='fail',
                message=list(exc_error.error.values())[0][0] if bool(exc_error.error.values()) else 'Unknown error',
                description=list(exc_error.error.values())[0][1] if bool(exc_error.error.values()) else 'Unknown error'
            )
        )
        await message.channel.basic_publish(exchange=env_exc,
                                            body=bytes(dumps(error.json()), 'utf-8'),
                                            routing_key="#.error.#")
    else:
        try:
            logger.debug(received_message)
            session = SessionMaker(token=env_token)
            captcha = await session.get_captcha()
            result = await session.get_person_info(task.params, captcha)
            result = result if result else ''
            response = Message(
                action=task.params.answer.action or "response",
                id=task.params.answer.id or task.id,
                params=Result(
                    status='success',
                    check_status=True if 'не обнаружено' in result else False,
                    message='There are no restrictions'
                    if 'не обнаружено' in result else 'There are restrictions'
                ),
                resource=task.params.answer.resource or task.resource,
                bank_id=task.bank_id,
                system_code=task.system_code,
            ).dict()
            response.update({"from": env_queue})
            logger.debug(f"BYTES RESPONSE : {bytes(dumps(response), 'utf-8')}")
            logger.info(f"{task.id} {result}")
            await message.channel.basic_publish(body=bytes(dumps(response), 'utf-8'),
                                                exchange=env_exc,
                                                routing_key=task.rmq_from)

        except (StatusCodeError, CaptchaError) as error:
            logger.error(str(error.get_error()))
            error = Message(
                action=task.params.answer.action or "response",
                id=task.params.answer.id or task.id,
                params=Error(
                    status='fail',
                    message=next(iter(error.error.values()))[0] if error.error.values() else 'UNKNOWN ERROR',
                    description=next(iter(error.error.values()))[0] if error.error.values() else 'Something went wrong!'
                ),
                resource=task.params.answer.resource or task.resource,
                bank_id=task.bank_id,
                system_code=task.system_code,
            ).dict()
            error.update({"from": env_queue})
            await session.session.close()
            await message.channel.basic_publish(exchange=env_exc,
                                                body=bytes(dumps(error), 'utf-8'),
                                                routing_key=task.rmq_from)
    finally:
        await message.channel.basic_ack(message.delivery.delivery_tag)

