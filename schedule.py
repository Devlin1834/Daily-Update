# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 23:11:20 2018

@author: Devlin
"""

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_todays_schedule():

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().replace(hour = 1, minute = 0).isoformat() + 'Z' # 'Z' indicates UTC time
    later = datetime.datetime.utcnow().replace(hour = 23, minute = 59).isoformat() + 'Z' # 'Z' indicates UTC time
    
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, timeMax=later, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    
    up_to = {'All-Days': [],
             'Events': []
             }
    
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', '')[11:16]
        end = event['end'].get('dateTime', '')[11:16]
        location = event.get('location', '')
        if start == '':
            up_to['All-Days'].append(event)
        else:
            item = '(' + start + '-' + end + ') ' + event['summary'] + ' @ ' + location
            up_to['Events'].append(item)
            
    return up_to

if __name__ == '__main__':
    print(get_todays_schedule())