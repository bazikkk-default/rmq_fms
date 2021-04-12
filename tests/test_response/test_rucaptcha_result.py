from asynctest import CoroutineMock, patch, TestCase

from recognition_captcha.recogn import CaptchaRecognition
from exception import CaptchaError, StatusCodeError


class TestAsyncRucaptchaResult(TestCase):

    @patch('aiohttp.ClientSession.get')
    async def test_success_register_captcha(self, mock_get):
        recogn = CaptchaRecognition(token='1234')
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[
            {'status': 0, 'request': '112233'}
        ])
        mock_get.return_value.__aenter__.return_value.status = 200
        captcha = await recogn.load_result('1234')
        self.assertEqual(captcha, '112233')

    @patch('aiohttp.ClientSession.get')
    async def test_err_status_register(self, mock_get):
        recogn = CaptchaRecognition(token='112233')
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[
            {'status': 0, 'request': 'ERROR'}
        ])
        mock_get.return_value.__aenter__.return_value.status = 200
        with self.assertRaises(CaptchaError):
            captcha = await recogn.load_result('1234')

    @patch('aiohttp.ClientSession.get')
    async def test_err_status_code(self, mock_get):
        recogn = CaptchaRecognition(token='1234')
        mock_get.return_value.__aenter__.return_value.json = CoroutineMock(side_effect=[
            {'status': 0, 'request': '112233'}
        ])
        mock_get.return_value.__aenter__.return_value.status = 502
        with self.assertRaises(StatusCodeError):
            captcha = await recogn.load_result('1234')

