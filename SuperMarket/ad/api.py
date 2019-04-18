from ad.models import MainWheel,MainNav,Mustbuy,Mainshow
from lib.httplib import render_json
# Create your views here.
#首页 GET

def home(request):
    # 取出所有的商品
    data = {}
    mains = Mainshow.objects.all()
    wheels = MainWheel.objects.all()
    navs = MainNav.objects.all()
    buys = Mustbuy.objects.all()
    data["mains"] = [wheel.to_dict() for wheel in wheels]
    data["wheels"] = [main.to_dict() for main in mains]
    data["navs"] = [nav.to_dict() for nav in navs]
    data["buys"] = [buy.to_dict() for buy in buys]
    return render_json(data)