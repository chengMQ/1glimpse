#!python3
import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_chinaz():
    '''<a style="color:#000000;" target="_blank" href="http://www.chinaz.com/" title="站长之家(中国站长站)为个人站长与企业网络提供全面的站长资讯、最新最全的源代码程序下载、海量建站素材、强大的搜索优化辅助工具、网络产品设计与运营理念以及一站式网络解决方案。做网站的应该都用过。">站长之家-首页推荐</a>'''
    starttime = time.time()
    my_title = pyld_chinaz.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 7
    iscover = 1
    try:
        r = requests.get('http://www.chinaz.com/')
        items = fromstring(r.content.decode('utf8','ignore')).xpath(
            '//div[@class="topicsImgTxtBar aTabMain"]/ul[1]/li')

        items = [i for i in items if i.xpath(
            './div/span[@class="date"]/text()')[0].startswith(thisday.strftime(r'%myue%dri').replace('yue', '月').replace('ri', '日'))]
        titles = [i.xpath('./a//h5/text()')[0] for i in items]
        covers = [i.xpath('./a//img/@src')[0] for i in items]
        urls = [i.xpath('./a/@href')[0] for i in items]
        sums = [i.xpath('./a//p/text()')[0] for i in items]

        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


print(pyld_chinaz())
