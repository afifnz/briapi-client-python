import re
import requests
import json
import sys
import hmac
import hashlib
import base64
import six

from datetime import datetime, timezone
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError, BackendApplicationClient

from .auth import Auth
from .config import ApiConfig
from .error import APIError, JSONDecodeError


class HttpClient(object):
    """
    Http Client Class that is wrapper to Python's `requests` module
    Used to do API call to BRIApi API urls.
    Capable of doing http :request:
    """
    def __init__(self):
        self.http_client = requests

    def get_token(self, config): 
        auth = Auth(
            is_production=config.is_production,
            client_secret=config.client_secret,
            client_id=config.client_id,
            token=config.token)
        return auth.access_token()

    @property
    def timestamp_iso8601(self):
        return (datetime.now().astimezone(timezone.utc)
                .isoformat(timespec="milliseconds")
                .replace("+00:00", "Z"))

    def build_signature(self, config, token, timestamp, request_url, method, body):
        path = request_url.replace(config.get_api_base_url(), "")
        verb = method.upper()
        if method == 'get':
            body = ''
        #elif method == 'delete':
        #    body = re.sub('"', '', body)
        message = f'path={path}&verb={verb}&token=Bearer {token}&timestamp={timestamp}&body={body}'
        digest = hmac.new(bytes(config.client_secret, 'utf-8'), bytes(message, 'utf-8'), hashlib.sha256).digest()
        signature = base64.b64encode(digest).decode()
        return signature

    def request(self, method, request_url, config, parameters=dict()):
        """
        Perform http request to an url (supposedly BRIApi API url)
        :param method: http method
        :param request_url: target http url
        :param config: ApiConfig class, as configurations object
        :param parameters: dictionary of BRIApi API JSON body as parameter, will be converted to JSON

        :return: tuple of:
        response_dict: Dictionary from JSON decoded response
        response_object: Response object from `requests`
        """

        # allow string of JSON to be used as parameters
        is_parameters_string = isinstance(parameters, six.string_types)
        if is_parameters_string:
            try:
                parameters = json.loads(parameters)
            except Exception as e:
                raise JSONDecodeError('fail to parse `parameters` string as JSON. Use JSON string or Dict as `parameters`. with message: `{0}`'.format(repr(e)))

        payload = json.dumps(parameters) if method != 'get' else parameters
        token = self.get_token(config)
        timestamp = self.timestamp_iso8601
        signature = self.build_signature(config, token, timestamp, request_url, method, payload)
        headers = {
            "BRI-Timestamp": timestamp,
            "BRI-Signature": signature,
            "Authorization": f"Bearer {token}"
        }
        if method != 'get':
            headers["content-type"] = "application/json"

        response_object = self.http_client.request(
            method,
            request_url,
            data=payload if method != 'get' else None,
            params=payload if method == 'get' else None,
            headers=headers,
            allow_redirects=True
        )

        # catch response JSON decode error
        try:
            response_dict = response_object.json()
        except json.decoder.JSONDecodeError as e:
            raise JSONDecodeError('Fail to decode API response as JSON, API response is not JSON: `{0}`. with message: `{1}`'.format(response_object.text,repr(e)))

        # raise API error HTTP status code
        if response_object.status_code >= 300:
            raise APIError(
                message='BRIApi API is returning API error. HTTP status code: `{0}`. '
                'API response: `{1}`'.format(response_object.status_code,response_object.text),
                api_response_dict=response_dict,
                http_status_code=response_object.status_code,
                raw_http_client_data=response_object
            )
        # raise core API error status code
        if 'status_code' in response_dict.keys() and int(response_dict['status_code']) >= 300 and int(response_dict['status_code']) != 407:
            raise APIError(
                'BRIApi API is returning API error. API status code: `{0}`. '
                'API response: `{1}`'.format(response_dict['status_code'],response_object.text),
                api_response_dict=response_dict,
                http_status_code=response_object.status_code,
                raw_http_client_data=response_object
            )

        return response_dict, response_object
