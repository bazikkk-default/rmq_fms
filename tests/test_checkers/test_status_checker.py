from session_maker.cheker import went_wrong

import unittest


class TestResult(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.codes = {
            400: [
                'Bad Request',
                'Bad request. This response means that the server does not understand the request due to invalid syntax.'
            ],
            401: [
                'Unauthorized',
                '"Unauthorized." Authentication is required to receive the requested response. The status is similar to the'
                ' 403 status, but in this case, authentication is possible. '
            ],
            402: [
                'Payment Required',
                '"Payment required". This response code is reserved for future use. The original target for '
                'creating this when it was in use for digital payment systems (currently not'
                'used).'
            ],
            403: [
                'Forbidden',
                '"Forbidden". The client does not have permission to access the content, so the server refuses to respond '
                'appropriately. '
            ],
            404: [
                'Not Found',
                '"Not found". The server cannot find the requested resource. The code for this answer is probably the most '
                'famous because of the frequency of its occurrence on the web. '
            ],
            405: [
                'Method Not Allowed',
                '"Method not allowed." The server knows about the requested method, but it has been deactivated and cannot'
                ' be used. The two required methods, GET and HEAD, should never be deactivated and should not return this '
                'error code.'
            ],
            406: [
                'Not Acceptable',
                'Этот ответ отсылается, когда веб сервер после выполнения server-driven content negotiation, не нашел '
                'контента, отвечающего критериям, полученным из user agent.'
            ],
            407: [
                'Proxy Authentication Required',
                'This response code is the same as 401, only authentication is required for the proxy server.'
            ],
            408: [
                'Request Timeout',
                'A response with this code can come even without a previous request. It means that the server would like '
                'to disable this unused connection. This method has been used more and more often since some '
                'browsers like Chrome and IE9 have started using HTTP pre-connection mechanisms to speed up'
                'surfing (see bug 634278, future implementation of this mechanism in Firefox). Also consider that '
                'some servers drop connections without sending such messages.'
            ],
            409: [
                'Conflict',
                'This response is sent when the request conflicts with the current state of the server.'
            ],
            410: [
                'Gone',
                "This response is sent when the requested content has been removed from the server."
            ],
            411: [
                'Length Required',
                'The request was denied because the server requires a Content-Length header, but it is not provided.'
            ],
            412: [
                'Precondition Failed',
                'The client has specified conditions in its headers that the server cannot fulfill'
            ],
            413: [
                'Request Entity Too Large',
                'The request size exceeds the limit announced by the server. The server can close the connection by '
                'returning a "Retry - After" header'
            ],
            414: [
                'Request-URI Too Long',
                'The URI requested by the client is too long for the server to process'
            ],
            415: [
                'Unsupported Media Type',
                'The media format of the requested data is not supported by the server, therefore the request is rejected'
            ],
            416: [
                'Requested Range Not Satisfiable',
                'The range specified by the Range request header cannot be executed; maybe he goes beyond passed URI'
            ],
            417: [
                'Expectation Failed',
                'This response code means that the expectation received from the Expect request header cannot be met '
                'server.'
            ],
            500: [
                'Internal Server Error',
                '"Internal server error". The server has encountered a situation that it does not know how to handle. '
            ],
            501: [
                'Not Implemented',
                '"Not performed". The request method is not supported by the server and cannot be processed. The only '
                'methods, which servers should support (and therefore should not return this code) are GET and HEAD.'
            ],
            502: [
                'Bad Gateway',
                '"Bad gateway". This error means that the server, while acting as a gateway to receive a response, '
                'required to process the request received an invalid (invalid) response.'
            ],
            503: [
                'Service Unavailable',

                '"Service is unavailable". The server is not ready to process the request. Server downtime is often the '
                'cause or that it is overloaded. Note that along with this answer, the convenient for '
                'The "user-friendly" page should post an explanation of the problem.This answer should '
                'be used for temporary conditions and Retry-After: the HTTP header should, if possible, contain'
                'estimated time before service recovery. The webmaster should also take care of the headers, '
                'cache-related, which are sent along with this response, since these responses are temporary-related'
                'conditions should not normally be cached.'
            ],
            504: [
                'Gateway Timeout',
                'This error response is provided when the server is acting as a gateway and cannot receive a response in '
                'time.'
            ],
            505: [
                'HTTP Version Not Supported',
                '"HTTP version not supported." The HTTP version used in the request is not supported by the server. '
            ]
        }

    def test_run_all(self):
        result = {}
        for test in self.codes.keys():
            result.update(went_wrong(test))
        self.assertEqual(result, self.codes)
