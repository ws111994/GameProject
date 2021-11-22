from unittest import TestCase

import game


class TestCurrentLocation(TestCase):
    def test_current_location_correct_output(self):
        new_board = {(0, 0): 'Empty room'}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        actual = game.current_location(new_board, new_character)
        expected = 'Empty room'
        self.assertEqual(actual, expected)

    def test_current_location_parameters_unchanged(self):
        new_board = {(0, 0): 'Empty room'}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        game.current_location(new_board, new_character)
        expected_board = {(0, 0): 'Empty room'}
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        self.assertEqual(expected_board, new_board)
        self.assertEqual(expected_character, new_character)