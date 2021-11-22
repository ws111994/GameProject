from unittest import TestCase
from unittest.mock import patch

import game


class TestGenerateGirl(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_girl_correct_dictionary_values(self, _):
        character = {'level': 1}
        girl = game.generate_girl(character)
        expected = {'name': 'Gold digging girl', 'Current HP': 10, 'Max HP': 10, 'damage': 1,
                    'type': ['Rich Boi', 'Lottery Winner', 'Elon Musk'], 'boss': False}
        self.assertEqual(girl, expected)

    def test_generate_girl_parameter_unchanged(self):
        character = {'level': 1}
        game.generate_girl(character)
        expected_character = {'level': 1}
        self.assertEqual(character, expected_character)

