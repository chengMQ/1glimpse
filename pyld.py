import requests
import re
import datetime
from lxml.html import fromstring
thisday = datetime.datetime.today()


def huxiu_pyld():
    '''<a style="color:#000000;" href="http://www.huxiu.com/focus" title="虎嗅网是一个有视角的、个性化商业资讯与交流平台,核心关注对象是包括公众公司与创业型企业在内的一系列明星公司。部分重要内容在推酷有收录，其他焦点资讯仍值得看一下">虎嗅网-看点</a>'''
    my_title = huxiu_pyld.__doc__
    column = 6
    iscover = 1
    try:
        r = requests.get('http://m.huxiu.com/focus/')
        scode = r.content.decode('utf-8')
        items = fromstring(scode).xpath('//ul[@class="ul-list focus-list"]/li')
        today1 = thisday.strftime('%Y-%m-%d')
        items = [i for i in items if i.xpath(
            './p/time/@title')[0].startswith(today1)]

        urls = [('http://www.huxiu.com/' + i.xpath('./a/@href')
                 [0]).replace('//', '/') for i in items]
        covers = [i.xpath('./a//img/@src')[0] for i in items]
        titles = [i.xpath('./a//b/text()')[0] for i in items]
        desc = [i.xpath('./a//p[@class="p2"]/text()')[0].strip()
                for i in items]
        ptime = [i.xpath('./p//time/@title')[0] for i in items]

        desc = ['<br>'.join(i) for i in list(zip(desc, ptime))]
        aa = list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


huxiu_pyld()
