import requests
import re
from lxml.html import fromstring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_jiandan():
    '''<a style="color:#000000;" target="_blank" href="http://jandan.net/" title="地球上没有新鲜事……Whatever...">煎蛋-首页</a>'''
    starttime = time.time()
    my_title = pyld_jiandan.__doc__
    column = 5
    iscover = 0
    try:
        r = requests.get('http://baobab.wandoujia.com/api/v1/feed')
        items = r.json()['dailyList'][0]['videoList']
        titles = [i['title'] for i in items]
        covers = [''] * len(titles)
        urls = [i['rawWebUrl'] for i in items]
        desc = ['<video height=200 src="{}" controls="controls"><a href="{}">您的浏览器不支持 video 标签</video></a><p>{}</p>'.format(
            i['playUrl'], i['rawWebUrl'], i['description']) for i in items]

        aa = list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print('%s  %s'%(re.sub('<.*?>', '', my_title),e))
        aa = [['error'] * 4]
    runtime1 = round(time.time() - starttime,3)
    print(re.sub('<.*?>', '', my_title), 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]

pyld_jiandan()