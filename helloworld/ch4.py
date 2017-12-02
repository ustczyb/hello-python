# coding=utf-8
"""字典基本操作"""


# 字典创建 python中的字典可以理解为java中的map,键可以是任意不可变类型 k in d查找的是键
def dict_demo():
    items = [('name', "bart"), ('age', 42)]
    d = dict(items)
    print(d)
    d.clear()  # 清空字典
    print(d)
    d = dict(name='homer', age=45)
    print(d)
    print(d.get('bart'))  # get如果获取不到键，返回None而不是抛出异常
    d['hello'] = 'world'
    print('hello' in d)  # in返回字典中是否包含对应的键
    print(d.items())  # 返回字典中所有元组
    print(d.keys())  # 返回字典中的键集合
    print(d.values())
    print(d.pop('hello'))  # 移除键值对信息，返回键对应的值
    print(d)
    dd = {'name': 'bart', 'hi': 'haha'}
    d.update(dd)  # 用新字典中的信息更新原字典，若不存在则添加，已存在用新值覆盖旧值
    print(d)


dict_demo()
