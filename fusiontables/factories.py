import httplib2
from oauth2client import client
from apiclient.discovery import build
from fusiontables.services import FusionTableService

class GoogleAuthFactory:
    def __init__(self):
        self.flow = self.flow = client.flow_from_clientsecrets(
            'client_secrets.json',
            scope='https://www.googleapis.com/auth/fusiontables',
            redirect_uri='http://localhost:8000'
        )
        self.flow.params['access_type'] = 'offline'
        self.flow.params['include_granted_scopes'] = 'true'

    def build_authorization_url(self):
        return self.flow.step1_get_authorize_url()

    def build_credentials(self, code):
        credentials = self.flow.step2_exchange(code)
        return credentials.to_json()
    
    def build_service(self, credentialsSession):
        credentials = client.OAuth2Credentials.from_json(credentialsSession)
        http_auth = credentials.authorize(httplib2.Http())
        service = build('fusiontables', 'v2', http=http_auth)
        return FusionTableService(service)