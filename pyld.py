#!python3
import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
import json
from html import unescape
from torequests import tPool
trequests = tPool(30)

thisday = datetime.datetime.today()


def pyld_pythonissues():
    '''<a style="color:#000000;" target="_blank" href="http://clericpy.github.io/" title="收录主流python社区的问答链接。V2EX、SegmentFault等">Python问答</a>'''
    starttime = time.time()
    my_title = pyld_pythonissues.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    todaystr = thisday.strftime('%Y-%m-%d')
    column = 6
    iscover = 0
    def getv2ex():
        try:
            r = trequests.get('http://v2ex.com/go/python')
            xpath=fromstring(r.text).xpath
            urls1 = xpath('//span[@class="item_title"]/a/@href')
            titles1 = xpath('//span[@class="item_title"]/a/text()')
            titles = ['V2ex']*(len(urls1)//5+1)
            covers = ['']*len(titles)
            urls=['http://v2ex.com/go/python']*len(titles)
            times=xpath('//td//span[@class="small fade"]/text()')
            desc = ['<li><a href="%s">%s</a></li>'%('http://v2ex.com'+i[1],i[0]) for i in zip(titles1,urls1,times) if '天前' not in i[2]]
            desc = [''.join(i) for i in list(zip(*(iter(desc),) *len(titles)))]
            aa = list(zip(covers, titles, urls, desc))

        except Exception as e:
            print('%s  %s' % (title_clean, e))
            aa = [['error'] * 4]
            iscover = 0
        return aa
    def getsegmentfault():
        try:
            r = trequests.get('http://segmentfault.com/t/python')
            xpath=fromstring(r.text).xpath
            urls1 = xpath('//h2[@class="title"]/a/@href')
            titles1 = xpath('//h2[@class="title"]/a/text()')
            titles = ['segmentfault']*(len(urls1)//5+1)
            covers = ['']*len(titles)
            urls=['http://segmentfault.com/t/python']*len(titles)
            times=xpath('//div[@class="summary"]/ul[@class="author list-inline"]/li/a[last()]/text()')
            desc = ['<li><a href="%s">%s</a></li>'%('http://segmentfault.com'+i[1],i[0]) for i in zip(titles1,urls1,times) if '天前' not in i[2]]
            desc = [''.join(i) for i in list(zip(*(iter(desc),) *len(titles)))]
            aa = list(zip(covers, titles, urls, desc))

        except Exception as e:
            print('%s  %s' % (title_clean, e))
            aa = [['error'] * 4]
            iscover = 0
        return aa
    aa=getv2ex()
    bb=getsegmentfault()
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa+bb, column, iscover]

print(pyld_pythonissues())
