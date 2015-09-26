import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_jiandan():
    '''<a style="color:#000000;" target="_blank" href="http://jandan.net/" title="地球上没有新鲜事……Whatever...">煎蛋-首页</a>'''
    starttime = time.time()
    my_title = pyld_jiandan.__doc__
    column = 5
    iscover = 1
    try:
        r = requests.get('http://jandan.net/', headers={
                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'})
        scode = r.content.decode('utf-8')
        items = fromstring(scode).xpath('//div[@class="post f list-post"]')
        covers = [i.xpath(
            './div[@class="thumbs_b"]/a/img/@src|./div[@class="thumbs_b"]/a/img/@data-original')[0] for i in items]
        urls = [i.xpath('./div[@class="thumbs_b"]/a/@href')[0] for i in items]
        titles = [i.xpath('./div[@class="indexs"]/h2/a/text()')[0]
                  for i in items]
        sums = [re.sub('<.*?>|\s{4,}','',i).strip() for i in re.findall('<h2>[\s\S]*?</h2>[\s\S]*?<a[\s\S]*?>([\s\S]*?)<a', scode)]
        print(sums)
        aa = list(zip(covers, titles, urls, desc))
        # print('推酷——finished……')
    except Exception as e:
        print('%s  %s' % (re.sub('<.*?>', '', my_title), e))
        aa = [['error'] * 4]
    runtime1 = round(time.time() - starttime, 3)
    print(re.sub('<.*?>', '', my_title), 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]

pyld_jiandan()
