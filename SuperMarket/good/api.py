from lib.httplib import render_json
from .logic import get_goods
# Create your views here.
# 分类 GET
def get_good(request):
    cart_id = request.GET.get("cartid")
    child_cid = request.GET.get("childcid")
    num = request.GET.get("num", 0)
    goods = get_goods(cart_id,child_cid,num)
    return render_json(goods)