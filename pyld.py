import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_tuicool():
    '''<a style="color:#000000;" target="_blank" href="http://www.tuicool.com/ah" title="推酷网是面向IT人的个性化阅读网站,其背后的推荐引擎通过智能化的分析,向用户推荐感兴趣的科技资讯、产品设计、网络营销、技术文章等内容。它最大的收录价值在于，不但汇聚了当前主流IT资讯类网站的内容，并且在其中进行了精选，省去了浏览冷门知识的时间。">推酷-文章</a>'''
    starttime = time.time()
    my_title = pyld_tuicool.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = thisday.strftime('%m-%d')
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
            # covers = [i[0].replace(
            #     '!middle', '') for i in covers if i else '']
            #.replace('!middle', '')
            covers = list(
                map(lambda x: re.sub('!middle$', '', x[0]) if x else '', covers))
            titles = xpath('//a[@class="article-list-title"]/text()')
            sums = [i.strip()
                    for i in xpath('//div[@class="article_cut"]/text()')]
            ptime = xpath('//div[@class="tip meta-tip"]')
            ptime = ['<div style="font-size:15px;" align="right"><br>%s</div>' % re.sub('\s{2,}', '&nbsp&nbsp&nbsp&nbsp', i.text_content().replace('稍后阅读', '').strip())
                     for i in ptime]
            # print(ptime)
            sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
            aa += list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    aa = [i for i in aa if thisday.strftime('%m-%d') in i[3]]
    return [my_title, aa, column, iscover]
print(pyld_tuicool())
