# ----- Author ----------------------------------------------------------------

__author__ = 'Michael Montero <mike@resy.com>'

# ----- Imports ---------------------------------------------------------------

from .error import APIError

import json
import requests
import urllib.parse

# ----- Public Classes --------------------------------------------------------

class RPC(object):
    '''
    Implements remote procedure calls to the Resy API.
    '''

    RESY_API = 'https://api.resy.com/2'

    def __init__(self, api_key):
        self.api_key = api_key


    def get(self, resource, params=None):
        return self.request('get', resource, params)


    def request(self, method, resource, params=None):
        resource = self.RESY_API + resource

        if method == 'get' or method == 'delete':
            if params is not None:
                resource += '?' + urllib.parse.urlencode(params)
        else:
            params = json.dumps(params)

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'ResyAPI api_key="' + self.api_key + '"'
        }

        if method == 'get':
            request = requests.get(resource, headers=headers)
        elif method == 'delete':
            request = requests.delete(resource, headers=headers)
        elif method == 'post':
            request = requests.post(resource, data=params, headers=headers)
        elif method == 'put':
            request = requests.put(resource, data=params, headers=headers)

        if request.status_code != 200:
            raise APIError(request.status_code, request.content.decode())

        return json.loads(request.content.decode())
