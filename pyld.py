#!python3
import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
import json
from html import unescape

thisday = datetime.datetime.today()

def pyld_kuaikeji():
    '''<a style="color:#000000;" target="_blank" href="http://news.mydrivers.com/" title="快科技(原驱动之家)新闻中心，每日持续更新报道IT业界、互联网、市场资讯、驱动更新、游戏及产品资讯新闻，是最及时权威的产业新闻及硬件新闻报道平台，快科技(原驱动之家)--全球最新科技资讯专业发布平台。别的不说，确实够长了...">快科技-资讯中心</a>'''
    starttime = time.time()
    my_title = pyld_kuaikeji.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = (str(thisday.year), str(thisday.month), str(thisday.day))
        pagenum = 8
        aa = []
        while 1:
            r = s.get('http://blog.mydrivers.com/getnewnewslistjson.aspx?pageid=%s' %
                      pagenum, headers={'Referer': 'http://news.mydrivers.com/'})
            items = json.loads(re.sub('^NewsList\(|\)$', '', re.sub(r'\\([^"])', '\\1',unescape(r.text))))['Table']
            # print(items)
            items = [i for i in items if today1 ==
                     (i['year'], i['month'], i['day'])]
            if not items:
                print(items,'adfadfadf')
                break
            pagenum += 1
            urls = ['http://news.mydrivers.com' + i['Url'] for i in items]
            covers = ['http://news.mydrivers.com' + i['ListPic']
                      for i in items]
            covers = list(map(lambda x: re.sub(
                '^http://news.mydrivers.com$', '', x), covers))
            titles = [i['Title'] for i in items]
            sums = [i['Content'].strip() for i in items]
            ptime = ['-'.join((i['year'], i['month'], i['day'])) + ' ' +
                     ':'.join((i['hour'], i['minute'], i['second'])) for i in items]
            ptime = [
                '<div style="font-size:15px;" align="right"><br>%s</div>' % i for i in ptime]
            # print(ptime)
            sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
            aa_new = list(zip(covers, titles, urls, sums))

            aa += aa_new

    except Exception as e:
        print(re.sub('^NewsList\(|\)$', '', re.sub(r'', '',unescape( r.text))))
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    aa = [i for i in aa if thisday.strftime('%m-%d') in i[3]]
    return [my_title, aa, column, iscover]

print(pyld_kuaikeji())
