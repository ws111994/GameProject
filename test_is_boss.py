from unittest import TestCase

import game


class TestIsBoss(TestCase):
    def test_is_boss_when_girl_is_boss(self):
        girl = {'boss': True}
        actual = game.is_boss(girl)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_boss_when_girl_is_not_boss(self):
        girl = {'boss': False}
        actual = game.is_boss(girl)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_boss_girl_is_unchanged(self):
        girl = {'boss': False}
        game.is_boss(girl)
        expected = {'boss': False}
        self.assertEqual(girl, expected)
