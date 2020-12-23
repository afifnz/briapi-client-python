from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

from .config import ApiConfig


class Auth:
    """
    Briva object used to do request to Briva API
    """

    def __init__(self, 
            is_production=False,
            client_secret='',
            client_id='',
            token=''):

        self.config = ApiConfig(is_production, client_secret, client_id, token)

    @property
    def config(self):
        return self.__config

    @config.setter
    def config(self, new_value):
        self.__config = new_value

    def access_token(self):
        client = BackendApplicationClient(client_id=self.config.client_id)
        oauth = OAuth2Session(client=client)
        token_url = f"{self.config.get_api_base_url()}/oauth/client_credential/accesstoken?grant_type=client_credentials"
        response = oauth.fetch_token(token_url=token_url, client_id=self.config.client_id, client_secret=self.config.client_secret)
        return response.get('access_token')
