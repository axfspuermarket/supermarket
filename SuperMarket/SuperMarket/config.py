# Author    :MrDan
# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 10:46
# @Author  : MrDan
# @Email   : xiedan0004@qq.com
# @File    : config.py
# @Software: PyCharm
from lib.alipay.alipay import AliPay


class Alipay_Config:
    AppID = '2016092400584411'
    HostIP = 'http://104.168.203.148/app/'
    P_Key = r'lib/alipay/key/ying_yong_si_yao.txt'
    S_Key = r"lib/alipay/key/zhi_fu_bao_gong_yao.txt"



class SMS:
    YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
    YZX_SMS_PARAMS = {
        "sid": "c725bdc0f520f502a9534129354e8dfd",
        "token": "840d85f451c38f5e38307c779ca99267",
        "appid": "88cffb8d342844f29a4f811e9f4b62bf",
        "templateid": "452946",
        "param": None,
        "mobile": None,
        "uid": "2d92c6132139467b989d087c84a365d8"
    }

    def set_Params(self, param, mobile):
        self.YZX_SMS_PARAMS["param"] = param
        self.YZX_SMS_PARAMS["mobile"] = mobile

class Qiniu:
    #千牛公私钥
    ACCESS_KEY = 'Pe48HxaDYu3ZOygi9sPq3qbn4mwZ7Znb3aUjG5-G'
    SECRET_KEY = 'MVJT6uoqPME_kgJE09jQIABE6RHVhQ3bAczepnxN'
    # 要上传的空间
    BUCKET_NAME = 'mynds'
    # 上传域名
    BUCKET_URL = 'https://ppqvqo62z.bkt.clouddn.com'

#积分
CREDITS_EXPEND = 100


