from .config import ApiConfig
from .http import HttpClient


class Briva:
    """
    Briva object used to do request to Briva API
    """

    def __init__(self, 
            is_production=False,
            client_secret='',
            client_id='',
            token=''):

        self.api_config = ApiConfig(is_production, client_secret, client_id, token)
        self.http_client = HttpClient()

    @property
    def api_config(self):
        return self.__api_config

    @api_config.setter
    def api_config(self, new_value):
        self.__api_config = new_value

    def create(self, parameters=dict()):
        """
        Trigger `/v1/briva` API call to Briva API
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva'

        response_dict, response_object = self.http_client.request(
            'post',
            api_url,
            self.api_config,
            parameters=parameters)

        return response_dict

    def get(self,parameters=dict()):
        """
        Trigger `/v1/briva/status/{institution_code}/{briva_no}/{customer_code}` API call to Briva API
        Capture is only used for pre-authorize transaction only
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva/{institutionCode}/{brivaNo}/{custCode}'.format(**parameters)
        response_dict, response_object = self.http_client.request(
            'get',
            api_url,
            self.api_config)

        return response_dict

    def status(self,parameters=dict()):
        """
        Trigger `/v1/briva/status/{institution_code}/{briva_no}/{customer_code}` API call to Briva API
        Capture is only used for pre-authorize transaction only
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva/status/{institutionCode}/{brivaNo}/{custCode}'.format(**parameters)
        response_dict, response_object = self.http_client.request(
            'get',
            api_url,
            self.api_config)

        return response_dict

    def status_update(self, parameters=dict()):
        """
        Trigger `/v1/briva/status` API call to Briva API
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva/status'

        response_dict, response_object = self.http_client.request(
            'put',
            api_url,
            self.api_config,
            parameters)

        return response_dict

    def update(self, parameters=dict()):
        """
        Trigger `/v1/briva` API call to Briva API
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva'

        response_dict, response_object = self.http_client.request(
            'put',
            api_url,
            self.api_config,
            parameters)

        return response_dict

    def delete(self,parameters=dict()):
        """
        Trigger `/v1/briva` API call to Briva API
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva'

        response_dict, response_object = self.http_client.request(
            'delete',
            api_url,
            self.api_config,
            parameters)

        return response_dict

    def report(self,parameters=dict()):
        """
        Trigger `/v1/briva/report/{institution_code}/{briva_no}/{start_date}/{end_date}` API call to Briva API
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva/report/{institutionCode}/{brivaNo}/{startDate}/{endDate}'.format(**parameters)

        response_dict, response_object = self.http_client.request(
            'get',
            api_url,
            self.api_config)

        return response_dict

    def report_time(self,parameters=dict()):
        """
        Trigger `/v1/briva/report/{institution_code}/{briva_no}/{start_date}/{start_time}/{end_date}/{end_time}` API call to Briva API
        :param parameters: dictionary of Briva API JSON body as parameter, will be converted to JSON
        (more params detail refer to: https://developers.bri.co.id/docs/dokumentasi)

        :return: Dictionary from JSON decoded response
        """
        api_url = self.api_config.get_api_base_url()+'/v1/briva/report_time/{institutionCode}/{brivaNo}/{startDate}/{startTime}/{endDate}/{endTime}'.format(**parameters)

        response_dict, response_object = self.http_client.request(
            'get',
            api_url,
            self.api_config)

        return response_dict
