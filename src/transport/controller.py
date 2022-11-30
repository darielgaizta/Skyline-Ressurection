# FILE: controller.py
# This file is not executable, use TicketController in another file!

from utils.database import DatabaseManager

DB = DatabaseManager('user', 'password', database='skyline')


class TransportController:
    # Use case: MELIHAT JADWAL TRANSPORTASI UMUM
    def get_all_transports():
        return DB.execute_query(r'''
			SELECT * FROM transport
		''')
