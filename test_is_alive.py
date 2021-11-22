from unittest import TestCase

import game


class TestIsAlive(TestCase):
    def test_is_alive_zero_hp(self):
        character = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 0}
        expected = False
        actual = game.is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_positive_hp(self):
        character = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 1}
        expected = True
        actual = game.is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_negative_hp(self):
        character = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': -1}
        expected = False
        actual = game.is_alive(character)
        self.assertEqual(expected, actual)

    def test_is_alive_parameter_unchanged(self):
        character = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 0}
        game.is_alive(character)
        expected = {'X-coordinate': 2, 'Y-coordinate': 3, 'Current HP': 0}
        self.assertEqual(expected, character)
