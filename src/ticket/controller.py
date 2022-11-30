# FILE controller.py
# This file is not executable, use TicketController in another file!

import sys
import time

from utils.database import DatabaseManager
from utils.mail import Mail

from .models import Ticket

# Database manager instance
DB = DatabaseManager('user', 'password', database='skyline')


class TicketController:
    # Use case: BELI TIKET
    def buy_ticket(total_tickets, email):
        new_tickets = []
        for i in range(total_tickets):
            ticket = Ticket(email)
            detail = ticket.get_detail_ticket()

            time.sleep(1)

            # Convert boolean into TINYINT
            detail['is_paid'] = 1 if detail['is_paid'] else 0
            DB.execute_query(f'''
				INSERT INTO ticket (email, regular_code, fastpass_code, date_added, ticket_id)
				VALUES (
					'{detail["email"]}',
					{detail["regular_code"]},
					{detail["fastpass_code"]},
					'{detail["date_added"]}',
					{detail["id"]}
				)
			''', commit=True)
            new_tickets.append(ticket)

        # Send ticket ID - Regular code - Fastpass code
        Mail.send_email(new_tickets)

    # Use case: UPGRADE TIKET KE FASTPASS
    def upgrade_ticket(ticket_id, payment_code, balance):
        ticket = TicketController.search_ticket(ticket_id)
        if ticket != None:
            # Ticket type validation
            if ticket[1] == 'Regular':
                # Ticket stat validation
                if ticket[2] == 'Active':
                    TicketController.pay_ticket(
                        ticket_id, payment_code, balance)
                    print('Upgrade ticket success.')
                else:
                    print('SK03: Ticket is not active.')
            else:
                print('SK04: Ticket is already fastpass.')
        else:
            print('SK09: Cannot identify ticket.')

    # Use case: CARI TIKET
    def search_ticket(ticket_id):
        tickets = DB.execute_query(f'''
			SELECT * FROM ticket WHERE ticket_id = {ticket_id}
		''')

        # Ticket validation
        if len(tickets) == 1:
            return tickets[0]
        elif len(tickets) > 1:
            print(f'SK08: Duplicate ID was found.')
        else:
            print('SK06: Ticket not found.')
        return None

    # (Optional) Ticket payment is not handled by Skyline
    def pay_ticket(ticket_id, payment_code, balance):
        ticket = TicketController.search_ticket(ticket_id)

        # Ticket validation
        if ticket != None:
            # Payment code validation
            if payment_code == ticket[5]:
                # Pay for regular ticket
                if balance >= Ticket._Ticket__REGULAR_PRICE:
                    DB.execute_query(f'''
						UPDATE ticket
							SET stat = 'Active'
							WHERE ticket_id = {ticket_id}
					''', commit=True)
                    print('Payment success.')
                else:
                    print('SK02: Insufficient balance.')
            elif payment_code == ticket[6]:
                if balance >= Ticket._Ticket__FASTPASS_PRICE:
                    DB.execute_query(f'''
						UPDATE ticket
							SET stat = 'Active',
								type = 'Fastpass
							WHERE ticket_id = {ticket_id}
					''', commit=True)
                    print('Payment success.')
                else:
                    print('SK02: Insufficient balance.')
            else:
                print('SK01: Invalid payment code.')
        else:
            print('SK09: Cannot identify ticket.')
