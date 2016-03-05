#_*_ coding:utf-8 _*_
__author__ = 'kysida'
#导入模块
import urllib2
import string
import re
import formatter
import htmllib
from HTMLParser import HTMLParser
#定义类
class MyParser(HTMLParser):

    def __init__(self):
        htmllib.HTMLParser.__init__(self)
        #self.links = []
        #self.text_names = []
        self.content = {}
    def handle_start(self, href, attr):
        self.save_bgn()
        self.link = href
    #def handle_starttag(self, tag, attrs):
     #   if tag == 'a':
     #       self.text =True
     #       if len(attrs) == 0:
      #          pass
     #       else:
     #           for name,value in attrs:
      #              if name == 'href':
      #                  self.links.append(value)
    def handle_end(self):
        text = string.strip(self.save_end)
        if self.link and text:
            self.content[text] = self.link
       # if tag == 'a':
        #    self.text = False
        #cont = string.strip()
    #def handle_data(self, data):
     #   if self.text:
      #     self.text_names.append(data)

#定义函数
def getHtml(url):
    page = urllib2.urlopen(url)
    cont = page.read()
    return cont
#主程序
if __name__ == "__main__":
    #获取html及内容
    url = 'http://sale.jd.com/act/yufbrhZtjx6JTV.html'
    cont = getHtml(url)

    html = MyParser()
    html.feed(cont)
    html.close()

    for h in
   # text = MyParser()
   # text.feed(content)
   # text.close()

#将两个列表并成字典
 #   url_name = dict(zip(text.text_names,html.links))
#    for text.text_names,html.links in url_name.items():
#        print text.text_names + '-->' + html.links
     #   if key.strip() is None:
     #       del dict[key]

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


#    if True:
 #        print 'OK'

