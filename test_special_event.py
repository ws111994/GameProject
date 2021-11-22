from unittest import TestCase
from unittest.mock import patch
import io

import game


class TestSpecialEvent(TestCase):
    def test_special_event_boost_hp_event(self):
        location = 'Top of Vancouver Revolving Restaurant'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected_character = {'Max HP': 7, 'Current HP': 6, 'exp': 0, 'item': None}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_event_boost_hp_event_print_statement(self, mock_output):
        location = 'Top of Vancouver Revolving Restaurant'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected = 'Your current and max HP is boosted by 2.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_special_event_boost_exp_event(self):
        location = 'Starbucks'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected_character = {'Max HP': 5, 'Current HP': 4, 'exp': 5, 'item': None}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_event_boost_exp_event_print_statement(self, mock_output):
        location = 'Starbucks'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected = 'Your Exp is boosted by 5.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_special_event_item_event(self):
        location = 'Nordstrom'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected_character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': 'LV limited edition handbag'}
        self.assertEqual(expected_character, character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_event_item_event(self, mock_output):
        location = 'Nordstrom'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected = 'You bought a LV limited edition handbag.\n'
        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_special_event_item_is_full_print_statement(self, mock_output):
        location = 'Nordstrom'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': 'Something'}
        game.special_event(location, character)
        expected = 'You already bought a Something, please gift it to someone before buying another one.\n'
        self.assertEqual(expected, mock_output.getvalue())

    def test_special_event_location_remains_unchanged(self):
        location = 'Nordstrom'
        character = {'Max HP': 5, 'Current HP': 4, 'exp': 0, 'item': None}
        game.special_event(location, character)
        expected_location = 'Nordstrom'
        self.assertEqual(expected_location, location)


