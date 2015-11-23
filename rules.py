#!python3
import requests
import re
from lxml.html import fromstring, tostring
import datetime
import time
from html import unescape
# from torequests import tPool
import json

thisday = datetime.datetime.today()
# requests = tPool(50)

def pyld_pythonissues():
    '''<a style="color:#000000;" target="_blank" href="http://clericpy.github.io/" title="收录主流python社区的问答链接。V2EX、SegmentFault等">Python问答</a>'''
    starttime = time.time()
    my_title = pyld_pythonissues.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    todaystr = thisday.strftime('%Y-%m-%d')
    column = 6
    iscover = 0
    def getv2ex():
        try:
            r = requests.get('http://v2ex.com/go/python')
            xpath=fromstring(r.text).xpath
            urls1 = xpath('//span[@class="item_title"]/a/@href')
            titles1 = xpath('//span[@class="item_title"]/a/text()')
            titles = ['V2ex']*(len(urls1)//5+1)
            covers = ['']*len(titles)
            urls=['http://v2ex.com/go/python']*len(titles)
            times=xpath('//td//span[@class="small fade"]/text()')
            desc = ['<li><a href="%s">%s</a></li>'%('http://v2ex.com'+i[1],i[0]) for i in zip(titles1,urls1,times) if '天前' not in i[2]]
            desc = [''.join(i) for i in list(zip(*(iter(desc),) *len(titles)))]
            aa = list(zip(covers, titles, urls, desc))

        except Exception as e:
            print('%s  %s' % (title_clean, e))
            aa = [['error'] * 4]
            iscover = 0
        return aa
    def getsegmentfault():
        try:
            r = requests.get('http://segmentfault.com/t/python')
            xpath=fromstring(r.text).xpath
            urls1 = xpath('//h2[@class="title"]/a/@href')
            titles1 = xpath('//h2[@class="title"]/a/text()')
            titles = ['segmentfault']*(len(urls1)//5+1)
            covers = ['']*len(titles)
            urls=['http://segmentfault.com/t/python']*len(titles)
            times=xpath('//div[@class="summary"]/ul[@class="author list-inline"]/li/a[last()]/text()')
            desc = ['<li><a href="%s">%s</a></li>'%('http://segmentfault.com'+i[1],i[0]) for i in zip(titles1,urls1,times) if '天前' not in i[2]]
            desc = [''.join(i) for i in list(zip(*(iter(desc),) *len(titles)))]
            aa = list(zip(covers, titles, urls, desc))

        except Exception as e:
            print('%s  %s' % (title_clean, e))
            aa = [['error'] * 4]
            iscover = 0
        return aa
    aa=getv2ex()
    bb=getsegmentfault()
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa+bb, column, iscover]



def pyld_toutiao():
    '''<a style="color:#000000;" target="_blank" href="http://toutiao.io/" title="开发者头条是一个基于程序员阅读和分享的社交平台。在开发者头条，程序员可以分享感兴趣的内容、订阅感兴趣的主题和关注感兴趣的人。收录它只因为它废话非常少。。。">开发者头条</a>'''
    starttime = time.time()
    my_title = pyld_toutiao.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    todaystr = thisday.strftime('%Y-%m-%d')
    column = 6
    iscover = 0
    try:
        r = requests.get('http://toutiao.io/prev/%s' % todaystr,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2552.0 Safari/537.36'})
        xpath=fromstring(r.text).xpath
        titles = xpath('//h3[@class="title"]/a/text()')
        covers = ['']*len(titles)
        urls = xpath('//h3[@class="title"]/a/@href')
        desc = [i.strip() for i in xpath('//div[@class="meta"]/text()')]
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]



def pyld_juejin():
    '''<a style="color:#000000;" target="_blank" href="http://gold.xitu.io/#/newest" title=" 挖掘最优质的互联网技术。干货还不错，很喜欢看">稀土掘金</a>'''
    starttime = time.time()
    my_title = pyld_juejin.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    todaystr = thisday.strftime('%Y-%m-%d')
    column = 6
    iscover = 1
    try:
        r = requests.get('https://api.leancloud.cn/1.1/classes/Entry?order=-createdAt&limit=30', headers={
            "X-avoscloud-Application-Id": "mhke0kuv33myn4t4ghuid4oq2hjj12li374hvcif202y5bm6", "x-avoscloud-request-sign": "14ee9964afc7d7c6cb090583e3c6ffa0,1447311991136"})
        items = r.json()['results']
        items = [i for i in items if i.get(
            'createdAt', '').startswith(todaystr)]
        titles = [i['title'] for i in items]
        covers = [i.get('screenshot', {}).get('url', '') for i in items]
        urls = [i['url'] for i in items]
        urlss = [i['originalUrl'] for i in items]
        desc = [i['content'] for i in items]

        def aa(x):
            if len(x) > 40:
                return '%s...' % (x[:40])
            return x
        desc = [aa(i) for i in desc]
        desc = ['%s<p><a href="%s">查看原文</a></p>' %
                (i) for i in zip(desc, urlss)]
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def no_pyld_kuaikeji():
    '''<a style="color:#000000;" target="_blank" href="http://news.mydrivers.com/" title="快科技(原驱动之家)新闻中心，每日持续更新报道IT业界、互联网、市场资讯、驱动更新、游戏及产品资讯新闻，是最及时权威的产业新闻及硬件新闻报道平台，快科技(原驱动之家)--全球最新科技资讯专业发布平台。别的不说，确实够长了...">快科技-资讯中心</a>'''
    starttime = time.time()
    my_title = pyld_kuaikeji.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = (str(thisday.year), str(thisday.month), str(thisday.day))
        pagenum = 1
        aa = []
        while 1:
            r = s.get('http://blog.mydrivers.com/getnewnewslistjson.aspx?pageid=%s' %
                      pagenum, headers={'Referer': 'http://news.mydrivers.com/'})
            items = json.loads(re.sub('^NewsList\(|\)$', '', re.sub(
                r'\\([^"])', '\\1', unescape(r.text))))['Table']
            # print(items)
            items = [i for i in items if today1 ==
                     (i['year'], i['month'], i['day'])]
            if not items:
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
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    aa = [i for i in aa if thisday.strftime('%m-%d') in i[3]]
    return [my_title, aa, column, iscover]


def pyld_pythondaily():
    '''<a style="color:#000000;" target="_blank" href="http://forum.memect.com/blog/thread-category/py/" title="好东西传送门旗下python干货合集，一日一更，虽然订阅了邮件，但还是想留点存档看看。">好东西传送门-python日报</a>'''
    starttime = time.time()
    my_title = pyld_pythondaily.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 7  # 根据内容数量来划分
    iscover = 0
    for day1 in range(3):
        try:
            theday = (
                thisday - datetime.timedelta(days=day1)).strftime("%Y-%m-%d")
            url = 'http://forum.memect.com/blog/thread/py-%s/' % theday
            r = requests.get(url)
            if r.status_code == 404:
                continue
            items = [tostring(i, encoding='utf-8').decode('utf-8')
                     for i in fromstring(r.text).xpath('//div[@id="container"]/div[@class]')]
            sums = [re.sub('<img.*?>', '', i).replace('font-size:14px', 'font-size:20px').replace('font-size:12px', 'font-size:20px').replace(
                'font-size:16px', 'font-size:20px').replace('class="repost"', 'class="repost" style="font-size:18"') for i in items]
            urls = [''] * len(sums)
            titles = [''] * len(sums)
            covers = [''] * len(sums)
            head = [('', fromstring(r.text).xpath('//h1/text()')[0], url, '')]
            aa = head + list(zip(covers, titles, urls, sums))
            break
        except Exception as e:
            print('%s  %s' % (title_clean, e))
            aa = [['error'] * 4]
            iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_jiandan():
    '''<a style="color:#000000;" target="_blank" href="http://jandan.net/" title="地球上没有新鲜事……Whatever...">煎蛋-首页</a>'''
    starttime = time.time()
    my_title = pyld_jiandan.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 0
    try:
        r = requests.get('http://jandan.net/', headers={'Host': 'jandan.net', 'Cookie': '1933948167=58',
                                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'})
        scode = r.content.decode('utf-8')
        items = fromstring(scode).xpath('//div[@class="post f list-post"]')
        items = [i for i in items if 'day' not in i.xpath(
            './div/div[@class="time_s"]/text()')[0]]
        covers = [i.xpath(
            './div[@class="thumbs_b"]/a/img/@src|./div[@class="thumbs_b"]/a/img/@data-original')[0] for i in items]
        urls = [i.xpath('./div[@class="thumbs_b"]/a/@href')[0] for i in items]
        titles = [i.xpath('./div[@class="indexs"]/h2/a/text()')[0]
                  for i in items]
        sums = [i.strip() for i in re.findall('</h2>([\s\S]*?)<a', scode)]
        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_36kr_next():
    '''<a style="color:#000000;" target="_blank" href="http://www.next.36kr.com/posts" title="36氪是一个关注互联网创业的科技博客，旗下NEXT栏目的宗旨是不错过任何一个新产品。不错，简洁明了信息量大">36kr-NEXT</a>'''
    starttime = time.time()
    my_title = pyld_36kr_next.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 10
    iscover = 0
    try:
        r = requests.get('http://www.next.36kr.com/posts')
        xpath = fromstring(r.text).xpath
        items = xpath('//div[@id="content"]/section[1]/ul/li')
        urls = ['http://www.next.36kr.com' +
                i.xpath('./div/div/a[@class="post-url"]/@href')[0] for i in items]
        covers = [''] * len(urls)
        titles = [i.xpath('./div/div/a[@class="post-url"]/text()')[0]
                  for i in items]
        sums = [i.xpath('./div/div[@class="product-url"]/span/text()')[0]
                for i in items]
        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_kaiyan():
    '''<a style="color:#000000;" target="_blank" href="http://www.wandoujia.com/eyepetizer/list.html" title="开眼，是豌豆荚出品的一款精品短视频日报应用。在这里，我们会每天为你推荐精心挑选的短视频，它们可能是创意惊人的大牌广告，可能是鲜为人知的美丽风景，也可能是专业的美食攻略或有品位的穿衣指导。挺多“外面”的视频……话说，流量预警啊">开眼-每日精选</a>'''
    starttime = time.time()
    my_title = pyld_kaiyan.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = requests.get('http://baobab.wandoujia.com/api/v1/feed')
        items = r.json()['dailyList'][0]['videoList']
        titles = [i['title'] for i in items]
        covers = [i['coverForFeed'] for i in items]
        urls = [i['rawWebUrl'] for i in items]
        desc = ['<p>{}</p>'.format(i['description']) for i in items]
        column = len(items)
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_jiangzhi():
    '''<a style="color:#000000;" target="_blank" href="http://www.jiangzhi.la/mryz/history_list.html" title="专为学生打造的第一款知识互动百科应用!精选词条百科开拓眼界,话题分类投你所好,脑洞大开思维碰撞,还能随时随地在线学习,用知识传播正能量!对于我这种懒得看百科的来说，看看这个也不错">酱知-每日一蘸</a>'''
    starttime = time.time()
    my_title = pyld_jiangzhi.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 5
    iscover = 1
    try:
        r = requests.get(
            'http://www.jiangzhi.la/v1/webservice/query/mryz/history')
        items = r.json()[:column]
        titles = ['第%s期  %s' % (i['seqNum'], i['topicName']) for i in items]
        covers = [i['bannerPic'] for i in items]
        urls = [i['shareUrl'] for i in items]
        desc = [''] * column

        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_36kr():
    '''<a style="color:#000000;" target="_blank" href="http://36kr.com/" title="36氪是一个关注互联网创业的科技博客，旨在帮助互联网创业者实现创业梦。我们相信每个人都可以像来氪星人超人那样强大无比。还行吧，有质有量还有料">36kr-首页</a>'''
    starttime = time.time()
    my_title = pyld_36kr.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = requests.get('http://36kr.com/')
        xpath1 = fromstring(r.text).xpath
        items = xpath1('//article')
        newurl = 'http://36kr.com' + \
            xpath1('//a[@id="info_flows_next_link"]/@href')[0]
        r = requests.get(newurl)
        items = items + fromstring(r.text).xpath('//article')
        items = [i for i in items if i.xpath('./div/div/span/time/@datetime')]
        urls = ['http://36kr.com' + i.xpath('./a/@href')[0] for i in items]
        covers = [i.xpath('./a/@data-lazyload')[0] for i in items]
        titles = [i.xpath('./div/a/text()')[0] for i in items]
        sums = [i.xpath('./div/div[@class="brief"]/text()')[0] for i in items]
        ptime = ['<div align="right"><br>%s</div>' % re.sub(' \+\d\d\d\d$', '', i.xpath('./div/div/span/time/@datetime')[0])
                 for i in items]
        sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
        aa = [i for i in list(zip(covers, titles, urls, sums)) if thisday.strftime(
            '%Y-%m-%d') in i[3]]

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_movie80s():
    '''<a style="color:#000000;" target="_blank" href="http://www.80s.cn/" title="专业提供MP4格式的手机视频下载,电影,电视剧,动漫,综艺,音乐短片，平时下电影的去处">80s-热门电影</a>'''
    starttime = time.time()
    my_title = pyld_movie80s.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 11
    iscover = 1
    try:
        r = requests.get('http://www.80s.cn/movie/list/-2015---h', headers={
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
        scode = r.text
        xpath = fromstring(scode).xpath
        titles = xpath('//ul[@class="me1 clearfix"]/li/a/@title')
        covers = xpath('//ul[@class="me1 clearfix"]/li/a/img/@_src')
        sums = xpath(
            '//ul[@class="me1 clearfix"]/li/span[@class="tip"]/text()')
        urls = ['http://www.80s.cn' +
                i for i in xpath('//ul[@class="me1 clearfix"]/li/a/@href')]
        aa = list(zip(covers, titles, urls, sums))[:22]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_youku():
    '''<a style="color:#000000;" target="_blank" href="http://www.youku.com/" title="视频服务平台,提供视频播放,视频发布,视频搜索,视频分享...对于这个网站，不想多做评论">优酷-热门</a>'''
    starttime = time.time()
    my_title = pyld_youku.__doc__
    # column = 7
    title_clean = re.sub('<.*?>', '', my_title)

    iscover = 1
    try:
        r = requests.get('http://www.youku.com/?screen=phone', headers={
            'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})
        scode = r.content.decode('utf-8')
        xpath = fromstring(scode).xpath
        titles = xpath(
            '//div[@class="yk-container"]/div[2]//div[@class="v-title"]/a/text()')
        covers = [re.sub("background-image:url\('|'\);", '', i)
                  for i in xpath('//div[@class="yk-container"]/div[2]//div[@class="v-pic-real"]/@style')]
        sums = [''] * len(titles)
        urls = xpath(
            '//div[@class="yk-container"]/div[2]//div[@class="v-title"]/a/@href')
        ptime = ['<div align="right"><br>%s</div>' %
                 i for i in xpath('//div[@class="yk-container"]/div[2]//span[@class="v-time"]/text()')]
        sums = [''.join(i) for i in list(zip(sums, ptime))]
        aa = list(zip(covers, titles, urls, sums))[:]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    column = len(titles)
    return [my_title, aa, column, iscover]


def pyld_chinaz():
    '''<a style="color:#000000;" target="_blank" href="http://www.chinaz.com/" title="站长之家(中国站长站)为个人站长与企业网络提供全面的站长资讯、最新最全的源代码程序下载、海量建站素材、强大的搜索优化辅助工具、网络产品设计与运营理念以及一站式网络解决方案。做网站的应该都用过。">站长之家-首页推荐</a>'''
    starttime = time.time()
    my_title = pyld_chinaz.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 7
    iscover = 1
    try:
        r = requests.get('http://www.chinaz.com/')
        items = fromstring(r.content.decode('utf8', 'ignore')).xpath(
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


def no_pyld_gankio():
    '''<a style="color:#000000;" target="_blank" href="http://gank.io/" title="每日分享妹子图和技术干货，还有供大家中午休息的休闲视频。妹子质量大约在70分以上，技术偏向于移动开发或前端，视频是真好东西，和“开眼”的逼格不一样。">干货集中营</a>'''
    starttime = time.time()
    my_title = pyld_gankio.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 1  # 根据内容数量来划分
    iscover = 0
    try:
        r = requests.get('http://gank.io/')
        scode = re.findall('<div class="outlink">(.*?)/div>', r.text)[0]
        # print(scode)
        items = ['<a href="{}"><img src="{}" width=100% /></a>'.format(i, i) for i in re.findall(
            '<h1.*?<img.*?src="(.*?)".*?</h1>', scode)]
        # print(items)
        scode = re.sub('.*(<img.*?</h1>){1,}', '', scode)
        ss = ['<p><span style="color:#000000;"><strong>%s</strong></span></p>%s' %
              (i[0], i[1])for i in re.findall('<h1.*?>(.*?)</h1>(.*?</ul>)', scode)]
        # print(ss)
        sums = items + ss
        sums = [re.sub('<ul.*?>', '<ul>', i) for i in sums]

        urls = [''] * len(sums)
        titles = [''] * len(sums)
        covers = [''] * len(sums)
        column = len(sums)
        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_huxiu():
    '''<a style="color:#000000;" target="_blank" href="http://www.huxiu.com/focus" title="虎嗅网是一个有视角的、个性化商业资讯与交流平台,核心关注对象是包括公众公司与创业型企业在内的一系列明星公司。部分重要内容在推酷有收录，其他焦点资讯仍值得看一下">虎嗅网-看点</a>'''
    starttime = time.time()
    my_title = pyld_huxiu.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = requests.get('http://m.huxiu.com/focus/')
        scode = r.content.decode('utf-8')
        items = fromstring(scode).xpath(
            '//ul[@class="ul-list focus-list"]/li[not(@class)]')
        today1 = thisday.strftime('%Y-%m-%d')
        items = [i for i in items if i.xpath(
            './p/time/@title')[0].startswith(today1)]

        urls = [('http://www.huxiu.com/' + i.xpath('./a/@href')
                 [0]).replace('//', '/').replace('http:/', 'http://') for i in items]
        covers = [i.xpath('./a//img/@src')[0] + '!200x300' for i in items]
        titles = [i.xpath('./a//b/text()')[0] for i in items]
        sums = [i.xpath('./a//p[@class="p2"]/text()')[0].strip()
                for i in items]
        ptime = ['<div align="right"><br>%s</div>' %
                 (i.xpath('./p//time/@title')[0]) for i in items]

        sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_appinn():
    '''<a style="color:#000000;" target="_blank" href="http://www.appinn.com/" title="分享免费、小巧、实用、有趣、绿色的软件。“我最喜欢的软件”栏目非常有价值，并且不定期更新优秀软件测评与推荐，值得一看。">小众软件（RSS）</a>'''
    starttime = time.time()
    my_title = pyld_appinn.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 7
    iscover = 1
    try:
        r = requests.get('http://feeds.appinn.com/appinns/', timeout=10)
        ss = unescape(r.text)
        xpath = fromstring(re.sub('<.*?>', '', ss, 1)).xpath
        titles = xpath('//item/title/text()')
        covers = re.findall('<content:encoded>[\s\S]*?<img.*?src="(.*?)"', ss)
        sums = xpath('//description/text()')[1:]
        urls = re.findall('<link>(.*?)</link>', ss)[1:]
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        sums = [''.join(i) for i in list(zip(sums, ptime))]
        aa = [i for i in list(zip(covers, titles, urls, sums)) if thisday.strftime(
            '%Y-%m-%d') in i[3]]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
        # print('异次元软件世界——finished……')
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_iplaysoft():
    '''<a style="color:#000000;" target="_blank" href="http://www.iplaysoft.com/" title="很有特色的软件博客!推荐精选实用的软件,并提供相当详细且精美的图文评测，有大量绿色、实用软件及资源下载。评测语气相对客观，是通过软件提升效率的一大门户。">异次元软件世界（RSS）</a>'''
    starttime = time.time()
    my_title = pyld_iplaysoft.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 5
    iscover = 0
    try:
        r = requests.get('http://feed.iplaysoft.com/')
        ss = unescape(r.text)
        xpath = fromstring(re.sub('<.*?>', '', ss, 1)).xpath
        titles = [i.replace('[来自异次元]', '').strip()
                  for i in xpath('//item/title/text()')]
        covers = xpath('//item/description/p[1]/a/img/@src')
        sums = [i.text_content()
                for i in xpath('//item/description/div[1]/p[1]')]
        urls = xpath('//item/description/p[1]/a/@href')
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        sums = [''.join(i) for i in list(zip(sums, ptime))]
        aa = list(zip(covers, titles, urls, sums))
        aa = [i for i in aa if thisday.strftime("%Y-%m-%d") in i[3]]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
        iscover = 0
        # print('异次元软件世界——finished……')
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_tuicool():
    '''<a style="color:#000000;" target="_blank" href="http://www.tuicool.com/ah" title="推酷网是面向IT人的个性化阅读网站,其背后的推荐引擎通过智能化的分析,向用户推荐感兴趣的科技资讯、产品设计、网络营销、技术文章等内容。它最大的收录价值在于，不但汇聚了当前主流IT资讯类网站的内容，并且在其中进行了精选，省去了浏览冷门知识的时间。">推酷-文章</a>'''
    starttime = time.time()
    my_title = pyld_tuicool.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        today1 = thisday.strftime('%m-%d')
        # 这个if用来决定抓哪天的
        # if datetime.datetime.today().hour < 5:
        #     today1 = '%s-%s' % (datetime.datetime.today().strftime('%m'),
        #                         (datetime.datetime.today().day - 1))
        pagenum = 0
        aa = []
        while 1:
            r = requests.get(
                'http://www.tuicool.com/ah/0/%s?lang=1' % pagenum)
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
        iscover = 0
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    aa = [i for i in aa if thisday.strftime('%m-%d') in i[3]]
    return [my_title, aa, column, iscover]


if __name__ == '__main__':
    print('请使用其他模块进行调用')
