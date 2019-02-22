import unittest
import cafe_repo as cafe


class ChallengeOneTests(unittest.TestCase):

    def test_menu_add_should_show_item_added(self):
            # arrange
            self.meal_number = '1'
            self.name = 'meal_name'
            self.description = 'description'
            self.ingredients = 'ingredients'
            self.price = 'price'

            # act
            cafe.add_menus(self.meal_number, self.name, self.description, self.ingredients, self.price)
            actual = 1

            # assert
            self.assertEqual(actual, len(cafe.menus))
    def test_method_item_should_be_deleted(self):
            # arrange
            #act
            actual = len(cafe.get_menus())
            expected = 1

            # assert
            self.assertEqual(actual, expected)
        

    def test_get_menu_should_return_menu_item(self):
            # arrange
            # act
            actual = type(cafe.get_menus())
            expected = type([])
            # assert
            self.assertEqual(actual, expected) 

