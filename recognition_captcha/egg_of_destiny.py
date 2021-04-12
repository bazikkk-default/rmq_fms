from exception import CaptchaError
from typing import Dict, Union, List

from .constants import NOT_READY


ErrorType = Dict[str, Union[str, List[str]]]


def check_error_code_register(error_code: str = 'ERROR'):
    try:
        assert 'ERROR' not in error_code
    except AssertionError as error:
        raise CaptchaError(wrong_went(error_code))


def wrong_went(error_code: str = 'ERROR') -> ErrorType:
    codes = {
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
    return {error_code: codes.get(error_code, 'Unknown error')}


def check_error_code_result(error_code: str = NOT_READY):
    try:
        assert (NOT_READY == error_code) or ("ERROR" not in error_code)
    except AssertionError as error:
        raise CaptchaError(wrong_went_result(error_code))


def wrong_went_result(error_code: str = NOT_READY) -> ErrorType:
    codes = {
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
    return {error_code: codes.get(error_code, 'Unknown error')}



