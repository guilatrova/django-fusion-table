import httplib2
from oauth2client import client
from apiclient.discovery import build
from fusiontables.services import FusionTableService

API = 'AIzaSyDEvQmQvSFTHflZDB-xtZTct7EBjYewBaw'
CLIENT_ID = '259366732937-muj5ftopo9otfbgakhblsr8dbq7eidrn.apps.googleusercontent.com'
SECRET_KEY = 'fPJddDe1YTItwgKSN0JabMI7'

class GoogleAuthFactory:
    def __init__(self):
        self.flow = self.flow = client.flow_from_clientsecrets(
            'client_secrets.json',
            scope='https://www.googleapis.com/auth/fusiontables',
            redirect_uri='http://localhost:8000'
        )

    def build_authorization_url(self):
        return self.flow.step1_get_authorize_url()

    def build_credentials(self, code):
        return self.flow.step2_exchange(code)
    
    def build_service(self, credentials):
        http_auth = credentials.authorize(httplib2.Http())
        service = build('fusiontables', 'v2', http=http_auth)
        return FusionTableService(service)
