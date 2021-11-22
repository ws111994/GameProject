from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['9', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice(self, mock_output, _):
        game.get_user_choice()
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Please choose a direction to move (or quit):\n1 Up\n2 Down\n3 Left\n4 Right' \
                          '\nPlease choose a valid option between 1-4\nPlease choose a direction to move ' \
                          '(or quit):\n1 Up\n2 Down\n3 Left\n4 Right\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', return_value='1')
    def test_get_user_choice_valid_input(self, _):
        expected = '1'
        actual = game.get_user_choice()
        self.assertEqual(expected, actual)
