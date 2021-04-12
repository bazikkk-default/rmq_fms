from recognition_captcha.egg_of_destiny import wrong_went

import unittest


class TestRegistration(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.codes = {
            'ERROR_WRONG_USER_KEY': [
                'You have specified a value for the key parameter in the wrong format, the key must be 32 characters long.',
                'Stop sending requests and check your API key.'
            ],
            'ERROR_KEY_DOES_NOT_EXIST': [
                'The key you specified does not exist.',
                'Stop sending requests and check your API key.'
            ],
            'ERROR_ZERO_BALANCE': [
                'There are insufficient funds in your account.',
                'Stop sending requests. Refill your account balance to continue working with the service. '
            ],
            'ERROR_PAGEURL': [
                'The pageurl parameter was not specified in the request.',
                'Stop sending requests and change your code to pass the correct value for the pageurl parameter.'
            ],
            'ERROR_NO_SLOT_AVAILABLE': [
                'You can get this error in two cases: 1.The queue of your captchas that are not yet allocated to'
                'workers are too long. The length of the queue depends on the total number of captchas that are waiting for'
                ' distribution, and can have values ​​from 50 to 100 captchas. 2.The maximum rate that you specified in the'
                ' settings of your account below the current rate on the server. You can raise your maximum bid. ',
                'If you receive this error, do not resubmit your request immediately after receiving it.'
                'Pause for 2-3 seconds and try to repeat your request.'
            ],
            'ERROR_ZERO_CAPTCHA_FILESIZE': [
                'Your image size is less than 100 bytes.',
                'Check the image file.'
            ],
            'ERROR_TOO_BIG_CAPTCHA_FILESIZE': [
                'Your image is over 100KB in size.',
                'Check the image file.'
            ],
            'ERROR_WRONG_FILE_EXTENSION': [
                'The file has an unsupported extension. Allowed extensions: jpg, jpeg, gif, png. ',
                'Check the image file.'
            ],
            'ERROR_IMAGE_TYPE_NOT_SUPPORTED': [
                'The server cannot recognize your file type.',
                'Check the image file.'
            ],
            'ERROR_UPLOAD': [
                'The server cannot read the file from your POST request. This happens if the POST request is invalid '
                'formed in the file sending part, or contains invalid base64.',
                'You need to fix a bug in the file uploading code.'
            ],
            'ERROR_IP_NOT_ALLOWED': [
                'The request was sent from an IP address that is not added to the list of allowed IP addresses.',
                'Check the list of allowed IP addresses.'
            ],
            'IP_BANNED': [
                'Your IP address has been blocked for too many authorization attempts with an invalid authorization key.',
                'The ban will be automatically lifted after 5 minutes.'
            ],
            'ERROR_BAD_TOKEN_OR_PAGEURL': [
                'You can get this error if you send us ReCaptcha V2. An error is returned if you sent an invalid pair of '
                'googlekey and pageurl values. This usually happens if ReCaptcha is loaded into an iframe with another '
                'domain or subdomain.',
                'Look closely at the page code and find the correct googlekey and pageurl values.'
            ],
            'ERROR_GOOGLEKEY': [
                'You can get this error if you send us ReCaptcha V2. An error is returned if sitekey is in '
                'your request is empty or has an invalid format.',
                'Check your code for looking up the sitekey and submitting the request to our API.'
            ],
            'ERROR_CAPTCHAIMAGE_BLOCKED': [

                'You have submitted an image that has been flagged as unrecognizable in our database. Usually this happens '
                'if the site on which you are solving the captcha stops giving you the captcha and gives you instead'
                'image with information about the lock.',
                'Try to bypass the restrictions of this site.'
            ],
            'TOO_MANY_BAD_IMAGES': [
                'You are submitting too many images that cannot be recognized',
                'Make sure your latest captchas are visible and readable, and check for unrecognizable captchas that'
                'we have saved for you. Fix your software to send images correctly. '
            ],
            'MAX_USER_TURN': [
                'You make more than 60 calls to in.php in 3 seconds. Your API key is locked for 10 seconds. '
                'The block will be released automatically.',
                'Increase the timeout between requests to in.php to 100ms.'
            ],
            'ERROR: NNNN': [
                'You have exceeded the request limit and your account has been temporarily suspended.',
                'You need to set the correct timeouts. More information in the chapter Request Limits. '
            ],
            'ERROR_BAD_PARAMETERS': [
                'An error code is returned if you send ReCaptcha as images without instructions for employees.',
                'Send the instruction in parameter textinstructions or imginstructions.'
            ],
            'ERROR_BAD_PROXY': [
                'You can get this error if your proxy server was marked BAD. we failed to see him connect.',
                'Use a different proxy server in your requests.'
            ]
        }

    def test_run_all(self):
        result = {}
        for test in self.codes.keys():
            result.update(wrong_went(test))
        self.assertEqual(result, self.codes)

