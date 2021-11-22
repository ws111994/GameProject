from unittest import TestCase


import game


class TestCheckIfAtBossLocation(TestCase):
    def test_check_if_at_boss_location_not_at_boss_location(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        expected = False
        actual = game.check_if_at_boss_location(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_at_boss_location_at_boss_location(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        expected = True
        actual = game.check_if_at_boss_location(board, character)
        self.assertEqual(expected, actual)

    def test_check_if_at_boss_location_first_input_is_not_modified(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        actual = game.check_if_at_boss_location(board, character)
        expected = True
        actual = board == {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room',
                           (1, 1): 'Treasure room'}
        self.assertEqual(expected, actual)

    def test_check_if_if_at_boss_location_second_input_is_not_modified(self):
        board = {(0, 0): 'Empty room', (0, 1): 'Dangerous room', (1, 0): 'Treasure room', (1, 1): 'Treasure room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        actual = game.check_if_at_boss_location(board, character)
        expected = True
        actual = character == {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(expected, actual)
