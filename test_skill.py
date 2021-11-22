from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestSkill(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_skill_correct_print_output(self, mock_output):
        new_girl = {'name': 'Alice', 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'Current HP': 8}
        new_character = {'class': 'CST Student', 'damage': 2, 'skill': 'Build a game'}
        game.skill(new_character, new_girl)
        expected = 'You initiated your special skill: Build a game!\nAlice is super into you! The skill is ' \
                   'very effective!\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_skill_super_effective_type(self):
        new_girl = {'name': 'Alice', 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'Current HP': 8}
        new_character = {'class': 'CST Student', 'damage': 2, 'skill': 'Build a game'}
        game.skill(new_character, new_girl)
        expected = 4
        actual = new_girl['Current HP']
        self.assertEqual(expected, actual)

    def test_skill_non_effective_type(self):
        new_girl = {'name': 'Alice', 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'Current HP': 8}
        new_character = {'class': 'Rich Boi', 'damage': 2, 'skill': 'Build a game'}
        game.skill(new_character, new_girl)
        expected = 7
        actual = new_girl['Current HP']
        self.assertEqual(expected, actual)

    def test_skill_character_unchanged(self):
        new_girl = {'name': 'Alice', 'type': ['CST Student', 'Indie Game Developer', 'Naoki Yoshida'], 'Current HP': 8}
        new_character = {'class': 'Rich Boi', 'damage': 2, 'skill': 'Build a game'}
        game.skill(new_character, new_girl)
        expected = {'class': 'Rich Boi', 'damage': 2, 'skill': 'Build a game'}
        self.assertEqual(expected, new_character)


