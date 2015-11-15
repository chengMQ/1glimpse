#!python3
import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
import json
from html import unescape

thisday = datetime.datetime.today()
def pyld_xitu():
    '''<a style="color:#000000;" target="_blank" href="http://www.wandoujia.com/eyepetizer/list.html" title="开眼，是豌豆荚出品的一款精品短视频日报应用。在这里，我们会每天为你推荐精心挑选的短视频，它们可能是创意惊人的大牌广告，可能是鲜为人知的美丽风景，也可能是专业的美食攻略或有品位的穿衣指导。挺多“外面”的视频……话说，流量预警啊">开眼-每日精选</a>'''
    starttime = time.time()
    my_title = pyld_kaiyan.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = trequests.get('http://baobab.wandoujia.com/api/v1/feed')
        items = r.json()['dailyList'][0]['videoList']
        titles = [i['title'] for i in items]
        covers = [i['coverForFeed'] for i in items]
        urls = [i['rawWebUrl'] for i in items]
        desc = ['<p>{}</p>'.format(i['description']) for i in items]
        column = len(items)
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]

print(pyld_36kr_next())
