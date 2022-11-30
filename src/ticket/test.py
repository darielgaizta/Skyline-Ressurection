#file:test.py
import unittest
import controller

from ..utils.database import DatabaseManager

from models import Ticket

DB = DatabaseManager('root', 'utankayu88', database='skyline')

##melakukan test fungsi search,buy, dan upgrade tiket
class TestControllerTicket(unittest.TestCase):
    def test_search(self):    
        ticket=controller.TicketController.search_ticket(1669730687) 
        self.assertIs(type(ticket), tuple)
        # # cek value
        # with self.assertRaises(TypeError):
        #     controller.TicketController.search_ticket(None) 

    def test_upgrade(self):
        controller.TicketController.upgrade_ticket(1669730687,27292,int(400000))
        ticket=controller.TicketController.search_ticket(1669730687)
        self.assertTrue(ticket[1]=='Fastpass')
   
    def test_buy(self):
        controller.TicketController.buy_ticket(int(1),"test@std")
        ticket= DB.execute_query(f'''
			SELECT * FROM ticket WHERE email = "test@std"
		''')
        self.assertTrue(type(ticket),tuple)