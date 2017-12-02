# coding:utf-8
from collections import Counter

from matplotlib import pyplot as plt

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 数据可视化

# 1.创建折线图
def draw_plow_graph():
    years = [1950, 1960, 1970, 1980, 1990]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6]
    # x轴年份，纵轴gdp
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    # 标题
    plt.title("GDP")
    # y轴标记
    plt.ylabel("billion")
    plt.show()


# 2.条形图
def draw_bar_graph():
    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]
    # 条形宽度默认为0.8,加上0.1后包装条在中心
    xs = [i + 0.1 for i, _ in enumerate(movies)]
    # 根据上面设置的宽度和高度画条形图
    plt.bar(xs, num_oscars)

    plt.ylabel("num of Oscar")
    plt.title("my favorite movie")
    # 标记x轴条形中心
    plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
    plt.show()


def draw_complex_bar_graph():
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100]
    decile = lambda grade: grade // 10 * 10
    histogram = Counter(decile(grade) for grade in grades)

    plt.bar([x - 4 for x in histogram.keys()],  # 每个条形向左移动4个单位
            histogram.values(),  # 每个条形高度设置
            8)  # 每个条形宽度设置

    plt.axis([-5, 105, 0, 5])  # x轴取值-5到105，y轴取值0到5

    plt.xticks([10 * i for i in range(11)])  # x轴标记为0到100
    plt.xlabel("十分相")
    plt.ylabel("学生数")
    plt.title("学生考试分布图")
    plt.show()


# draw_bar_graph()
draw_complex_bar_graph()
