from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestGainExp(TestCase):
    def test_gain_exp_correct_exp_amount_at_level_one(self):
        character = {'level': 1, 'exp': 0}
        game.gain_exp(character)
        expected = 2
        actual = character['exp']
        self.assertEqual(actual, expected)

    def test_gain_exp_correct_exp_amount_at_level_two(self):
        character = {'level': 2, 'exp': 0}
        game.gain_exp(character)
        expected = 4
        actual = character['exp']
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_gain_exp_correct_print_statement(self, mock_output):
        character = {'level': 2, 'exp': 0}
        game.gain_exp(character)
        expected = 'You gained 4 fame.\n'
        self.assertEqual(mock_output.getvalue(), expected)


