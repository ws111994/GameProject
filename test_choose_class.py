from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestChooseClass(TestCase):
    @patch('builtins.input', side_effect=['9', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_class_invalid_input(self, mock_output, _):
        game.choose_class()
        game_printed_this = mock_output.getvalue()
        expected = '1 Rich Man\n2 Smart Man\n3 Sports Man\n4 Gamer\nPlease choose a valid option between 1-4\n1 Rich ' \
                   'Man\n2 Smart Man\n3 Sports Man\n4 Gamer\n'
        self.assertEqual(game_printed_this, expected)

    @patch('builtins.input', return_value='1')
    def test_choose_class_valid_input(self, _):
        actual = game.choose_class()
        expected = 'Rich Man'
        self.assertEqual(actual, expected)
