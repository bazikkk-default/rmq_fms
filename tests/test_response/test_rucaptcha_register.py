from asynctest import CoroutineMock, patch, TestCase

from recognition_captcha.recogn import CaptchaRecognition
from exception import CaptchaError, StatusCodeError


class TestAsyncRucaptchaRegistr(TestCase):

    @patch('aiohttp.ClientSession.post')
    async def test_success_register_captcha(self, mock_get):
        recogn = CaptchaRecognition(token='1234')
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[
            {'status': 0, 'request': '4123451'}
        ])
        mock_get.return_value.__aenter__.return_value.status = 200
        captcha_id = await recogn.load_data(bytes("picture", "utf-8"))
        self.assertEqual(captcha_id, '4123451')

    @patch('aiohttp.ClientSession.post')
    async def test_err_status_register(self, mock_get):
        recogn = CaptchaRecognition(token='1234')
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[
            {'status': 0, 'request': 'ERROR'}
        ])
        mock_get.return_value.__aenter__.return_value.status = 200
        with self.assertRaises(CaptchaError):
            captcha_id = await recogn.load_data(bytes("picture", "utf-8"))

    @patch('aiohttp.ClientSession.post')
    async def test_err_status_code(self, mock_get):
        recogn = CaptchaRecognition(token='1234')
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[
            {'status': 0, 'request': '12345'}
        ])
        mock_get.return_value.__aenter__.return_value.status = 502
        with self.assertRaises(StatusCodeError):
            captcha_id = await recogn.load_data(bytes("picture", "utf-8"))

