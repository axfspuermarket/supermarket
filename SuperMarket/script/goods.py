#Author    :MrDan
# -*- coding: utf-8 -*-

import os,sys,random,django,json
# 设置环境

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperMarket.settings")
django.setup()
from user.models import User
from good.models import Goods,Goodtypes

last_names = (
    '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
    '朱秦尤许何吕施张孔曹严华金魏陶姜'
    '戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
    '鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
    '费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
    '乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

first_names = {
    'male': [
        '致远', '俊驰', '雨泽', '烨磊', '晟睿',
        '天佑', '文昊', '修洁', '黎昕', '远航',
        '旭尧', '鸿涛', '伟祺', '荣轩', '越泽',
        '浩宇', '瑾瑜', '皓轩', '浦泽', '绍辉',
        '绍祺', '升荣', '圣杰', '晟睿', '思聪'
    ],
    'female': [
        '沛玲', '欣妍', '佳琦', '雅芙', '雨婷',
        '韵寒', '莉姿', '雨婷', '宁馨', '妙菱',
        '心琪', '雯媛', '诗婧', '露洁', '静琪',
        '雅琳', '灵韵', '清菡', '溶月', '素菲',
        '雨嘉', '雅静', '梦洁', '梦璐', '惠茜'
    ]
}

def random_name():
    last_name = random.choice(last_names)
    sex = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[sex])
    # , sex
    return ''.join([last_name, first_name])


def create_robots(n):
    # 创建初始用户
    for i in range(n):
        # name, sex = random_name()
        name = random_name()
        try:
            User.objects.create(
                phone='%s' % random.randrange(13100000000, 19900000000),
                password = "000000",
                name=name,
                credits = 0
            )
            print('created: %s ' % (name))
        except django.db.utils.IntegrityError:
            pass

def init_goods(path,gt_id):
    # with open(os.path.join(BASE_DIR,'script/data/会员特价.json'),mode="r",encoding="gbk") as f:
    with open(path, mode="r", encoding="gbk") as f:
        data = json.load(f)
    products = data.get('products')[1:]
    for good_dict in products:
        if good_dict.get("type") != "product":
            continue
        # print(good_dict)
        good = Goods()
        good.productimg=good_dict.get("image")
        good.productname = good_dict.get("name")
        good.productlongname = good_dict.get("subtitle")
        good.price = good_dict.get("vip_price_pro").get("price_up").get("price")
        good.marketprice = good_dict.get("vip_price_pro").get("price_down").get("price")
        good.productnum = 20
        good.storenums = 100
        good.specifics =  good_dict.get("sku")
        good.categoryid = gt_id
        good.save()

        # print(product)
        pass

# print(os.path.join(BASE_DIR,'script/data/'))
path = os.path.join(BASE_DIR,'script/data/')
for root,dirs,files in os.walk(path):

    files_list = files

gt_id = 0
for path in [os.path.join(path,file) for file in files_list]:
    try:
        title = os.path.splitext(os.path.basename(path))[0]
        good_type = Goodtypes.objects.get_or_create(typeid= gt_id,typename= title)[0]
        print(good_type)
        init_goods(path,good_type.typeid)
    except Exception as e:
        print(e)
    gt_id+=1



#     print()
# if __name__ == '__main__':
    # create_robots(10)