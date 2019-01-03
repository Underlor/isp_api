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

    def send_request(self, func, params, out='sjson'):
        qs = {
            'out': out,
            'func': func,
            'auth': self.session
        }
        qs.update(params)
        response = self.requester.get(url=self.url, params=qs)
        print(response.text)
        if out == 'xml':
            return fromstring(response.text)
        if out == 'json' or out == 'sjson':
            response = response.json()['doc']
            if 'error' in response:
                raise ApiException(response['error']['msg']['$'])
            return response

    def update_session(self):
        params = {
            'func': 'auth',
            'out': 'sjson',
            'username': self.username,
            'password': self.password,
        }
        response = self.requester.get(url=self.url, params=params).json()['doc']

        if 'error' in response:
            raise ApiException(response['error']['$object'])
        self.session = response['auth']['$']


if __name__ == '__main__':
    s = Session()
