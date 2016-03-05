#coding=utf-8
__author__ = 'kysida'
#导入库
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
        #去掉a标签保留a标签n内容
        text = string.strip(self.save_end())
        if self.link and text:
            self.links[text] = self.link
#主程序
if __name__ == '__main__':
    #删除原有的文件
    try:
        os.remove('E:\pycs\html.txt')
    except WindowsError:
        pass

    fp = urllib2.urlopen("http://sale.jd.com/act/yufbrhZtjx6JTV.html")
    data = fp.read()
    fp.close()

    demo = GetLinks() #实例化
    demo.feed(data) #给HTMLParser喂食
    demo.close()

    for href, link in demo.links.items():
        #匹配link以‘http://e.jd.com/’开头的链接
        link_result = link.startswith('http://e.jd.com/')
      #  href_result = href.startswith('立即下载')
        if link_result == True and href != '立即下载':
            #print 'ok'
            #写入文件
            htmlfile = open('E:\pycs\html.txt','a+')
            htmlfile.write("《"+href+"》"+'   '+link + '\n')
            htmlfile.close()
        else:
            continue
    if True:
        print 'Successful!'