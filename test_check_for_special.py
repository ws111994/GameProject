from unittest import TestCase

import game


class TestCheckForSpecial(TestCase):
    def test_check_for_special_location_is_special(self):
        location = 'Starbucks'
        actual = game.check_for_special(location)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_for_special_location_is_not_special(self):
        location = 'DT street'
        actual = game.check_for_special(location)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_for_special_location_is_not_changed(self):
        location = 'DT street'
        game.check_for_special(location)
        expected_location = 'DT street'
        self.assertEqual(location, expected_location)
