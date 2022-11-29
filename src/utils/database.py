import mysql.connector
import os

class DatabaseManager:
	"""Docstring for DatabaseManager"""
	def __init__(self, user, password, database=None):
		self.__connection = self.get_db_connection(user, password, database) 

	def get_db_connection(self, user, password, database=None):
		db = mysql.connector.connect(
			host='localhost',
			user=user,
			passwd=password,
			database=database
		)
		return db

	def execute_query(self, q, commit=False):
		db = self.__connection
		with db.cursor() as cursor:
			try:
				cursor.execute(q)
				if commit:
					db.commit()
				print('Query success.')
				if 'SELECT' or 'DESCRIBE' in q:
					return [i for i in cursor]
			except Exception as e:
				print('SK07: Invalid query.')
				print('Program is automatically closed to prevent unwanted action.')
				print('Please contact our developer ASAP, thank you!')
				print(e, os.path.dirname(__file__), __name__)
				exit()

if __name__ == '__main__':
	db = DatabaseManager('root', 'ZiagSQL21_', database='skyline')

	print(db.execute_query(r'''
		SELECT * FROM menu_restaurant
	'''))

	pass