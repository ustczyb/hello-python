# coding=utf-8
import requests
import chardet


# get请求
def http_get(url):
    r = requests.get(url)
    print(r.content)


# post请求
def post_with_param(url):
    postdata = {'key': 'value'}
    r = requests.post(url, postdata)
    print(r.content)


# 构建get参数的url
def get_with_param(url, getdata):
    r = requests.get(url, params=getdata)
    print(r.url)
    print(r.content)


# 编码
def test_encoding(url):
    r = requests.get(url)
    print('content:' + r.content)
    print('text:' + r.text)
    print('encoding:' + r.encoding)
    r.encoding = 'utf-8'
    print('new text:' + r.text)
    print(chardet.detect(r.content))


# 请求header
def get_with_header(url, header):
    r = requests.get(url, header)
    print(r.content)
    print(r.headers)  # 响应header
    print(r.status_code)
    print(r.headers.get('content-type'))


# cookie处理
def get_with_cookie(url):
    r = requests.get(url)
    for cookie in r.cookies.keys():
        print(cookie + r.cookies.get(cookie))


# 重定向

# 超时

# 代理
def request_with_proxy(url, proxy):
    r = requests.get(url, proxy)


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    data = {'test': 'hello', 'lang': 'python'}
    get_with_param(url, data)