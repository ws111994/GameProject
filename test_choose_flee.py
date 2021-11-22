from unittest import TestCase

import game


class TestChooseFlee(TestCase):
    def test_choose_flee_action_is_to_flee(self):
        action = 'Flee'
        actual = game.choose_flee(action)
        expected = True
        self.assertEqual(expected, actual)

    def test_choose_flee_action_is_not_flee(self):
        action = 'Something Else'
        actual = game.choose_flee(action)
        expected = False
        self.assertEqual(expected, actual)

    def test_choose_flee_action_is_unchanged(self):
        action = 'Something Else'
        game.choose_flee(action)
        expected = 'Something Else'
        self.assertEqual(expected, action)
