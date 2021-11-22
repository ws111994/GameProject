from unittest import TestCase


import game


class TestMoveCharacter(TestCase):
    def test_move_character_character_is_modified(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = (1, 0)
        expected = False
        game.move_character(character, direction)
        actual = character == {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(expected, actual)

    def test_move_character_character_coordinate_change_correctly(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        direction = (1, 0)
        expected = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        game.move_character(character, direction)
        actual = character
        self.assertEqual(expected, actual)