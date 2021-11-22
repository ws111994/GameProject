from unittest import TestCase
from unittest.mock import patch

import game


class TestGenerateBoss(TestCase):
    @patch('random.randint', return_value=0)
    def test_generate_boss_correct_values(self, _):
        expected = {
            'name': 'Griana Arande',
            'Current HP': 50,
            'Max HP': 50,
            'damage': 6,
            'type': ['Rich Boi', 'Lottery Winner', 'Elon Musk'],
            'boss': True
        }
        actual = game.generate_boss()
        self.assertEqual(expected, actual)
