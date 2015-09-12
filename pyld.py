import requests
import re
import datetime
from lxml.html import fromstring
from pprint import pprint

# 本文件只用来测试时候用的，没有其他价值


thisday = datetime.datetime.today()


def chinaz_pyld():
    '''<a style="color:#000000;" href="http://www.chinaz.com/" title="站长之家(中国站长站)为个人站长与企业网络提供全面的站长资讯、最新最全的源代码程序下载、海量建站素材、强大的搜索优化辅助工具、网络产品设计与运营理念以及一站式网络解决方案。做网站的应该都用过。">站长之家-首页推荐</a>'''
    my_title = chinaz_pyld.__doc__
    column = 6
    iscover = 1
    try:
        r = requests.get('http://www.chinaz.com/')
        items = fromstring(r.content.decode('utf8')).xpath(
            '//div[@class="topicsImgTxtBar aTabMain"]/ul[1]/li')

        items = [i for i in items if i.xpath(
            './div/span[@class="date"]/text()')[0].startswith('09月12日')]
        titles = [i.xpath('./a//h5/text()')[0] for i in items]
        covers = [i.xpath('./a//img/@src')[0] for i in items]
        urls = [i.xpath('./a/@href')[0] for i in items]
        desc = [i.xpath('./a//p/text()')[0] for i in items]

        aa = list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


# huxiu_pyld()
r = requests.get('http://www.chinaz.com/')
items = fromstring(r.content.decode('utf8')).xpath(
    '//div[@class="topicsImgTxtBar aTabMain"]/ul[1]/li')

items = [i for i in items if i.xpath(
    './div/span[@class="date"]/text()')[0].startswith('09月12日')]
titles = [i.xpath('./a//h5/text()')[0] for i in items]
covers = [i.xpath('./a//img/@src')[0] for i in items]
urls = [i.xpath('./a/@href')[0] for i in items]
desc = [i.xpath('./a//p/text()')[0] for i in items]
