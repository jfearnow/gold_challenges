import cafe

while True:
    print('Welcome to Komodo Burgers')
    user_input = input('Choose a menu option:\n' +
                    '1. Add a option\n' +
                    '2. Menu List\n' +
                    '3. Update menu Option\n'
                    '4. Delete Item\n' +
                    '5. Exit\n' +
                    '> ')
                        
    if user_input == '1':
        mealnumber = input('Enter Menu Number: ')
        meal_name = input('Enter Meal Name: ')
        description = input('Enter Description: ')
        ingredients = input('View Ingredients: ')
        price = input('Menu Price: ')
        cafe.add_menus(mealnumber,meal_name, description, ingredients, price)
        # TODO: Refactor user input into a function
        # repeated on line 24-27
    elif user_input == '2':
        menus = cafe.get_menus()
        if len(menus) > 0:
            for item in menus:
                print(item)
    elif user_input == '3':
        menu_to_update = input('Enter menu number to update: ')
        if  cafe.menu_check(menu_to_update):   
            mealnumber = input('Enter new Meal Number: ')
            meal_name = input('Enter new meal name: ')
            description = input('Enter new description: ')
            ingredients = input('Enter new ingredients: ')
            price = input('Enter new price: ')
            cafe.update_menu(menu_to_update, mealnumber,meal_name, description, ingredients, price)
        else:
            print('menu item does not exist')
    elif user_input == '4':
        menu_to_del = input('Enter menu number to delete: ')
        cafe.delete_menu(menu_to_del)

    elif user_input == '5':
        exit()