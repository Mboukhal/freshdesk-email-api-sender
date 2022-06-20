#!/usr/bin/env python3
import requests
from info import *

json_data = {
	'description': description,
	'subject': subject,
	'email': user_email,
	'priority': 1,
	'status': 2,
}

def send_mail(domain, api_key, email_list):
	global json_data
	json_data['cc_emails'] = email_list
	headers = {}
	response = requests.post(f'https://{domain}.freshdesk.com/api/v2/tickets', headers=headers, json=json_data, auth=(api_key, 'X'))
	if response.status_code == 201:
		print('Email send success.')
	else:
		print(f'Email send error code {response.status_code}')

if __name__ == '__main__':
	with open(filename, 'r') as f:
		li = f.read().splitlines()
	li = list(dict.fromkeys(li))
	send_mail(domain, api_key, li)
