from menus import Menu


'''
This module will handle the UI
and CRUD Functionality of the Menus object
'''
#CRUD: Create, Read Update Delete

menus = []

def add_menus(meal_number, name, description, ingredients, price):
    m = Menu(meal_number, name, description, ingredients, price)
    menus.append(m)


def get_menus():
    return menus


def menu_check(number_check):
    for item in menus:
      if item.meal == number_check:
        return True
    else:
      return False
# update is the same as dele
# te and recreate
def update_menu(update_number, meal_number, name, description, ingredients, price):
    for item in menus:
        if item.meal == update_number:
            item_index = menus.index(item)
            temp = Menu(meal_number, name, description, ingredients, price)
            menus[item_index] = temp
    
    
# add_menus(meal_number, name, description, ingredients, price)


def delete_menu(menunum):
    for item in menus:
            if menunum == item.meal:
                item_index = menus.index(item)
                menus.pop(item_index)
