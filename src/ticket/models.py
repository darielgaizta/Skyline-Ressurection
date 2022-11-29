# FILE: models.py

from datetime import datetime

import time
import random

class Ticket(object):
	__REGULAR_PRICE = 150000
	__FASTPASS_PRICE = 300000

	"""Docstring for Ticket"""
	def __init__(self, email):
		self.__id = int(time.time())
		self.__type = 'Regular'
		self.__stat = 'Expired'
		self.__is_paid = False
		self.__email = email
		random.seed(self.__id)
		self.__regular_code = int(str(random.random())[-5:])
		random.seed(self.__regular_code)
		self.__fastpass_code = int(str(random.random())[-5:])
		self.__date_added = str(datetime.now().strftime("%Y-%m-%d"))

	# GETTER
	# Get all attributes
	def get_detail_ticket(self):
		return {
			'id': self.__id,
			'type': self.__type,
			'stat': self.__stat,
			'is_paid': self.__is_paid,
			'email': self.__email,
			'regular_code': self.__regular_code,
			'fastpass_code': self.__fastpass_code,
			'date_added': self.__date_added
		}

	# METHOD
	# Ticket type validation
	def validate_ticket_type(self, type):
		return self.__type == type

	# Ticket status validation
	def validate_ticket_stat(self, stat):
		return self.__stat == stat

	# Regular code validation
	def validate_regular_code(self, regular_code):
		return self.__regular_code == regular_code

	# Fastpass code validation
	def validate_fastpass_code(self, fastpass_code):
		return self.__fastpass_code == fastpass_code

	# Upgrade ticket to fastpass
	def upgrade(self):
		if self.validate_ticket_type('Fastpass'):
			print('Your ticket is already Fastpass.')
		else:
			self.__type = 'Fastpass'

	# Activate Ticket
	def activate(self):
		self.__stat = 'Active'
		self.__is_paid = True

	# Deactivate ticket
	def deactivate(self):
		self.__stat = 'Expired'
		self.__is_paid = False