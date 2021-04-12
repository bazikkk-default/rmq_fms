MAIN_PAGE = 'http://services.fms.gov.ru/info-service.htm'
CAPTCHA_PAGE = 'http://services.fms.gov.ru/services/captcha.jpg'
REG_EXP_TAG = lambda tag: f"<{tag}>.*</{tag}>"
START_TAG_LEN = len('<em>')
END_TAG_LEN = len('</em>')
