# coding=utf-8
"""基本输入输出"""
print(25)

# python2中如果通过input()输入一个字符串，那么输入的值必须带引号。我们一般使用raw_input，python3中取消了raw_input
# x = input("x:")
# y = input("y:")
# print(x * y)

# python中字符串单引号和双引号没有区别
s = "hello world"
# 以u开头的Unicode字符串,python3中所有的字符串都是unicode
us = u"中文"
print(us)
# 以r开头的为原始字符串，不会对字符串中的反斜线做特殊处理
rs = r"he said:\n"
print(rs)
rs2 = r'let\'s go'
print(rs2)

