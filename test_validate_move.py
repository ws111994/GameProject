from unittest import TestCase


import game


class TestValidateMove(TestCase):
    def test_validate_move_invalid_move(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = (-1, 0)
        expected = False
        actual = game.validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_valid_move(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = (1, 0)
        expected = True
        actual = game.validate_move(board, character, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_parameters_unchanged(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = (1, 0)
        expected_board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room',
                          (1, 1): 'Treasure room'}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        game.validate_move(board, character, direction)
        self.assertEqual(expected_character, character)
        self.assertEqual(expected_board, board)
