# coding=utf-8
"""列表基本操作"""


# 列表的索引
def test_index():
    L = ['Adam'.lower(), 95.5, 'Lisa'.lower(), 85, 'Bart'.lower(), 59];
    print(L)
    print(L[0])  # 索引访问列表,如果越界会抛出异常
    print(L[-1])  # 倒序访问


# 列表的切片 即子序列的选取
def test_slice():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(numbers[1:3])  # 第2到第3个元素
    print(numbers[0:-1])  # 第1到最后一个(不包含)元素
    print(numbers[3:])  # 第4个到结束
    print(numbers[:4])  # 第一个到第4个(不包含)

    print(numbers[1:9:2])  # 以2为步长输出列表中第2到8个元素，即输出序列中索引为1,3,5,7的元素
    print(numbers[::-1])  # 步长为负数，则倒序选取列表中的元素


# 列表的运算
def test_operation():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(l1 + l2)  # 两个列表相加，即将这两个列表连接在一起，需要注意的是列表无法和字符串连接在一起，虽然字符串也是序列
    print(l1 * 4)  # 一个列表和一个数相乘，即复制这个列表若干次


# 元素是否在列表中
def test_in():
    num = [1, 2, 3, 4, 5]
    print(3 in num)  # 列表是否包含元素
    print([1, 2] in num)
    print('i' in 'hello')  # 字符串是否包含字符
    print('ll' in 'hello')  # 字符串是否包含子串


# 列表插入元素
def test_add():
    L = ['Adam', 'Lisa', 'Bart']
    L.insert(2, 'Paul')  # 在列表第三个位置添加元素
    L.append('keal')  # 在列表后添加元素
    print(L)


# 移除指定位置元素或队尾元素
def test_delete():
    L = ['Adam', 'Lisa', 'Bart']
    L.pop(2)  # 移除索引为2的元素，并返回它的值
    del L[2]
    print(L)


# 列表的赋值操作
def test_assign():
    name = list('perl')  # 将一个字符串转换为一个列表
    name[1:] = list('ython')  # 分片赋值，替换
    print(name)

    nums = [1, 5]
    nums[1:1] = [2, 3, 4]  # 通过分片赋值在目标位置插入新元素，同理也可以用作删除
    print(nums)


# 列表的方法
def test_list_func():
    nums = [1, 2, 3, 4, 5, 1]
    nums.reverse()  # reverse方法，转置原列表，无返回值
    print(nums)
    print(nums.count(1))  # count方法，用于统计列表中1出现的次数
    print(nums.index(3))  # index方法，找出该值第一次出现的索引位置
    nums.remove(1)  # remove方法，移除列表中对应值的第一个匹配项
    print(nums)

    a = [1, 2, 3]
    b = [4, 5, 6]
    a.extend(b)  # extend方法，将一个列表追加到当前列表后面，和连接操作不同的是，extend修改了原列表
    print(a)


# 列表排序
def test_sort():
    nums = [1, 3, 4, 7, 6, 2]
    nums.sort()  # 排序，改变原列表
    print(sorted(nums))  # 排序，不改变原列表，返回一个排序后的副本
    print(nums)

    # 自定义比较器排序 cmp参数
    # 反向排序 reverse参数


# 元组是不可变的列表
t = tuple([1,2,3])
print(t)