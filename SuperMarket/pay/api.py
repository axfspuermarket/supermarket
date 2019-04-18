# Create your views here.
import os

from lib.httplib import render_json
from .logic import *

# ------------支付宝模块------------



# 支付
def pay(request):
    # 传递参数初始化支付类
    user = request.user
    orderNo = request.POST.get('orderNo')
    re_url = pay_logic(user,orderNo)
    return render_json({'re_url': re_url})


# 异步支付通知url (上线后使用)
def notify(request):
    # fileName = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    #                         'log/%s_notify.txt' % request.method)
    if request.method == 'GET':
        params = request.GET.dict()
    else:
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)
        params = {}
        for k, v in post_data.items():
            params[k] = v[0]
    # with open(fileName, 'a') as fp:
    #     fp.write(str(params))
        return render_json(params)
