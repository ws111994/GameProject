from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestDescribeGirl(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_girl_correct_print_output(self, mock_output):
        girl = {'name': 'Alice'}
        game.describe_girl(girl)
        expected = '*** A wild Alice appears ! ***\n'
        game_printed_this = mock_output.getvalue()
        self.assertEqual(expected, game_printed_this)

    def test_describe_girl_parameter_unchanged(self):
        girl = {'name': 'Alice'}
        game.describe_girl(girl)
        expected_girl = {'name': 'Alice'}
        self.assertEqual(expected_girl, girl)
