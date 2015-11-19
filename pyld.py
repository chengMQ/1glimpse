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


def pyld_toutiao():
    '''<a style="color:#000000;" target="_blank" href="http://toutiao.io/" title="开发者头条是一个基于程序员阅读和分享的社交平台。在开发者头条，程序员可以分享感兴趣的内容、订阅感兴趣的主题和关注感兴趣的人。收录它只因为它废话非常少。。。">开发者头条</a>'''
    starttime = time.time()
    my_title = pyld_toutiao.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    todaystr = thisday.strftime('%Y-%m-%d')
    column = 6
    iscover = 0
    try:
        r = trequests.get('http://toutiao.io/prev/%s' % todaystr,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2552.0 Safari/537.36'})
        xpath=fromstring(r.text).xpath
        titles = xpath('//h3[@class="title"]/a/text()')
        covers = ['']*len(titles)
        urls = xpath('//h3[@class="title"]/a/@href')
        desc = ['']*len(titles)
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]

print(pyld_toutiao())
