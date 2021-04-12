
class TemplateException(Exception):
    def __init__(self, error, message=None):
        self.message = message or str(error)
        self.error = error

    def get_error(self):
        return self.error


class StatusCodeError(TemplateException):
    pass


class CaptchaError(TemplateException):
    pass


class ValidateSchemaError(TemplateException):
    pass
