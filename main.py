from Calendar import Calendar
import Auth as Auth

def main():
    #Get credentials
    credentials = Auth.ServiceAuth() 

    #Load calendar using credentials and calendarID   
    calendar = Calendar(credentials, 'CALENDAR_ID@gmail.com')

    #Get the events of the day
    calendar.GetEvents()

    #Display the events for GetEvents() 
    calendar.DisplayEvents()

if __name__ == '__main__':
    main()