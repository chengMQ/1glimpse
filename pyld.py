import requests
import re
import datetime
from lxml.html import fromstring
from pprint import pprint

# 本文件只用来测试时候用的，没有其他价值


thisday = datetime.datetime.today()


def pyld_jiangzhi():
    '''<a style="color:#000000;" href="http://www.jiangzhi.la/mryz/history_list.html" title="专为学生打造的第一款知识互动百科应用!精选词条百科开拓眼界,话题分类投你所好,脑洞大开思维碰撞,还能随时随地在线学习,用知识传播正能量!对于我这种懒得看百科的来说，看看这个也不错">酱知-每日一蘸</a>'''
    my_title = pyld_jiangzhi.__doc__
    column = 2
    iscover = 1
    try:
        r = requests.get(
            'http://www.jiangzhi.la/v1/webservice/query/mryz/history')
        items = r.json()[:2]
        titles = ['第%s期  %s'%(i['seqNum'],i['topicName']) for i in items]
        covers = [i['bannerPic'] for i in items]
        urls = [i['shareUrl'] for i in items]
        desc = ['', '']

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
