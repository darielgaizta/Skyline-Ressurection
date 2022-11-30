# FILE: controller.py
# This file is not executable, use RestaurantController in another file!

from utils.database import DatabaseManager

DB = DatabaseManager('user', 'password', database='skyline')


class RestaurantController:
    # Use case: MELIHAT SEMUA RESTORAN YANG ADA DI THEME PARK
    def get_all_restaurants():
        return DB.execute_query(r'''
			SELECT * FROM restaurant
		''')

    # Use case: MELIHAT SEMUA MENU YANG ADA DI RESTORAN
    def get_menu_restaurant(restaurant_id):
        return DB.execute_query(f'''
			SELECT * FROM menu_restaurant
				WHERE restaurant_id = {restaurant_id}
		''')
