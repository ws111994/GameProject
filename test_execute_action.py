from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestExecuteAction(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_action_successful_invoke_charm_function(self, mock_output):
        action = 'Charm'
        girl = {'Current HP': 2, 'name': 'Alice'}
        character = {'damage': 1, 'name': 'Bob'}
        game.execute_action(action, character, girl)
        expected = 'Bob tried to charm Alice.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_execute_action_action_is_unchanged(self):
        action = 'Charm'
        girl = {'Current HP': 2, 'name': 'Alice'}
        character = {'damage': 1, 'name': 'Bob'}
        game.execute_action(action, character, girl)
        expected = 'Charm'
        self.assertEqual(expected, action)

