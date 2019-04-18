from common import errors
from lib.httplib import render_json
from order.models import Order
from .api import *
# Create your views here.
def get_price(request):
    user = request.user
    coupon_id = request.POST.get("coupon_id",None)
    discount_id = request.POST.get('discount_id',None)
    credit = request.POST.get('credit',None)
    order_no = request.POST.get("order_no",None)
    try:
        order = Order.objects.get(order_no,user_id= user.id)
    except Exception as e:
        print(e)
        raise errors.Order_Error.NOT_THIS_ORDER
    order.order_no
    return True