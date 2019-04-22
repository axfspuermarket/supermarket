from lib.httplib import render_json
from .logic import get_goods
from .models import *
# Create your views here.
# 分类 GET
def goods(request):
    types_id = request.GET.get("types")
    child_type = request.GET.get("childtype")
    num = request.GET.get("num", 0)
    goods = get_goods(types_id,child_type,num)
    return render_json(goods)


def types(request):
    type_id = request.GET.get("types","all")
    if type_id == "all":
        types = Goodtypes.objects.all()
    else:
        types = Goodtypes.objects.filter(typeid = type_id)
    data = {}
    type_ids = []
    for type_ in types:
        if type_.typeid in type_ids:
            if data.get("child",None) == None:
                data["child"] = []
            data["child"].append(type_.to_dict())
        data[type_.typeid] = type_.to_dict()
        type_ids.append(type_.typeid)
    return render_json(data)