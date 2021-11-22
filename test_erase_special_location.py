from unittest import TestCase

import game


class TestEraseSpecialLocation(TestCase):
    def test_erase_special_location_successful_convert_special_back_to_normal(self):
        new_board = {(0, 0): 'Starbucks'}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        game.erase_special_location(new_board, new_character)
        expected = 'DT street'
        actual = new_board[(0, 0)]
        self.assertEqual(expected, actual)

    def test_erase_special_location_character_unchanged(self):
        new_board = {(0, 0): 'Starbucks'}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        game.erase_special_location(new_board, new_character)
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        self.assertEqual(expected_character, new_character)