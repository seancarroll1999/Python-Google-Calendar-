import os.path
from google.oauth2 import service_account
import json
    
'''
    README
        replace Service_Token.json with the credentials downloaded from the cloud platform
'''

def ServiceAuth():
    with open('Service_Token.json') as source:
        info = json.load(source)
        credentials = service_account.Credentials.from_service_account_info(info)
        return credentials
