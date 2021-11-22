from unittest import TestCase

import game


class TestMarkSpecialOnMap(TestCase):
    def test_mark_special_on_map_boss_location(self):
        original_map = [['|_|', '|_|'], ['|_|', '|_|']]
        new_board = {(0, 0): "Starbucks", (0, 1): "DT street", (1, 0): "Starbucks", (1, 1): "Starbucks"}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        expected = '|B|'
        game.mark_special_on_map(new_character, new_board, original_map)
        actual = original_map[-1][-1]
        self.assertEqual(expected, actual)

    def test_mark_special_on_map_character_location(self):
        original_map = [['|_|', '|_|'], ['|_|', '|_|']]
        new_board = {(0, 0): "Starbucks", (0, 1): "DT street", (1, 0): "Starbucks", (1, 1): "Starbucks"}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        expected = '|U|'
        game.mark_special_on_map(new_character, new_board, original_map)
        actual = original_map[new_character['Y-coordinate']][new_character['X-coordinate']]
        self.assertEqual(expected, actual)

    def test_mark_special_on_map_Starbucks_location(self):
        original_map = [['|_|', '|_|'], ['|_|', '|_|']]
        new_board = {(0, 0): "DT street", (0, 1): "DT street", (1, 0): "Starbucks", (1, 1): "DT street"}
        new_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        expected = '|^|'
        game.mark_special_on_map(new_character, new_board, original_map)
        actual = original_map[0][1]
        self.assertEqual(expected, actual)
