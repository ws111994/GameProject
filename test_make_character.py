from unittest import TestCase

import game


class TestMakeCharacter(TestCase):
    def test_make_character_correct_values(self):
        character_name = 'Bob'
        class_name = 'Rich Man'
        actual = game.make_character(class_name, character_name)
        expected = {
            'X-coordinate': 0,
            'Y-coordinate': 0,
            'Max HP': 5,
            'Current HP': 5,
            'name': 'Bob',
            'level': 1,
            'exp': 0,
            'class': 'Rich Boi',
            'skill': 'Shopping Spree',
            'damage': 4,
            'item': None
        }
        self.assertEqual(actual, expected)
