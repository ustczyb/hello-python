# coding=utf-8
"""字符串基本操作"""


# 字符串可以认为是一个字符列表，因此字符串也支持列表操作，但是字符串是不可变的，因此字符串不可进行赋值操作
from string import maketrans


def hello():
    s = 'hello world'
    print(s[1])


# 字符串格式化
def test_format():
    name = 'bart'
    word = 'hello'
    value = 3.1415926
    print('name = %s, word = %s, value = %.3f' % (name, word, value))


# 字符串find方法,返回子串所在位置最左端索引，如果没有返回-1
def test_find():
    s = 'hello world'
    sub_str = 'wo'
    print(s.find(sub_str))
    print(s.find('ha'))


# join方法，用于连接一个序列中的所有元素，序列中的元素必须都是string，否则抛出异常
def test_join():
    seq = ['1', '2', '3', '4', '5']
    sp = '+'
    print(sp.join(seq))


# 一些常用的方法
def test_str_method():
    # 大小写转换
    name = 'Bart'
    print(name.upper())
    print(name.lower())

    # 字符串替换
    s = 'helloworld'
    print(s.replace('o', '0'))

    # 字符串分割
    s = '1,2,3,4,5'
    print(s.split(','))

    #去除字符串两端的空格，即java的trim()
    s = '  haha '
    print(s.strip())

    # 字符替换,替换字母表
    s = 'this is an incredible test'
    table = maketrans('cs', 'kz')
    print(s.translate(table))


test_str_method()
