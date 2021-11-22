from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestChooseName(TestCase):
    @patch('builtins.input', return_value='1')
    def test_choose_name_short_name(self, _):
        expected = '1'
        actual = game.choose_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='Thisisaverylongnamethataplayercouldchoose')
    def test_choose_name_long_name(self, _):
        expected = 'Thisisaverylongnamethataplayercouldchoose'
        actual = game.choose_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['', 'Bob'])
    def test_choose_name_empty_name(self, _):
        expected = 'Bob'
        actual = game.choose_name()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='    Bob    ')
    def test_choose_name_name_with_whitespace(self, _):
        expected = 'Bob'
        actual = game.choose_name()
        self.assertEqual(expected, actual)
