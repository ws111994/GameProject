from unittest import TestCase

import game


class TestConvertToDirectionOffset(TestCase):
    def test_convert_to_direction_offset_correct_output(self):
        user_choice = '1'
        expected = (0, -1)
        actual = game.convert_to_direction_offset(user_choice)
        self.assertEqual(expected, actual)

    def test_convert_to_direction_offset_correct_output_type(self):
        user_choice = '1'
        expected = tuple
        actual = type(game.convert_to_direction_offset(user_choice))
        self.assertEqual(expected, actual)

    def test_convert_to_direction_offset_parameter_unchanged(self):
        user_choice = '1'
        expected = '1'
        game.convert_to_direction_offset(user_choice)
        self.assertEqual(expected, user_choice)
