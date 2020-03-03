# ----- Author ----------------------------------------------------------------

__author__ = 'Michael Montero <mike@resy.com>'

# ----- Imports ---------------------------------------------------------------

from .error import APIError
from .RPC import RPC

# ----- Public Classes --------------------------------------------------------

class API(object):
    '''
    Resy API implementation for Python.
    '''

    def __init__(self, api_key):
        self.api_key = api_key
        self.rpc = RPC(self.api_key)


    def reservation_find(self,
                         x,
                         y,
                         day,
                         num_seats,
                         auth_token=None,
                         time_slot=None,
                         venue_id=None,
                         location_id=None):
        params = {
            'x': x,
            'y': y,
            'day': day,
            'num_seats': num_seats
        }

        if auth_token is not None:
            params['auth_token'] = auth_token

        if time_slot is not None:
            params['time_slot'] = time_slot

        if venue_id is not None:
            params['venue_id'] = venue_id

        if location_id is not None:
            params['location_id'] = location_id

        return self.rpc.get('/reservation/find', params)


    def venues(self, location_id=None):
        params = {'location_id': ''}
        if location_id is not None:
            params['location_id'] = location_id

        return self.rpc.get('/venues', params)
