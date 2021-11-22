from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestLevelUp(TestCase):
    def test_level_up_correct_dictionary_values_change(self):
        new_character = {'level': 1, 'exp': 20, 'Max HP': 10, 'Current HP': 8, 'damage': 5}
        game.level_up(new_character)
        expected = {'level': 2, 'exp': 0, 'Max HP': 25, 'Current HP': 23, 'damage': 6}
        self.assertEqual(expected, new_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_correct_print_statement(self, mock_output):
        new_character = {'level': 1, 'exp': 20, 'Max HP': 10, 'Current HP': 8, 'damage': 5}
        game.level_up(new_character)
        expected = 'You feel more confident in yourself! More charming! More Love!\n'
        self.assertEqual(expected, mock_output.getvalue())
