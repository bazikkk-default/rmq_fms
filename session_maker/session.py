from re import search
from aiohttp import ClientSession
from logging import getLogger

from message_models import Person
from recognition_captcha.recogn import CaptchaRecognition
from mapper import mapper_to_request
from session_maker.constants import MAIN_PAGE, CAPTCHA_PAGE, REG_EXP_TAG, START_TAG_LEN, END_TAG_LEN
from session_maker.cheker import check_status_code


logger = getLogger(__name__)


class SessionMaker:
    def __init__(self, token=None):
        self.TOKEN = token
        self.session = ClientSession()

    async def get_captcha(self) -> str:
        await self.session.get(MAIN_PAGE)
        captcha_jpg = await self.session.get(CAPTCHA_PAGE)
        check_status_code(captcha_jpg.status)
        recognition = CaptchaRecognition(self.TOKEN)
        return await recognition.run(await captcha_jpg.content.read())

    async def get_person_info(self, person_data: Person, captcha: str):
        logger.debug(f"PAYLOAD FMS: {mapper_to_request(person_data, captcha)}")
        async with self.session.post(MAIN_PAGE, params=mapper_to_request(person_data, captcha)) as resp:
            check_status_code(resp.status)
            response = await resp.text()
            status = search(REG_EXP_TAG('em'), response)
            status = status.group() if status else None
            logger.debug(f"FMS STATUS: {status}")
        await self.session.close()
        return status[START_TAG_LEN:len(status)-END_TAG_LEN] if status else None
