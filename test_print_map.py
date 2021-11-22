from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestPrintMap(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_correct_output(self, mock_output):
        original_map = [['|U|', '|^|'], ['|_|', '|B|']]
        expected = '|U||^|\n|_||B|\n'
        game.print_map(original_map)
        the_game_printed_this = mock_output.getvalue()
        self.assertEqual(expected, the_game_printed_this)

