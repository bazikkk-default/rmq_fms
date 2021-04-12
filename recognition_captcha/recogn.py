from base64 import b64encode
import aiohttp
import asyncio
from typing import Union, Any
from logging import getLogger

from session_maker.cheker import check_status_code
from recognition_captcha.egg_of_destiny import check_error_code_result, check_error_code_register
from recognition_captcha.constants import *


logger = getLogger(__name__)


class CaptchaRecognition:
    TOKEN = None
    IN_URL = "https://rucaptcha.com/in.php"
    RESULT_URL = "https://rucaptcha.com/res.php"

    def __init__(self, token: str = None):
        self.TOKEN = token

    async def load_data(self, captcha_img):
        payload = {'body': b64encode(captcha_img).decode("utf-8"),
                   'key': self.TOKEN,
                   'json': JSON,
                   'method': BASE_64
                   }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.IN_URL, data=payload) as resp:
                check_status_code(resp.status)
                captcha_id = await resp.json()
                logger.debug(resp.request_info)
                logger.debug(f"capcha id ={captcha_id}")
                check_error_code_register(captcha_id.get('request'))
        return captcha_id.get('request')

    async def load_result(self, captcha_id) -> Union[str, Any]:
        payload = {'key': self.TOKEN,
                   'json': JSON,
                   'method': BASE_64,
                   'id': captcha_id,
                   'action': GET
                   }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.RESULT_URL, params=payload) as resp:
                check_status_code(resp.status)
                result = await resp.json()
                logger.debug(f"result recognition ={result}")
                check_error_code_result(result.get('request', NOT_READY))
        return result.get('request') if result.get('request', NOT_READY) != NOT_READY else None

    async def run(self, captcha_img) -> str:
        result = None
        captcha_id = await self.load_data(captcha_img)
        while not result:
            await asyncio.sleep(5)
            result = await self.load_result(captcha_id)
        return result
