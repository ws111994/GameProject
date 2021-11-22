from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestCheckLevelUp(TestCase):
    def test_check_level_up_sufficient_exp_to_level_up(self):
        new_character = {'level': 1, 'exp': 30}
        actual = game.check_level_up(new_character)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_level_up_non_sufficient_exp_to_level_up(self):
        new_character = {'level': 1, 'exp': 0}
        actual = game.check_level_up(new_character)
        expected = False
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_level_up_correct_print_statement_when_exp_is_not_sufficient_to_level_up(self, mock_output):
        new_character = {'level': 1, 'exp': 0}
        game.check_level_up(new_character)
        expected = 'You are 15 fame away from becoming a better person\n'
        self.assertEqual(mock_output.getvalue(), expected)

    def test_check_level_up_parameter_unchanged(self):
        new_character = {'level': 1, 'exp': 0}
        game.check_level_up(new_character)
        expected = {'level': 1, 'exp': 0}
        self.assertEqual(new_character, expected)

