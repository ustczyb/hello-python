# coding=utf-8

import urllib
import urllib2


# get请求
def get(url):
    get_request = urllib2.Request(url)
    get_response = urllib2.urlopen(get_request)
    html = get_response.read()
    print(html)


get('http://www.zhihu.com')


# post请求
def post(url, data):
    data = urllib.urlencode(post_data)
    post_request = urllib2.Request(url, data)
    post_response = urllib2.urlopen(post_request)
    html = post_response.read()
    print(html)


def post_with_header(url, data, header):
    post_request = urllib2.Request(url, data, header)
    post_response = urllib2.urlopen(post_request)
    html = post_response.read()
    print(html)


url = 'https://flights.ch.com/service/CheckTicketDetail'
post_data = {
    'OrderNo': '731-2456028640',
    'CardType': '220602197401040010',
    'CardNo': '0'
}
header = {
    'Host': 'flights.ch.com',
    'Origin': 'https://flights.ch.com',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://flights.ch.com/show-check-ticket'
}

post(url, post_data)
post_with_header(url, post_data, header)
