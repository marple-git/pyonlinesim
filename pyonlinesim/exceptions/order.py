from pyonlinesim.exceptions.base import APIError


class ExceededConcurrentOperations(APIError):
    match = 'exceeded_concurrent_operations'
    text = 'Exceeded concurrent operations for your account'


class NoNumber(APIError):
    match = 'no_number'
    text = 'No available numbers for this service'


class TimeIntervalError(APIError):
    match = 'time_interval_error'
    text = 'Delayed forwarding is not available at this moment'


class IntervalConcurrentRequestsError(APIError):
    match = 'interval_concurrent_requests_error'
    text = 'Exceeded concurrent requests. Try later'


class NoDefferForward(APIError):
    match = 'no_forward_for_deffer'
    text = 'No forward for deffer'


class NoNumberForForward(APIError):
    match = 'no_number_for_forward'
    text = 'No available numbers for forwarding'


class ForwardLengthError(APIError):
    match = 'error_length_number_for_forward'
    text = 'Forwarding number has wrong length'


class DuplicateError(APIError):
    match = 'duplicate_operation'
    text = 'Duplicate operation'


class NotEnoughFunds(APIError):
    match = 'warning_low_balance'
    text = 'Not enough funds'
