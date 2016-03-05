#coding=utf-8
__author__ = 'kysida'
#导入模块
import htmllib
import urllib2
import formatter
import string
import os

#定义类
class GetLinks(htmllib.HTMLParser):
    #初始化
    def __init__(self):
        #设置字典格式：links{href:link}
        self.links = {}
        #将传输过来的数据不做处理，格式化为数据流
        f = formatter.NullFormatter()
        htmllib.HTMLParser.__init__(self, f)

    #开始处理标签
    def anchor_bgn(self, href, name, type):
        self.save_bgn()
        self.link = href
    #结束处理标签
    def anchor_end(self):
        #去掉a标签保留a标签并保留内容
        text = string.strip(self.save_end())
        if self.link and text:
            self.links[text] = self.link
 #---------下面算法有点bug------------
#def handle_start(self, href, attr):
#    self.save_bgn()
#    self.link = href
#def handle_starttag(self, tag, attrs):
#    if tag == 'a':
#       self.text =True
#       if len(attrs) == 0:
#          pass
#       else:
#           for name,value in attrs:
#              if name == 'href':
#                  self.links.append(value)
#def handle_end(self):
#     text = string.strip(self.save_end)
#     if self.link and text:
#        self.content[text] = self.link
#     if tag == 'a':
#    self.text = False
#    cont = string.strip()
#def handle_data(self, data):
#    if self.text:
#       self.text_names.append(data)

#主程序
if __name__ == '__main__':
    #删除原有的文件
    try:
        os.remove('bookmenu.txt')
    except WindowsError:
        pass
    #读取html
    #fp = urllib2.urlopen(rawinput("Please input some bookstation link: "))
    fp = urllib2.urlopen("http://sale.jd.com/act/yufbrhZtjx6JTV.html")
    data = fp.read()
    fp.close()
    #实例化
    demo = GetLinks()
    demo.feed(data)
    demo.close()
    #字典遍历
    for href, link in demo.links.items():
        #匹配link以‘http://e.jd.com/’开头的链接
        link_result = link.startswith('http://e.jd.com/')
        #href_result = href.startswith('立即下载')
        #去掉干扰的href
        if link_result == True and href != '立即下载':
            #print 'ok'
            #写入文件
            htmlfile = open('bookmenu.txt','a+')
            htmlfile.write("《"+href+"》"+'-------------->'+link + '\n\n')
            htmlfile.close()
        else:
            continue
    if True:
        print 'The book had been send successfully! '