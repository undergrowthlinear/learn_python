#coding=utf-8
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/2738151262")

print(html)
