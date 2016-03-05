#_*_ coding:utf-8 _*_
__author__ = 'kysida'
#导入模块
import urllib2
import re
#import HTMLParser
from HTMLParser import HTMLParser
#定义类
class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if len(attrs) == 0:
                pass
            else:
                for name,value in attrs:
                    if name == 'href':
                        self.links.append(value)

class TextParser(HTMLParser):
    text = False
    def __init__(self):
        HTMLParser.__init__(self)
        self.text_names = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.text = True
    def handle_endtag(self, tag):
        if tag == 'a':
            self.text = False
    def handle_data(self, data):
        if self.text:
           self.text_names.append(data)



#定义函数
def getHtml(url):
    page = urllib2.urlopen(url)
    content = page.read()
    return content
#主程序
if __name__ == "__main__":
    #获取html及内容
    url = 'http://sale.jd.com/act/yufbrhZtjx6JTV.html'
    content = getHtml(url)

    html = MyParser()
    html.feed(content)


    text = TextParser()
    text.feed(content)
#将两个列表并成字典
    url_name = dict(zip(html.links,text.text_names))
    for key in url_name:
        print key + ' ' + url_name[key]

 #   for link_url in html.links:
  #      for text_name in text.text_names:
   #         htmlfile = open('E:\pycs\html.txt','a+')
  #          htmlfile.write(link_url + text_name + '\n')
   #         htmlfile.close()
#    for link_url in html.links:
#       #将html内容写入文件
#        htmlfile = open('E:\pycs\html.txt','a+')
 #       htmlfile.write(link_url + '\n')
 #       htmlfile.close()
#    for text_name in text.text_names:
#        htmlfile2 = open('E:\pycs\html2.txt','a+')
#        htmlfile2.write(text_name + '\n')
#        htmlfile2.close()


    if True:
         print 'OK'

