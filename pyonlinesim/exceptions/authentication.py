from .base import APIError


class AccountBlocked(APIError):
    match = 'account_blocked'
    text = 'Your account is blocked'


class WrongAPIKey(APIError):
    match = 'error_wrong_key'
    text = 'Wrong API Key'


class NoAPIKey(APIError):
    match = 'error_no_key'
    text = 'No API Key provided'


class NoServiceProvided(APIError):
    match = 'error_no_service'
    text = 'No service provided'


class RequestNotFound(APIError):
    match = 'request_not_found'
    text = 'Request not found'


class APIAccessDisabled(APIError):
    match = 'api_access_disabled'
    text = 'API access disabled'


class APIAccessIP(APIError):
    match = 'api_access_ip'
    text = 'Allow connections from your IP Address'


class TryAgainLater(APIError):
    match = 'try_again_later'
    text = 'Try again later'


class NoCountry(APIError):
    match = 'no_country'
    text = 'No country provided'
