# FILE: models.py

class Restaurant(object):
	"""Docstring for Restaurant"""
	def __init__(self, name, lokasi):
		self.__name = name
		self.__location = location

	# GETTER
	# Get all attributes
	def get_detail_restaurant(self):
		return {
			'name': self.__name,
			'location': self.__location
		}

class MenuRestaurant(object):
	"""Docstring for MenuRestaurant"""
	def __init__(self, name, price, description):
		self.__name = name
		self.__price = price
		self.__description = description
	
	# GETTER
	# Get all attributes
	def get_detail_menu_restaurant(self):
		return {
			'name': self.__name,
			'price': self.__price,
			'description': self.__description
		}