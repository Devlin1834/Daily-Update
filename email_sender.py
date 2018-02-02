# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:51:15 2018

@author: Devlin
"""
####################################################################################################
### A lot of this is pretty shamelessly copied from googles examples. But I figure that there's ####
### no need to rewrite what works, especially seeing as I don't really understand why this works ###
### or how they came up with this in the first place. ##############################################

import base64
import httplib2
from apiclient import discovery
from email.mime.text import MIMEText
import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import email_writer

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,'gmail-python-quickstart.json')
    store = Storage(credential_path)
    credentials = store.get()
    
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
        
    return credentials

def send_message(service, user_id, message):
  message = (service.users().messages().send(userId=user_id, body=message).execute())
  return message


def create_message(sender, to, subject, message_text):
### I actually changed part of this one so haha google I beat you at your own game
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()} # Changed .as_string() to .as_bytes() then added .decode()
                                                                        # It was broken and I made it work
####################################################################################################
### Here's the part where I actually send the email ################################################
                                                                        
credentials = get_credentials()
service = discovery.build('gmail', 'v1', http = credentials.authorize(httplib2.Http()))

recipients = [email_writer.recipient_one, email_writer.recipient_two]
for r in recipients:
    message_one = create_message(email_writer.sender_one, r, email_writer.subject, email_writer.daily_update)
    send_message(service, 'me', message_one)

