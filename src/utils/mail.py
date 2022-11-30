from email.message import EmailMessage

import os
import ssl
import smtplib

# WARNING: This is our email credentials
# Please use it with all of your heart, do not ruin our life. Thanks! :)
SOURCE = 'skylinedeveloperteam@gmail.com'
PASSWORD = 'vmvmdaltglfmikfz'

class Mail:
	def send_email(tickets):
		global SOURCE, PASSWORD

		subj = 'Here Is Your Skyline Ticket!'
		
		# Get detail ticket
		body = ''
		addr = ''

		for ticket in tickets:
			detail_ticket = ticket.get_detail_ticket()
			body += f'ID {detail_ticket["id"]} - {detail_ticket["regular_code"]} - {detail_ticket["fastpass_code"]}\n'
			addr = detail_ticket['email']

		# Build email message
		mail = EmailMessage()
		mail['From'] = SOURCE
		mail['To'] = addr

		# Set subject and content
		mail['subject'] = subj
		mail.set_content(body)

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
			smtp.login(SOURCE, PASSWORD)
			smtp.sendmail(SOURCE, addr, mail.as_string())

if __name__ == '__main__':
	pass