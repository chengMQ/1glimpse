import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_pythondaily():
    '''<a style="color:#000000;" target="_blank" href="http://forum.memect.com/blog/thread-category/py/" title="好东西传送门旗下python干货合集，一日一更，虽然订阅了邮件，但还是想留点存档看看。">好东西传送门-python日报</a>'''
    starttime = time.time()
    my_title = pyld_pythondaily.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6  # 根据内容数量来划分
    iscover = 0
    for day1 in range(3):
        try:
            theday = (
                thisday - datetime.timedelta(days=day1)).strftime("%Y-%m-%d")
            url = 'http://forum.memect.com/blog/thread/py-%s/' % theday
            r = requests.get(url)
            if r.status_code==404:
                continue
            items = [tostring(i,encoding='utf-8').decode('utf-8') for i in fromstring(r.text).xpath('//div[@id="container"]/div[@class]')]
            sums = [re.sub('<img.*?>','',i) for i in items]
            urls = [''] * len(sums)
            titles = [''] * len(sums)
            covers = [''] * len(sums)
            aa = list(zip(covers, titles, urls, sums))

        except Exception as e:
            print('%s  %s' % (title_clean, e))
            aa = [['error'] * 4]
        runtime1 = round(time.time() - starttime, 3)
        print(title_clean, 'finished in %s seconds' % runtime1)
        return [my_title, aa, column, iscover]


pyld_pythondaily()
