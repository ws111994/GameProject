from unittest import TestCase

import game


class TestCheckQuit(TestCase):
    def test_check_quit_user_choose_to_quit(self):
        user_choice = 'quit'
        expectation = True
        actual = game.check_quit(user_choice)
        self.assertEqual(expectation, actual)

    def test_check_quit_user_choose_to_not_quit(self):
        user_choice = 'something else'
        expectation = False
        actual = game.check_quit(user_choice)
        self.assertEqual(expectation, actual)

    def test_check_quit_user_choice_is_unchanged(self):
        user_choice = 'something else'
        expectation = 'something else'
        game.check_quit(user_choice)
        self.assertEqual(expectation, user_choice)
