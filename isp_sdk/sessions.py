from xml.etree.ElementTree import fromstring
import requests

from .errors import ApiException


class Session:
    session = None

    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.requester = requests.Session()
        self.update_session()

    def __del__(self):
        self.requester.close()

    def _send_request(self, request_data: dict) -> requests.Response:

        response = self.requester.get(url=self.url, params=request_data, verify=False)
        return response

    def send_request(self, func: str, params: dict, out: str = 'sjson'):
        request_data = {
            'out': out,
            'func': func,
            'auth': self.session
        }
        request_data.update(params)

        response = self._send_request(request_data)

        if out == 'xml':
            return fromstring(response.text)

        if out == 'json' or out == 'sjson':
            response = response.json()['doc']
            if 'error' in response:
                raise ApiException(response['error']['msg']['$'])
            return response
        return response

    def update_session(self):
        request_data = {
            'func': 'auth',
            'out': 'sjson',
            'username': self.username,
            'password': self.password,
        }

        response = self._send_request(request_data)
        doc = response.json()['doc']

        if 'error' in response:
            raise ApiException(doc['error']['$object'])

        self.session = doc['auth']['$']
