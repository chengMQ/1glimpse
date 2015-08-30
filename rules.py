import requests
import re
from lxml.html import fromstring
import datetime
import time
from html import unescape


def iplaysoft_pyld():
    # 异次元软件世界-RSS-前12个
    my_title = '异次元软件世界（RSS）'
    column = 6
    iscover = 0
    try:
        r = requests.get('http://feed.iplaysoft.com/')
        ss = unescape(r.text)
        xpath = fromstring(re.sub('<.*?>', '', ss, 1)).xpath
        titles = [i.replace('[来自异次元]', '').strip()
                  for i in xpath('//item/title/text()')]
        covers = xpath('//item/description/p[1]/a/img/@src')
        desc = [i.text_content()
                for i in xpath('//item/description/div[1]/p[1]')]
        urls = xpath('//item/description/p[1]/a/@href')
        result = list(zip(covers, titles, urls, desc))[:12]
    except:
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    print(my_title,'finished')
    return [my_title, result, column, iscover]


def tuicool_pyld():
    # 当天的推酷-文章，早上5点以前则将前一天的也算上
    my_title = '推酷（%s）' % datetime.datetime.today().strftime('%Y-%m-%d')
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = datetime.datetime.today().strftime('%m-%d')
        # 这个if用来决定抓哪天的
        if datetime.datetime.today().hour < 5:
            today1 = '%s-%s' % (datetime.datetime.today().strftime('%m'),
                                (datetime.datetime.today().day - 1))
        pagenum = 0
        aa = []
        while 1:
            r = s.get('http://www.tuicool.com/ah/0/%s?lang=1' % pagenum)
            scode = r.text
            xpath = fromstring(scode).xpath
            dates = re.findall(
                '<i class="icon-time icon"></i>(.*?)</span>', scode, flags=re.S)
            date = re.findall('(\d\d-\d\d)\D', ' '.join(dates))
            if today1 not in date:
                break
            pagenum += 1
            pids = xpath('//div[@class="single_fake"]/@data-id')
            urls = ['http://www.tuicool.com/articles/' + i for i in pids]
            covers = [xpath(
                '//div[@data-id="%s"]//div[@class="article_thumb"]/img/@src' % i) for i in pids]
            covers = list(map(lambda x: x[0].replace(
                '!middle', '') if x else 'empty.jpg', covers))
            titles = xpath('//a[@class="article-list-title"]/text()')
            desc = [i.strip()
                    for i in xpath('//div[@class="article_cut"]/text()')]
            aa += list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except:
        aa = [['error'] * 4]
    print(my_title,'finished')
    return [my_title, aa, column, iscover]


def function():
    pass


if __name__ == '__main__':
    print('请使用其他模块进行调用')
