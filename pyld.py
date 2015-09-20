import requests
import re
import datetime
from lxml.html import fromstring
from pprint import pprint

# 本文件只用来测试时候用的，没有其他价值


thisday = datetime.datetime.today()


def pyld_kaiyan():
    '''<a style="color:#000000;" href="http://www.wandoujia.com/eyepetizer/list.html" title="开眼，是豌豆荚出品的一款精品短视频日报应用。在这里，我们会每天为你推荐精心挑选的短视频，它们可能是创意惊人的大牌广告，可能是鲜为人知的美丽风景，也可能是专业的美食攻略或有品位的穿衣指导。挺多外面的…">开眼-每日精选</a>'''
    my_title = pyld_kaiyan.__doc__
    column = 5
    iscover = 0
    try:
        r = requests.get('http://baobab.wandoujia.com/api/v1/feed')
        items = r.json()['dailyList'][0]['videoList']
        titles = [i['title'] for i in items]
        covers = [''] * len(titles)
        urls = [i['rawWebUrl'] for i in items]
        desc = ['<video src="%s" controls="controls">您的浏览器不支持 video 标签</video>' %
                i['playUrl'] for i in items]

        aa = list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]
