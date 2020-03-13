# ----- Author ----------------------------------------------------------------

__author__ = 'Michael Montero <mike@resy.com>'

# ----- Public Classes --------------------------------------------------------

class APIError(Exception):
    '''
    Thrown when a non-200 response is returned from the Resy API.
    '''

    def __init__(self, status_code, response):
        self.status_code = status_code
        self.response = response
