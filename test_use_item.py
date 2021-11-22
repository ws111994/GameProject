from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestUseItem(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_item_print_output_when_there_is_no_item(self, mock_output):
        new_character = {'item': None}
        new_girl = {'Current HP': 30, 'type': ['Rich Boi', 'Lottery Winner', 'Elon Musk'], 'name': 'Alice'}
        game.use_item(new_character, new_girl)
        expected = 'You frantically searched for something to gift her, but you found none. You missed your timing.\n'
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_use_item_print_output_when_there_is_item(self, mock_output):
        new_character = {'item': 'Something'}
        new_girl = {'Current HP': 30, 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'name': 'Alice'}
        game.use_item(new_character, new_girl)
        expected = 'You gifted Alice Something, she happily accepted it.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_use_item_super_effective_damage_when_girl_is_rich_class(self):
        new_character = {'item': 'Something'}
        new_girl = {'Current HP': 30, 'type': ['Rich Boi', 'Lottery Winner', 'Elon Musk'], 'name': 'Alice'}
        game.use_item(new_character, new_girl)
        expected = 0
        actual = new_girl['Current HP']
        self.assertEqual(expected, actual)

    def test_use_item_normal_damage_when_girl_is_other_class(self):
        new_character = {'item': 'Something'}
        new_girl = {'Current HP': 30, 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'name': 'Alice'}
        game.use_item(new_character, new_girl)
        expected = 15
        actual = new_girl['Current HP']
        self.assertEqual(expected, actual)


