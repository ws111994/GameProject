from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestClassAdvancement(TestCase):
    def test_class_advancement_correct_class_advancement(self):
        new_character = {'class': 'Rich Boi', 'level': 2}
        game.class_advancement(new_character)
        expected = 'Lottery Winner'
        actual = new_character['class']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_class_advancement_correct_print_statement(self, mock_output):
        new_character = {'class': 'Rich Boi', 'level': 2}
        game.class_advancement(new_character)
        expected = 'Others start to call you Lottery Winner, you feel like you are on a whole new level!\n'
        self.assertEqual(expected, mock_output.getvalue())
