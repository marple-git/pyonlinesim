from pyonlinesim.exceptions import APIError


class AccountBlocked(APIError):
    pass


class WrongAPIKey(APIError):
    pass


class NoAPIKey(APIError):
    pass


class NoServiceProvided(APIError):
    pass


class RequestNotFound(APIError):
    pass


class APIAccessDisabled(APIError):
    pass


class APIAccessIP(APIError):
    pass


class NotEnoughFunds(APIError):
    pass


def throw_exception(exception_name: str) -> None:
    if exception_name == 'ACCOUNT_BLOCKED':
        raise AccountBlocked('Account is blocked')
    elif exception_name == 'ERROR_WRONG_KEY':
        raise WrongAPIKey('Wrong API key provided')
    elif exception_name == 'ERROR_NO_KEY':
        raise NoAPIKey('No API key provided')
    elif exception_name == 'ERROR_NO_SERVICE':
        raise NoServiceProvided('No service provided')
    elif exception_name == 'REQUEST_NOT_FOUND':
        raise RequestNotFound('Request not found')
    elif exception_name == 'API_ACCESS_DISABLED':
        raise APIAccessDisabled('API access disabled')
    elif exception_name == 'API_ACCESS_IP':
        raise APIAccessIP('Unknown IP address, please configure your IP address')
    elif exception_name == 'WARNING_LOW_BALANCE':
        raise NotEnoughFunds('Not enough funds')
    raise APIError(exception_name)
