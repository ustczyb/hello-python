# coding=utf-8
import requests
import bs4

if __name__ == '__main__':
    # 1.http请求
    url = 'http://www.runoob.com/python/python-modules.html'
    html = requests.get(url).content
    # 2.html解析
    bsoup = bs4.BeautifulSoup(html, "html.parser")
    content = bsoup.find(id='content')
    print(content)