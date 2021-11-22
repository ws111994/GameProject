from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestCharacterCurrentStatus(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_current_status_correct_print_output(self, mock_output):
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 5, 'Current HP': 5, 'name': 'Bob', 'level': 1,
                         'exp': 0, 'class': 'Rich Boi', 'skill': 'Shopping Spree', 'damage': 4, 'item': None}
        game.character_current_status(new_character)
        expected = "Bob's current status [Resistance: 5/5] [Level: 1] [Exp: 0] [Charm: 4] [Item: None] " \
                   "[Social Position: Rich Boi]\n"
        self.assertEqual(expected, mock_output.getvalue())

    def test_character_current_status_parameter_unchanged(self):
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 5, 'Current HP': 5, 'name': 'Bob', 'level': 1,
                         'exp': 0, 'class': 'Rich Boi', 'skill': 'Shopping Spree', 'damage': 4, 'item': None}
        game.character_current_status(new_character)
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Max HP': 5, 'Current HP': 5, 'name': 'Bob',
                              'level': 1,'exp': 0, 'class': 'Rich Boi', 'skill': 'Shopping Spree', 'damage': 4,
                              'item': None}
        self.assertEqual(expected_character, new_character)