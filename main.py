#!/usr/bin/env python3
import requests

filename = 'emails.txt'
domain = 'lio-support'
api_key = 'LrMouVFEnodY2LfefTBo'
user_email = 'support@lio-support.freshdesk.com'
subject = 'ok'
description = 'Details about the issue...'

json_data = {
	'description': description,
	'subject': subject,
	'email': user_email,
	'priority': 1,
	'status': 2,
}

headers = {}							# you can add your own headers

def send_mail(domain, api_key, email_list,json_data, headers):
	json_data['cc_emails'] = email_list
	res = requests.post(f'https://{domain}.freshdesk.com/api/v2/tickets',
							headers=headers, json=json_data, auth=(api_key, 'X'))
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
	send_mail(domain, api_key, email_list, json_data, headers)
