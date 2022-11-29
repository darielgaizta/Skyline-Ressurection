# FILE: models.py
# Model for transport as in MVC architecture

class Transport(object):
	"""Docstring for Transport"""
	def __init__(self, name, schedule_start, schedule_end, origin, destination):
		self.__name = name
		self.__schedule_start = schedule_start
		self.__schedule_end = schedule_end
		self.__origin = origin
		self.__destination = destination

	# GETTER
	# Get all attributes
	def get_detail_transport(self):
		return {
			'name': self.__name,
			'schedule_start': self.__schedule_start,
			'schedule_end': self.__schedule_end,
			'origin': self.__origin,
			'destination': self.__destination
		}