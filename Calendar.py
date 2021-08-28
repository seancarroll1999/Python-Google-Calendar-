from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build

'''
    README:
        This is the Calendar class which will display basic data on events happing today.
        refering to this document and the offical Calendar docs.

        calendarID can be found by logging into Google Calendar web application => Calendar Settings => Calendar ID
'''

class Calendar():
    def __init__(self, credentials, calendarId):
        self.Service = build('calendar', 'v3', credentials= credentials)
        self.CalendarId = calendarId
        self.CalendarEvents = None
        

    def GetEvents(self):
        currentDate = datetime.utcnow()
        nextDate = currentDate + timedelta(days=1)
        events_result = self.Service.events().list(calendarId=self.CalendarId, timeMin=currentDate.isoformat() + 'Z', timeMax=nextDate.isoformat() + 'Z').execute()
        events = events_result.get('items', [])
        self.CalendarEvents = events
    
    def DisplayEvents(self):
        for event in self.CalendarEvents:
            print(event['start'].get('date'), event['summary'])
