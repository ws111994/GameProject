from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestFlee(TestCase):
    @patch('random.randint', return_value=1)
    def test_flee_character_hp_drop_case(self, _):
        character = {'Current HP': 5}
        girl = {'name': 'Alice', 'damage': 2}
        game.flee(character, girl)
        expected = 3
        actual = character['Current HP']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_flee_character_hp_unchanged_case(self, _):
        character = {'Current HP': 5}
        girl = {'name': 'Alice', 'damage': 2}
        game.flee(character, girl)
        expected = 5
        actual = character['Current HP']
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_flee_correct_print_output(self, mock_output, _):
        character = {'Current HP': 5}
        girl = {'name': 'Alice', 'damage': 2}
        game.flee(character, girl)
        expected = 'You told Alice that you are married, so Alice let you go free.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_flee_girl_is_unchanged(self):
        character = {'Current HP': 5}
        girl = {'name': 'Alice', 'damage': 2}
        game.flee(character, girl)
        expected = {'name': 'Alice', 'damage': 2}
        self.assertEqual(expected, girl)