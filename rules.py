import requests
import re
from lxml.html import fromstring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today().strftime('%Y-%m-%d')

def huxiu_pyld():
    '''虎嗅网-看点'''
    my_title = huxiu_pyld.__doc__
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = datetime.datetime.today().strftime('%Y-%m-%d')
        # 这个if用来决定抓哪天的
        # if datetime.datetime.today().hour < 5:
        #     today1 = '%s-%s' % (datetime.datetime.today().strftime('%m'),
        #                         (datetime.datetime.today().day - 1))
        pagenum = 1
        aa = []
        while 1:
            r = s.get('http://www.huxiu.com/focus/%s.html' % pagenum)
            scode = r.content.decode('utf-8')
            xpath = fromstring(scode).xpath
            dates=[re.sub(' .*','',i) for i in xpath('//time[@class="time"]/text()')]
            if today1 not in dates:
                break
            pagenum += 1
            urls = ['http://www.tuicool.com/articles/' + i for i in xpath('//div[@class="clearfix shadow-box-noshadow mod-info-flow"]//h3/a/@href')]
            covers = xpath('//div[@class="clearfix mod-b mod-art"]/a/img/@src')
            titles = xpath('//div[@class="clearfix shadow-box-noshadow mod-info-flow"]//h3/a/text()')
            desc = [i.strip()
                    for i in xpath('//div[@class="mob-sub"]/text()')]
            ptime = xpath('//div[@class="mob-author"]')
            ptime = ['<div style="font-size:15px;" align="right"><br>%s</div>' % re.sub('\s{2,}', '&nbsp&nbsp&nbsp&nbsp', i.text_content().replace('稍后阅读', '').strip())
                     for i in ptime]
            # print(ptime)
            desc = ['<br>'.join(i) for i in list(zip(desc, ptime))]
            aa += list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(my_title, 'finished')
    return [my_title, aa, column, iscover]



def iplaysoft_pyld():
    '''异次元软件世界（RSS）'''
    my_title = iplaysoft_pyld.__doc__
    column = 6
    iscover = 1
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
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        desc = [''.join(i) for i in list(zip(desc, ptime))]
        result = list(zip(covers, titles, urls, desc))[:6]
    except:
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    print(my_title, 'finished')
    return [my_title, result, column, iscover]


def tuicool_pyld():
    '''推酷-文章'''
    my_title = tuicool_pyld.__doc__
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = datetime.datetime.today().strftime('%m-%d')
        # 这个if用来决定抓哪天的
        # if datetime.datetime.today().hour < 5:
        #     today1 = '%s-%s' % (datetime.datetime.today().strftime('%m'),
        #                         (datetime.datetime.today().day - 1))
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
            ptime = xpath('//div[@class="tip meta-tip"]')
            ptime = ['<div style="font-size:15px;" align="right"><br>%s</div>' % re.sub('\s{2,}', '&nbsp&nbsp&nbsp&nbsp', i.text_content().replace('稍后阅读', '').strip())
                     for i in ptime]
            # print(ptime)
            desc = ['<br>'.join(i) for i in list(zip(desc, ptime))]
            aa += list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(my_title, 'finished')
    return [my_title, aa, column, iscover]


def func_modle():
    '''标题'''
    my_title = func_modle.__doc__
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
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        desc = [''.join(i) for i in list(zip(desc, ptime))]
        result = list(zip(covers, titles, urls, desc))[:6]
    except:
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    print(my_title, 'finished')
    return [my_title, result, column, iscover]

if __name__ == '__main__':
    print('请使用其他模块进行调用')
