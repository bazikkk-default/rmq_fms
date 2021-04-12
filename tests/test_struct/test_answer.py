from message_models import *

import unittest


class TestStructAnswer(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.standard_message = Answer(
            id=11111,
            action="fms",
            resource='bpm',
            system_code='bpm',
        )

        self.error_message = Answer(
            id=11111,
            action="fms",
            system_code='bpm',
        )
        self.mistake_keys = Answer()

    def test_init_struct_Message(self):
        reference = Answer(**{
            "id": 11111,
            "action": "fms",
            'resource': 'bpm',
            'system_code': 'bpm',
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.standard_message.dict()))

    def test_init_struct_ErrorMessage(self):
        reference = Answer(**{
            "id": 11111,
            "action": "fms",
            'resource': None,
            'system_code': 'bpm',
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.error_message.dict()))

    def test_mistake_key(self):
        reference = Answer(**{
            "id": None,
            "action": None,
            'resource': None,
            'system_code': None,
        }
                            )
        self.assertEqual(str(reference.dict()), str(self.mistake_keys.dict()))

