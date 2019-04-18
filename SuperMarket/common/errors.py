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
    NOT_EMPTY_ORDER = gen_logice_error(name="NOT_EMPTY_ORDER", code=4302, msg="Cart Is Empty!")

class Cart_Error:
    NOT_THIS_GOOD = gen_logice_error(name="NOT_THIS_GOOD", code=4401, msg="Not This Good!")
    NOT_THIS_CART = gen_logice_error(name="NOT_THIS_CART", code=4402, msg="Not This Cart!")

class Pay_Error:
    PAY_DEFEATED = gen_logice_error(name="PAY_DEFEATED", code=4401, msg="Pay Defeated!")

class Sms_Error:
    SMS_ERROR = gen_logice_error(name="SMS_ERROR", code=4901, msg="发送失败")
    SMS_VERIFIER_ERROR = gen_logice_error(name="SMS_VERIFIER_ERROR", code=4902, msg="验证失败")
    SMS_TIME_LIMIT = gen_logice_error(name="SMS_TIME_LIMIT", code=4903, msg="时间限制")

class Other_Error:
    NOT_VERIFIER = gen_logice_error(name="NOT_VERIFIER", code=4901, msg="Verifier Error!")
    FROM_VALID_ERRO = gen_logice_error(name="FROM_VALID_ERROR", code=4902, msg="From Valid Error!")
    MODEL_ERROR = gen_logice_error(name="MODEL_ERROR", code=4903, msg="MODEL ERROR!")
    NO_PERMISSION_ERROR = gen_logice_error(name="NO_PERMISSION", code=4904, msg="Not This Permission!")
