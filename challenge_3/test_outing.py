import unittest
import outing_repo

class ChallengeThreeTests(unittest.TestCase):

    def test_Outing_should_show_event_totals(self):
        # arrange
        # act
        outing_repo.create_outing("event_type", 50, "date", 10)
        actual = len(outing_repo.outings)
        expected = 1

        # assert
        self.assertEqual(actual, expected)
    def test_get_outings_is_list(self):
        # arrange
        # act
        actual = type(outing_repo.get_outings())
        expected = type([])
        # assert
        self.assertEqual(actual, expected)
    def test_get_total_cost_of_outing(self):
        # arrange
        # act
        outing_repo.total_by_type(500)
        actual = len(outing_repo.outings)
        expected = 1

        # assert
        self.assertEqual(actual, expected)
    

         
