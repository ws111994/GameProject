from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestGirlCurrentHp(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_girl_current_hp_correct_print_output(self, mock_output):
        girl = {'Current HP': 5, 'Max HP': 10}
        game.girl_current_hp(girl)
        expected = 'Her resistance to your love is [5 / 10].\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_girl_current_hp_parameter_unchanged(self):
        girl = {'Current HP': 5, 'Max HP': 10}
        game.girl_current_hp(girl)
        expected_girl= {'Current HP': 5, 'Max HP': 10}
        self.assertEqual(expected_girl, girl)
