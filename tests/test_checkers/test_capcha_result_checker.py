from recognition_captcha.egg_of_destiny import wrong_went_result

import unittest


class TestResult(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.codes = {
        'ERROR_CAPTCHA_UNSOLVABLE': [

            'We cannot solve your captcha - three of our employees could not solve it, or we did not receive an answer '
            'in for 90 seconds. We will not charge you for this request. ',
            'You can try sending the captcha again.'
        ],
        'ERROR_WRONG_USER_KEY': [
            'You have specified a value for the key parameter in the wrong format, the key must be 32 characters long.',
            'Stop sending requests and check your API key.'
        ],
        'ERROR_KEY_DOES_NOT_EXIST': [
            'The key you specified does not exist.',
            'Stop sending requests and check your API key.'
        ],
        'ERROR_WRONG_ID_FORMAT': [
            'You sent the captcha ID in the wrong format. ID consists of numbers only. ',
            'Check the ID of your captcha or the code that is responsible for receiving and sending the ID.'
        ],
        'ERROR_WRONG_CAPTCHA_ID': [
            'You have sent an invalid CAPTCHA ID.',
            'Check the ID of your captcha or the code that is responsible for receiving and sending the ID.'
        ],
        'ERROR_BAD_DUPLICATES': [
            'Ошибка возвращается, если вы используете функцию 100% распознавания. Ошибка означает, что мы достигли '
            'максимального числа попыток, но требуемое количество совпадений достигнуто не было.',
            'Вы можете попробовать отправить вашу капчу ещё раз.'
        ],
        'REPORT_NOT_RECORDED': [
            'An error is returned when submitting a complaint about an incorrect answer if you have already complained '
            'about a large number correctly solved captchas (over 40%). Or if more than 15 minutes have passed since '
            'the captcha was sent to the solution. ',
            'Make sure that you only submit complaints if you do not resolve correctly.'
        ],
        'ERROR_DUPLICATE_REPORT': [
            'An error is returned when sending reports if you re-send a report for the same captcha.',
            'Make sure you only submit the report for each captcha once.'
        ],
        'ERROR': [
            'You have exceeded the request limit and your account has been temporarily suspended.',
            'You need to set the correct timeouts. More information in the chapter Request Limits. '
        ],
        'ERROR_IP_ADDRES': [
            'An error is returned when adding domain or IP for pingback (callback). This happens if you '
            'send a request to add an IP or domain from an IP address that does not match your IP or domain'
            'for pingback.',
            'Send a request from the same IP address to which you want to receive pingback.'
        ],
        'ERROR_TOKEN_EXPIRED': [
            'You can get this error if you solve GeeTest captcha. This error code means expired challenge value '
            'actions from your request.',
            'Try sending your request again. If you always get this error, then we cannot solve GeeTest captcha on '
            'this site.'
        ],
        'ERROR_EMPTY_ACTION': [
            'The action parameter was not passed or was passed without a value.',
            'Add the required parameter and value to the request, such as get or getbalance.'
        ],
        'ERROR_PROXY_CONNECTION_FAILED': [
            'You may get this error if we were unable to download the captcha through your proxy server. This proxy '
            'will be marked BAD and we will not accept requests with it for 10 minutes. And in.php will return '
            'ERROR_BAD_PROXY error when using this proxy.',
            'Use a different proxy server in your requests.'
        ]

    }

    def test_run_all(self):
        result = {}
        for test in self.codes.keys():
            result.update(wrong_went_result(test))
        self.assertEqual(result, self.codes)

