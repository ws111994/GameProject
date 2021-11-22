from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestIntroduction(TestCase):
    @patch('random.randint', return_value=101)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_introduction_correct_names(self, mock_output, _):
        character = {'name': 'Bob'}
        boss = {'name': 'Alice'}
        game.introduction(character, boss)
        game_printed_this = mock_output.getvalue()
        expected = "Welcome to this world for the 101th time, Bob.\nYour girlfriend, Alice, has been acting weird " \
                   "lately. You think something is not right.\nMaybe it's you, maybe it's her, maybe there's " \
                   "something else in the dark. You woke up this morning to an\nempty bed, she is gone, disappeared. " \
                   "You frantically called all your friends about it, but they don't\neven seem to recognize her " \
                   "name anymore. You looked at the calendar, May 23th 2014, the day you met her\nseven years ago. " \
                   "You hear a mysterious voice inside your head: She is out there, somewhere waiting to\nfall in " \
                   "love with you again. Go, find her. You have so many questions about your current situation." \
                   "\nDid you travel back in time? Was this a dream I had before? The mysterious voice remained " \
                   "silent.\nEven though this is surreal in every aspect, you have decided to find her, again...." \
                   "again...again...?\n(Why am I saying AGAIN?)\n"
        self.assertEqual(game_printed_this, expected)

    @patch('random.randint', return_value=101)
    def test_introduction_parameters_unchanged(self, _):
        character = {'name': 'Bob'}
        boss = {'name': 'Alice'}
        game.introduction(character, boss)
        expected_character = {'name': 'Bob'}
        expected_boss = {'name': 'Alice'}
        self.assertEqual(expected_boss, boss)
        self.assertEqual(expected_character, character)
