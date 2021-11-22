from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestGirlFlee(TestCase):
    @patch('random.randint', return_value=1)
    def test_girl_flee_she_chose_to_flee(self, _):
        girl = {'name': 'Alice'}
        actual = game.girl_flee(girl)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=2)
    def test_girl_flee_she_chose_not_to_flee(self, _):
        girl = {'name': 'Alice'}
        actual = game.girl_flee(girl)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_girl_flee_print_statement_when_girl_flee(self, mock_output, _):
        girl = {'name': 'Alice'}
        game.girl_flee(girl)
        expected = 'Alice is not interested in you anymore, she walked away like you never existed.\n'
        self.assertEqual(mock_output.getvalue(), expected)

    def test_girl_flee_parameter_unchanged(self):
        girl = {'name': 'Alice'}
        game.girl_flee(girl)
        expected = {'name': 'Alice'}
        self.assertEqual(girl, expected)
