# Python_Google_Calendar_Example
A tutorial showing you how to authorise a python application to access a private google calendar without needing to use OAuth2 sign in page

(Note: this tutorial is being used in Thermal, however any python application can benefit)

## Steps
You have two main options to obtain authorisation from google to access their Calendar API. The First and most common is to use OAuth2 sign in pages. These will create temporary keys which allow you access. This doesn’t suit my personal purpose, if a key expires, I would have to use user input to re-authenticate meaning downtime on Thermal. 

To get around this, we are going to be using something called a Service Account. Now while I don’t know a lot about Googles Service Accounts, I know enough to get this project set up. 

1.	Log into https://console.cloud.google.com/ and set up a new project.
2.	Once your new project is set up, on the left menu select APIs & Services and the select “Library”. From here search and enable the Calendar API for your new project.
3.	Now we need to set up a new Service Account for our project, still in APIs & Services go to “Credentials”
4.	At the top select “Create Credentials” and then “Service Account”. Give your service account a name and small description.
5.	Under step 2 of the service account creation you want to select “Owner” as the role.
6.	Under step 3 of the service account creation you want to enter your google email address into both “Service account users role” and “Service account admins role” then hit Done.
7.	Now let’s link our private calendar with this new service account. Once back on the Credentials page you will now see a long email under Service Accounts. Copy this email address.
8.	Log into Google Calendar web application at: https://calendar.google.com/calendar/
9.	On the left-hand menu, hover over the three dots over the name of the calendar you wish python to access. Select “Settings and Sharing”.
10.	Scroll the settings page until “Share with specific people” here select “Add People” and enter the service account email copied from before.
11.	Now you have a service account linked with your person calendar which can read all events.
12.	We now need to download the service account information to pass into the python code.
13.	Go back to “Credentials” on the google cloud platform and click on the service account email.
14.	Go to “Keys” and select “Add Key” -> “Create new Key” and select “JSON” then finally “create”
15.	Save this json file in the same working directory as the code.
16.	Refer to code comments to set up 

