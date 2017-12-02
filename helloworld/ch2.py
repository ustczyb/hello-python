# coding=utf-8

# 列表的基本操作
L = ['Adam'.lower(), 95.5, 'Lisa'.lower(), 85, 'Bart'.lower(), 59];
print(L)
print(L[0])  # 索引访问列表
print(L[-1])  # 倒序访问
# print(L[10])    # 越界访问

# 列表插入元素
L = ['Adam', 'Lisa', 'Bart']
L.insert(2, 'Paul')
print(L)

# 移除指定位置元素或队尾元素
L.pop(2)
print(L)
None
# 元组的基本操作
t = (1, 2, 3)
print(t)
print (t[2])
