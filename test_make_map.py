from unittest import TestCase

import game


class TestMakeMap(TestCase):
    def test_make_map_correct_2d_list(self):
        rows = 2
        columns = 2
        expected = [['|_|', '|_|'], ['|_|', '|_|']]
        new_map = game.make_map(rows, columns)
        self.assertEqual(expected, new_map)

    def test_make_map_correct_list_length(self):
        rows = 2
        columns = 2
        expected = rows * columns
        new_map = game.make_map(rows, columns)
        actual = len(new_map) * len(new_map[0])
        self.assertEqual(expected, actual)

