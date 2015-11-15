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


def pyld_juejin():
    '''<a style="color:#000000;" target="_blank" href="http://gold.xitu.io/#/newest" title=" 挖掘最优质的互联网技术。干货还不错，很喜欢看">稀土掘金</a>'''
    starttime = time.time()
    my_title = pyld_juejin.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = trequests.get('https://api.leancloud.cn/1.1/classes/Entry?order=-createdAt&limit=30', headers={
            "X-avoscloud-Application-Id": "mhke0kuv33myn4t4ghuid4oq2hjj12li374hvcif202y5bm6", "x-avoscloud-request-sign": "14ee9964afc7d7c6cb090583e3c6ffa0,1447311991136"})
        items = r.json()['results']
        titles = [i['title'] for i in items]
        covers = [i.get('screenshot',{}).get('url','') for i in items]
        urls = [i['url'] for i in items]
        urlss= [i['originalUrl'] for i in items]
        desc = [i['content'] for i in items]
        def aa(x):
            if len(x)>40:
                return '%s...'%(x[:40])
            return x
        desc = [aa(i) for i in desc]
        desc=['%s<p><a href="%s">查看原文</a></p>'%(i) for i in zip(desc,urlss)]
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]

print(pyld_juejin())
