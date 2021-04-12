from message_models import *

import unittest


class TestStructMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.standard_message = Message(
            id=11111,
            rmq_from="test_application",
            action="fms",
            application='bpm',
            params=Result(),
            bank_id='other',
            system_code='bpm',
        )

        self.error_message = Message(
            id=11111,
            rmq_from="test_application",
            action="fms",
            application='bpm',
            params=Error(),
            bank_id='other',
            system_code='bpm',
        )
        self.mistake_keys = Message(
            id=11111,
            rmq_from="test_application",
            action="fms",
            application='bpm',
            bank_id='other',
            system_code='bpm',
        )

    def test_init_struct_Message(self):
        reference = Message(**{
            "id": 11111,
            "rmq_from": "test_application",
            "action": "fms",
            'params': {'status': 'success', 'message': 'There are no restrictions',
                       'description': 'Help or message of repair'},
            'application': 'bpm',
            'bank_id': 'other',
            'system_code': 'bpm',
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.standard_message.dict()))

    def test_init_struct_ErrorMessage(self):
        reference = Message(**{
            "id": 11111,
            "rmq_from": "test_application",
            "action": "fms",
            'params': {'status': 'fail', 'message': 'Something went wrong', 'description': 'Help or message of repair'},
            'application': 'bpm',
            'bank_id': 'other',
            'system_code': 'bpm',
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.error_message.dict()))

    def test_mistake_key(self):
        reference = Message(**{
            "id": 11111,
            "rmq_from": "test_application",
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
                "type_of_document": "Паспорт",
                "number_of_document": "1111111",
                "period_of_validity": "01.01.2020",
                "issued_from": "АЛБАНИЯ",
                'answer': None
            },
            'application': 'bpm',
            'bank_id': 'other',
            'system_code': 'bpm',
        }
                            )
        self.assertNotEqual(str(reference.dict()), str(self.mistake_keys.dict()))

