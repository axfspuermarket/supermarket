#Author    :MrDan
# -*- coding: utf-8 -*-
class LogiceError(Exception):
    name = None
    code = None
def gen_logice_error(name,code,msg):
    return type(name,(LogiceError,),{"code":code,"msg":msg})

class Host_Error:
    REQUEST_FORBID = gen_logice_error(name="REQUEST_FORBID", code=4001, msg="Request Frequently!")
    BAD_REQUEST = gen_logice_error(name="BAD_REQUEST", code=4002, msg="Request Error!")

class User_Error:
    NOT_THIS_USER = gen_logice_error(name="NOT_THIS_USER", code=4101, msg="Not This User!")
    NOT_IDENT = gen_logice_error(name="NOT_IDENT", code=4102, msg="Ident Error!")

class Event_Error:
    NOT_THIS_EVENT = gen_logice_error(name="NOT_THIS_EVENT", code=4201, msg="Not This Event!")
    EVENT_NOT_VALID = gen_logice_error(name="EVENT_NOT_VALID", code=4202, msg="Event Not Valid!")
    CONSTRAINT_NOT_ENOUGH = gen_logice_error(name="CONSTRAINT_NOT_ENOUGH", code=4203, msg="Constraint Not Enough!")

class Order_Error:
    NOT_THIS_ORDER = gen_logice_error(name="NOT_THIS_ORDER", code=4301, msg="Not This Order!")

class Other_Error:
    NOT_VERIFIER = gen_logice_error(name="NOT_VERIFIER", code=4901, msg="Verifier Error!")
    FROM_VALID_ERRO = gen_logice_error(name="FROM_VALID_ERROR", code=4902, msg="From Valid Error!")
    MODEL_ERROR = gen_logice_error(name="MODEL_ERROR", code=4903, msg="MODEL ERROR!")
    NO_PERMISSION_ERROR = gen_logice_error(name="NO_PERMISSION", code=4904, msg="Not This Permission!")
    PAY_ERROR = gen_logice_error(name="PAY_ERROR", code=4905, msg="支付失败")