# coding :utf8

import urllib
from urllib import request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法')
response1 = request.urlopen(url)
print(response1.getcode())
print(response1.read())

print('第二种方法')
req = request.Request(url)
req.add_header('user-agent','Mozilla/5.0')
response2 = request.urlopen(req)
print(response2.getcode())
print(response2.read())

print('第三种方法')
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())

# 输入输出
name=input()
print("hello",name)

