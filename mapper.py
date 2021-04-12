from constants import DOC_TYPE, PLACE, DOC_FROM
from message_models import Person


def mapper_to_request(person_data: Person, captcha: str) -> dict:
    doc_issuer = PLACE.get(person_data.issued_from.upper() if person_data.issued_from else '')
    doc_issuer = doc_issuer or DOC_FROM.get(person_data.issued_from.upper() if person_data.issued_from else '')
    return {
        "sid": 3000,
        "form_name": "form",
        "CITIZEN_LASTNAME_LAT": person_data.last_name_lat or '',
        "CITIZEN_FIRSTNAME_LAT": person_data.name_lat or '',
        "CITIZEN_LASTNAME": person_data.last_name,
        "CITIZEN_FIRSTNAME": person_data.name,
        "CITIZEN_GIVENNAME": person_data.second_name or '',
        "CITIZEN_SEX": person_data.gender[0].upper(),
        "CITIZEN_BIRTHDATE": person_data.birthday,
        "CITIZENSHIP": PLACE.get(person_data.citizenship.upper(), ),
        "DOC_TYPE": DOC_TYPE.get(person_data.type_of_document.upper()),
        "DOC_NUMBER": person_data.number_of_document,
        "DOC_VALIDITYDATE": person_data.period_of_validity or '',
        "DOC_ISSUER": doc_issuer,
        "captcha-input": captcha
    }