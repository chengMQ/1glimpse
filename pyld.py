

import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_36kr_next():
    '''<a style="color:#000000;" target="_blank" href="http://36kr.com/" title="36氪是一个关注互联网创业的科技博客，NEXT，不错过任何一个新产品。不错，简洁明了信息量大">36kr-NEXT</a>'''
    starttime = time.time()
    my_title = pyld_36kr_next.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = requests.get('http://36kr.com/')
        xpath1 = fromstring(r.text).xpath
        items = xpath1('//article')
        newurl = 'http://36kr.com' + \
            xpath1('//a[@id="info_flows_next_link"]/@href')[0]
        r = requests.get(newurl)
        items = items + fromstring(r.text).xpath('//article')
        items = [i for i in items if i.xpath('./div/div/span/time/@datetime')]
        urls = ['http://36kr.com'+i.xpath('./a/@href')[0] for i in items]
        covers = [i.xpath('./a/@data-lazyload')[0].replace('!feature','') for i in items]
        titles = [i.xpath('./div/a/text()')[0] for i in items]
        sums = [i.xpath('./div/div[@class="brief"]/text()')[0] for i in items]
        ptime = ['<div align="right"><br>%s</div>' % re.sub(' \+\d\d\d\d$', '', i.xpath('./div/div/span/time/@datetime')[0])
                 for i in items]
        sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
        aa = list(zip(covers, titles, urls, sums))
        # print('推酷——finished……')
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]

(pyld_36kr_next())


# def pyld_jiandan():
#     '''<a style="color:#000000;" target="_blank" href="http://jandan.net/" title="地球上没有新鲜事……Whatever...">煎蛋-首页</a>'''
#     starttime = time.time()
#     my_title = pyld_jiandan.__doc__
#     column = 5
#     iscover = 0
#     try:
#         r = requests.get('http://baobab.wandoujia.com/api/v1/feed')
#         items = r.json()['dailyList'][0]['videoList']
#         titles = [i['title'] for i in items]
#         covers = [''] * len(titles)
#         urls = [i['rawWebUrl'] for i in items]
#         desc = ['<video height=200 src="{}" controls="controls"><a href="{}">您的浏览器不支持 video 标签</video></a><p>{}</p>'.format(
#             i['playUrl'], i['rawWebUrl'], i['description']) for i in items]

#         aa = list(zip(covers, titles, urls, desc))
#         # print('推酷——finished……')
#     except Exception as e:
#         print('%s  %s'%(re.sub('<.*?>', '', my_title),e))
#         aa = [['error'] * 4]
#     runtime1 = round(time.time() - starttime,3)
#     print(re.sub('<.*?>', '', my_title), 'finished in %s seconds' % runtime1)
#     return [my_title, aa, column, iscover]

# pyld_jiandan()