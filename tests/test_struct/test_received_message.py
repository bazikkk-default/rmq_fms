from message_models import *

import unittest


class TestStructReceivedMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.standard_message = ReceivedMessage(
            id=11111,
            rmq_from="test_application",
            resource="fms_agreement",
            action="fms",
            params=Person(
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
                    resource="fms_agreement",
                    action="fms_agreement_done",
                    id=22222,
                    system_code="bpm"
                )
            ),
            application="bpm",
            bank_id="other",
            system_code="bpm",
            project_id="bpm"
        )

        self.error_message = ReceivedMessage(
            id=11111,
            rmq_from="test_application",
            resource="fms_agreement",
            action="fms",
            application="bpm",
            params=Person(
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
                    resource="fms_agreement",
                    action="fms_agreement_done",
                    id=22222,
                    system_code="bpm"
                )
            ),
            bank_id="other",
            system_code="bpm",
            project_id="bpm"
        )
        self.mistake_keys = ReceivedMessage(
            id=11111,
            rmq_from="test_application",
            resource="fms_agreement",
            action="fms",
            params=Person(
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
            ),

            application="bpm",
            bank_id="other",
            system_code="bpm",
            project_id="bpm"
        )

    def test_init_struct_ReceivedMessage(self):
        reference = ReceivedMessage(**{
            "id": 11111,
            "rmq_from": "test_application",
            "resource": "fms_agreement",
            "action": "fms",
            "params": {
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
                "answer": {
                    "resource": "fms_agreement",
                    "action": "fms_agreement_done",
                    "id": 22222,
                    "system_code": "bpm"
                }
            },
            "application": "bpm",
            "bank_id": "other",
            "system_code": "bpm",
            "project_id": "bpm"
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.standard_message.dict()))

    def test_init_struct_ErrorReceivedMessage(self):
        reference = ReceivedMessage(**{
            "id": 11111,
            "rmq_from": "test_application",
            "resource": "fms_agreement",
            "action": "fms",
            "params": {
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
                "answer": {
                    "resource": "fms_agreement",
                    "action": "fms_agreement_done",
                    "id": 22222,
                    "system_code": "bpm"
                }
            },
            "application": "bpm",
            "bank_id": "other",
            "system_code": "bpm",
            "project_id": "bpm"
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.error_message.dict()))

    def test_mistake_key(self):
        reference = ReceivedMessage(**{
            "id": 11111,
            "rmq_from": "test_application",
            "resource": "fms_agreement",
            "action": "fms",
            "params": {
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
                "answer": None
            },
            "application": "bpm",
            "bank_id": "other",
            "system_code": "bpm",
            "project_id": "bpm"
        }
                            )
        self.assertNotEqual(str(reference.dict()), str(self.mistake_keys.dict()))

