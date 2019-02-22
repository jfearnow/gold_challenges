import unittest
import claim_repo

class ChallengeTwoTests(unittest.TestCase):
        
    def test_create_claim_should_return_claim_list(self):
        # arrange
        claimtype = "Auto"
        description = "Car blows up, lame"
        claimamount = 10000
        dateofincident = "12-11-12"
        dateofclaim = "12-12-12"
        isvalid = True

        # act
        claim_repo.create_claim(claimtype, description, claimamount, dateofincident, dateofclaim, isvalid)
        actual = len(claim_repo.claims)
        expected = 1

        # assert
        self.assertEqual(actual, expected)

    def test_get_claims_should_give_claim_information(self):
        # arrange

        # act
        actual = type(claim_repo.get_claims())
        expected = type([])

        # assert
        self.assertEqual(actual, expected)


    def test_remove_first_claim_from_overall_list(self):
        # arrange
        # act
        expected = 0
        claim_repo.remove_first_claim()
        actual = len(claim_repo.claims)
        # assert
        self.assertEqual(actual, expected)