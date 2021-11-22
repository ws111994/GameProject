from unittest import TestCase
from unittest.mock import patch


import game


class TestCheckForGirls(TestCase):
    @patch('random.randint', return_value=1)
    def test_check_for_girls_encounter_girl(self, _):
        expected = True
        actual = game.check_for_girls()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_check_for_girls_does_not_encounter_girl(self, _):
        expected = False
        actual = game.check_for_girls()
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 2, 3, 4, 5])
    def test_check_for_girls_one_fifth_chance_to_encounter_girl(self, _):
        result = []
        count = 0
        while count != 5:
            result.append(game.check_for_girls())
            count += 1
        expected = [True, False, False, False, False]
        self.assertEqual(expected, result)
