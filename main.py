#!/usr/bin/env python3
import requests

################################################
#     Authentification for more see images 
################################################
domain = 'lio-support'
api_key = '*****************'
user_email = 'support@lio-support.freshdesk.com'
################################################
filename = 'emails_file.txt'
subject = 'Text'
description = 'Your message in html format ...'

# you can add more option 
# by adding parameters from link:
# https://developers.freshdesk.com/api/#tickets
data = {
	'description': description,
	'subject': subject,
	'email': user_email,
	'priority': 1,
	'status': 2,
	'source': 2,
}

# you can add your own headers
headers = {}

def send_mail(domain, api_key, email_list, data, headers):
	data['cc_emails'] = email_list
	res = requests.post(f'https://{domain}.freshdesk.com/api/v2/tickets',
							headers=headers, json=data, auth=(api_key, 'X'))
	if res.status_code == 201:
		print('Email send success.')
	else:
		print(f'Email send error code {res.status_code}')

def get_list(filename):
	with open(filename, 'r') as f:
		li = f.read().splitlines()		# split emails file by line 
	li = list(dict.fromkeys(li))		# remove duplicated mails
	return li

if __name__ == '__main__':
	email_list = get_list(filename)
	send_mail(domain, api_key, email_list, data, headers)
