from ..base import APIError


class UndefinedCountry(APIError):
    match = 'undefined_country'
    text = 'Undefined country'


class UndefinedDays(APIError):
    match = 'undefined_days'
    text = 'Undefined days'
