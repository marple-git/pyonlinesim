from pyonlinesim.exceptions.base import APIError


class OperationsNotFound(APIError):
    match = 'error_no_operations'
    text = 'Operations not found'


class IdentificationRequired(APIError):
    match = 'account_identification_required'
    text = 'Account identification required'
