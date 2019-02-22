
class Menu:

    def __init__(self, mealnumber,meal_name, description, ingredients, price):
            self.meal = mealnumber
            self.name = meal_name
            self.description = description
            self.ingredients = ingredients
            self.price = price

    def __repr__(self):
        return f'{self.meal}: {self.name}:'




