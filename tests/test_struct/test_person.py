from message_models import *

import unittest


class TestStructPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.standard_message = Person(
                name_lat="Ivan",
                last_name_lat="Ivanov",
                name="Иван",
                last_name="Иванов",
                second_name="Иванович",
                gender="male",
                birthday="01.01.2020",
                citizenship="АЛБАНИЯ",
                type_of_document="ЗАГРАНИЧНЫЙ ПАСПОРТ",
                number_of_document="1111111",
                period_of_validity="01.01.2020",
                issued_from="АЛБАНИЯ",
                answer=Answer(
                    resource='fms_agreement',
                    action='fms_agreement_done',
                    id=22222,
                    system_code='bpm'
                )
            )

        self.error_message = Person(
                name_lat="Ivan",
                last_name_lat="Ivanov",
                name="Иван",
                last_name="Иванов",
                second_name="Иванович",
                gender="male",
                birthday="01.01.2020",
                citizenship="АЛБАНИЯ",
                type_of_document="ЗАГРАНИЧНЫЙ ПАСПОРТ",
                number_of_document="1111111",
                period_of_validity="01.01.2020",
                issued_from="АЛБАНИЯ"
            )
        self.mistake_keys = Person(
                name="Иван",
                last_name="Иванов",
                gender="male",
                birthday="01.01.2020",
                citizenship="АЛБАНИЯ",
                type_of_document="ЗАГРАНИЧНЫЙ ПАСПОРТ",
                number_of_document="1111111",
                issued_from="АЛБАНИЯ"
            )

    def test_init_struct_Message(self):
        reference = Person(**{
                "name_lat": "Ivan",
                "last_name_lat": "Ivanov",
                "name": "Иван",
                "last_name": "Иванов",
                "second_name": "Иванович",
                "gender": "male",
                "birthday": "01.01.2020",
                "citizenship": "АЛБАНИЯ",
                "type_of_document": "ЗАГРАНИЧНЫЙ ПАСПОРТ",
                "number_of_document": "1111111",
                "period_of_validity": "01.01.2020",
                "issued_from": "АЛБАНИЯ",
                'answer': {
                    'resource': 'fms_agreement',
                    'action': 'fms_agreement_done',
                    'id': 22222,
                    'system_code': 'bpm'
                }
            }
                            )
        self.assertEqual(str(reference.dict()), str(self.standard_message.dict()))

    def test_init_struct_ErrorMessage(self):
        reference = Person(**{
                "name_lat": "Ivan",
                "last_name_lat": "Ivanov",
                "name": "Иван",
                "last_name": "Иванов",
                "second_name": "Иванович",
                "gender": "male",
                "birthday": "01.01.2020",
                "citizenship": "АЛБАНИЯ",
                "type_of_document": "ЗАГРАНИЧНЫЙ ПАСПОРТ",
                "number_of_document": "1111111",
                "period_of_validity": "01.01.2020",
                "issued_from": "АЛБАНИЯ",
                'answer': {
                    'resource': 'fms_agreement',
                    'action': 'response',
                    'id': None,
                    'system_code': 'bpm'
                }
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.error_message.dict()))

    def test_mistake_key(self):
        reference = Person(**{
                "name_lat": None,
                "last_name_lat": None,
                "name": "Иван",
                "last_name": "Иванов",
                "second_name": None,
                "gender": "male",
                "birthday": "01.01.2020",
                "citizenship": "АЛБАНИЯ",
                "type_of_document": "ЗАГРАНИЧНЫЙ ПАСПОРТ",
                "number_of_document": "1111111",
                "period_of_validity": None,
                "issued_from": "АЛБАНИЯ",
                'answer': {
                    'resource': 'fms_agreement',
                    'action': 'response',
                    'id': None,
                    'system_code': 'bpm'
                }
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.mistake_keys.dict()))

