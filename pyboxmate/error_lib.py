"""
Copied most of this from another SDK package. Work smarter, not harder.
"""


class APIError(Exception):
    """ Base class for all errors """


class AuthError(APIError, Exception):
    """ Error thrown when API call doesn't have correct authentication """


class NotFoundError(APIError, Exception):
    """ FOUR-OH-FOUR - End-Point or page not found """


def eva_error(label, r=None):
    if r is not None:
        __handle_http_error(label, r)
    else:
        raise APIError(label)


def __handle_http_error(label, r):
    error_string = '{}: status code {}'.format(label, r.status_code)
    try:
        r_json = r.json()
        if 'error' in r_json:
            error_string += ' with error [{}]'.format(r_json)
    except ValueError:
        pass

    if r.status_code == 401:
        raise AuthError(error_string)
    elif r.status_code == 404:
        raise NotFoundError(error_string)
    else:
        raise APIError(error_string)
