from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestGetUserAction(TestCase):
    @patch('builtins.input', side_effect=['9', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_action_invalid_input(self, mock_output, _):
        game.get_user_action()
        expected = '1 Charm\n2 Skill\n3 Item\n4 Flee\nPlease choose a valid option between 1-4\n1 Charm\n2 Skill\n3 ' \
                   'Item\n4 Flee\n'
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_action_valid_input(self, mock_output, _):
        actual = game.get_user_action()
        expected = 'Charm'
        self.assertEqual(expected, actual)
