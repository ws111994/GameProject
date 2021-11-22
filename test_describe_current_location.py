from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_correct_print_output(self, mock_output):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0}
        game.describe_current_location(board, character)
        game_printed_this = mock_output.getvalue()
        expected = 'You are at (0, 0)\nCurrent area is Empty room\n'
        self.assertEqual(game_printed_this, expected)

    def test_describe_current_location_both_parameters_remain_unchanged(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        game.describe_current_location(board, character)
        expected_board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room',
                          (1, 1): 'Treasure room'}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(expected_board, board)
        self.assertEqual(expected_character, character)