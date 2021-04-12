from pydantic import BaseModel, validator
from typing import Optional, Union, Any
from re import findall
from datetime import datetime

from constants import *
from exception import ValidateSchemaError


class Error(BaseModel):
    status: str = 'fail'
    message: str = 'Something went wrong'
    description: str = 'Help or message of repair'


class Result(BaseModel):
    status: str = 'success'
    message: str = 'There are no restrictions'
    check_status: bool = False


class Answer(BaseModel):
    resource: Optional[str]
    action: Optional[str]
    id: Optional[int]
    system_code: Optional[str]


class Person(BaseModel):
    name_lat: Optional[str]  # Имя латиница
    last_name_lat: Optional[str]  # Фамилия латиница
    name: str  # Имя
    last_name: str  # Фамилия
    second_name: Optional[str]  # Отчество
    gender: str
    birthday: str
    citizenship: str
    type_of_document: str
    number_of_document: str
    period_of_validity: Optional[str]
    issued_from: str

    answer: Optional[Union[Answer, Any]] = Answer(
        resource='fms_agreement',
        action='response',
        system_code='bpm',
    )

    @classmethod
    def raise_date_error(cls, field_name):
        raise ValidateSchemaError(
            error={
                "error": [
                    f"Must be exist field {field_name}",
                    f"Does not have any date in format dd.mm.YYYY"
                ]
            }
        )

    @classmethod
    def __real_date(cls, value, field_name):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            cls.raise_date_error(field_name)
        else:
            return value

    @classmethod
    def __check_value(cls, value, field_name):
        if value:
            result = findall("\d{2}.\d{2}.\d{4}", value)
            if not result or len(result) != 1:
                cls.raise_date_error(field_name)
            return cls.__real_date(next(iter(result)), field_name)
        else:
            return value

    @validator(
        'birthday', 'period_of_validity',
        always=True, allow_reuse=True)
    def check_date(cls, value, values, **kwargs):
        if value or kwargs['field'].name == 'period_of_validity':
            return cls.__check_value(value, kwargs['field'].name)
        else:
            cls.raise_date_error(kwargs['field'].name)

    @validator('type_of_document', always=True)
    def in_allowed_docs(cls, value: str):
        if value and (value.upper() in DOC_TYPE.keys()):
            return value
        else:
            raise ValidateSchemaError(
                error={
                    "error": [
                        "Unknown doc type field",
                        f"Must be one of {[y.capitalize() for y in DOC_TYPE.keys()]}"
                    ]
                }
            )

    @validator('citizenship', always=True)
    def in_allowed_citizenship(cls, value: str):
        if value and (value.upper() in PLACE.keys()):
            return value
        else:
            raise ValidateSchemaError(
                error={
                    "error": [
                        "Unknown place field",
                        f"Must be one of {[y.capitalize() for y in PLACE.keys()]}"
                    ]
                }
            )

    @validator('issued_from', always=True)
    def in_allowed_issued_from(cls, value: Union[str, Any]):
        if value and (value.upper() in list(PLACE.keys())) or (value.upper() in list(DOC_FROM.keys())):
            return value

        else:
            raise ValidateSchemaError(
                error={
                    "error": [
                        "Unknown issued from field",
                        f"Must be one of {list(PLACE.keys()) + list(DOC_FROM.keys())}"
                    ]
                }
            )

    @validator('gender', always=True)
    def in_allowed_gender(cls, value: Union[str, Any]):
        if (not value) or (value.lower() not in ["male", "female"]):
            raise ValidateSchemaError(
                error={
                    "error": [
                        "Unknown gender field",
                        "Must be one of {male or female}"
                    ]
                }
            )
        else:
            return value

    @validator('number_of_document', always=True)
    def in_allowed_number_of_document(cls, value: Union[str, Any]):
        if not value:
            raise ValidateSchemaError(
                error={
                    "error": [
                        "Unknown number_of_document field",
                        "Must be number of document"
                    ]
                }
            )
        else:
            return value


class ReceivedMessage(BaseModel):
    action: str
    id: int
    rmq_from: str
    params: Union[Person]
    resource: str
    application: str
    bank_id: str
    system_code: str
    project_id: str


class Message(BaseModel):
    action: str = 'response'
    id: Optional[int] = 0
    params: Union[Result, Error] = Error()
    resource: str = 'fms_agreement'
    application: str = 'fms_agreement'
    bank_id: Optional[str] = 'not_recognized'
    system_code: Optional[str] = 'not_recognized'
    project_id: str = 'service'

