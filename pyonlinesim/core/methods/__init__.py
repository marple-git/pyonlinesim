from enum import Enum


class Methods(Enum):
    GET_BALANCE = 'getBalance'
    GET_NUMBERS_STATS = 'getNumbersStats'
    GET_NUM = 'getNum'
    GET_STATE = 'getState'
    SET_OPERATION_REVISE = 'setOperationRevise'
    SET_OPERATION_OK = 'setOperationOk'


class RentMethods(Enum):
    TARIFFS_RENT = 'tariffsRent'
    GET_RENT_NUM = 'getRentNum'
    GET_RENT_STATE = 'getRentState'
    EXTEND_RENT_STATE = 'extendRentState'
    CLOSE_RENT_NUM = 'closeRentNum'


__all__ = ['Methods', 'RentMethods']