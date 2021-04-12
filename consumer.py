from arabbitmq.utils import callback
import logging
import aiormq
from os import environ
import asyncio
from sys import exit

env_exc = environ.get("RMQ_EXCANGE", 'services')
env_queue = environ.get("RMQ_QUEUE", 'fms_agreement_in')
rmq_url = environ.get("RMQ_URL", "amqp://guest:guest@localhost/")
env_log_file = environ.get("LOG_PATH", 'fms_agreement.log')


def logs(log_format: str = '%(levelname) -10s %(asctime)s %(name) -10s %(funcName) -20s %(lineno) -3d: %(message)s',
         file_name: str = "debug.log"):
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler(file_name),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('FMS_AGREEMENT')


async def run_server():
    logger = logs(file_name=env_log_file)
    try:  
        connection = await aiormq.connect(rmq_url)
        channel = await connection.channel()
    except (aiormq.AMQPConnectionError, aiormq.AMQPChannelError) as error:
        logger.error(f"Closed connection by url: {rmq_url} with error: {error}")
        exit(1)
    else:
        declare_ok = await channel.queue_declare(env_queue, durable=True)

        logger.info(f"Start consume on queue: {env_queue}...")
        await channel.basic_consume(consumer_callback=callback, queue=declare_ok.queue, no_ack=False)


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(run_server())
event_loop.run_forever()
