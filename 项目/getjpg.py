#coding=utf-8
__author__ = 'kysida'


import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):

    reg = r'src="(http:[\\|\/|\.|\w|=|%]*\.[jpg|png] )" '

    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print imglist
        #urllib.urlretrieve(imgurl,'d:/tu\%s.jpg' % x)
        #x+=1
    return imglist
#html = getHtml("http://tieba.baidu.com/p/2460150866")
html = getHtml(raw_input('Please input url:'))
print getImg(html)
if True:
    print 'success!'