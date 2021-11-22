from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestCharm(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_charm_correct_print_output(self, mock_output):
        new_attacker = {'damage': 1, 'name': 'Alice'}
        new_receiver = {'Current HP': 2, 'name': 'Bob'}
        game.charm(new_attacker, new_receiver)
        expected = 'Alice tried to charm Bob.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_charm_receiver_dead_with_zero_hp(self):
        new_attacker = {'damage': 2, 'name': 'Alice'}
        new_receiver = {'Current HP': 2, 'name': 'Bob'}
        game.charm(new_attacker, new_receiver)
        expected = 0
        actual = new_receiver['Current HP']
        self.assertEqual(expected, actual)

    def test_charm_receiver_dead_with_overkill_damage(self):
        new_attacker = {'damage': 100, 'name': 'Alice'}
        new_receiver = {'Current HP': 2, 'name': 'Bob'}
        game.charm(new_attacker, new_receiver)
        expected = 0
        actual = new_receiver['Current HP']
        self.assertEqual(expected, actual)
