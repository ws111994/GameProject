from unittest import TestCase
from unittest.mock import patch


import game


class TestMakeBoard(TestCase):
    @patch('random.randint', return_value=0)
    def test_make_board_correct_dictionary_format(self, _):
        rows = 2
        columns = 2
        expected = {(0, 0): 'Top of Vancouver Revolving Restaurant', (0, 1): 'Top of Vancouver Revolving Restaurant',
                    (1, 0): 'Top of Vancouver Revolving Restaurant', (1, 1): 'Top of Vancouver Revolving Restaurant'}
        actual = game.make_board(rows, columns)
        self.assertEqual(expected, actual)

    def test_make_board_number_of_keys_generated(self):
        rows = 2
        columns = 2
        expected = rows * columns
        actual = len(game.make_board(rows, columns).keys())
        self.assertEqual(expected, actual)

    def test_make_board_key_as_tuple(self):
        rows = 2
        columns = 2
        new_board = game.make_board(rows, columns)
        expected = {tuple}
        actual = set(map(type, new_board))
        self.assertEqual(expected, actual)

    def test_make_board_value_as_string(self):
        rows = 2
        columns = 2
        new_board = game.make_board(rows, columns)
        expected = {str}
        actual = set(map(type, new_board.values()))
        self.assertEqual(expected, actual)
