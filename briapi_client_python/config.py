class ApiConfig:
    """
    Config Object that used to store is_production, client_secret, client_id.
    And also API base urls.
    note: client_id is not necessarily required for API call.
    """
    SANDBOX_BASE_URL = 'https://sandbox.partner.api.bri.co.id'
    PRODUCTION_BASE_URL = 'https://partner.api.bri.co.id'

    def __init__(self, 
            is_production=False,
            client_secret='',
            client_id='',
            token=''):
        self.is_production = is_production
        self.client_secret = client_secret
        self.client_id = client_id
        self.token = token

    def get_api_base_url(self):
        if self.is_production: 
            return self.PRODUCTION_BASE_URL
        return self.SANDBOX_BASE_URL

    # properties setter
    def set(self,
            is_production=None,
            client_secret=None,
            client_id=None,
            token=None):
        if is_production is not None:
            self.is_production = is_production
        if client_secret is not None:
            self.client_secret = client_secret
        if client_id is not None:
            self.client_id = client_id
        if token is not None:
            self.token = token

    @property
    def client_secret(self):
        return self.__client_secret
    
    @client_secret.setter
    def client_secret(self, new_value):
        self.__client_secret = new_value

    @property
    def client_id(self):
        return self.__client_id
    
    @client_id.setter
    def client_id(self, new_value):
        self.__client_id = new_value

    def __repr__(self):
        return ("<ApiConfig({0},{1},{2})>".format(self.is_production,
            self.client_secret,
            self.client_id,
            self.token))
