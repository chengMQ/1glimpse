import requests
import re
from lxml.html import fromstring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def pyld_jiandan():
    '''<a style="color:#000000;" target="_blank" href="http://jandan.net/" title="地球上没有新鲜事……Whatever...">煎蛋-首页</a>'''
    starttime = time.time()
    my_title = pyld_jiandan.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 1
    try:
        r = requests.get('http://jandan.net/', headers={'Host': 'jandan.net', 'Cookie': '1933948167=58',
                                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'})
        scode = r.content.decode('utf-8')
        items = fromstring(scode).xpath('//div[@class="post f list-post"]')
        covers = [i.xpath(
            './div[@class="thumbs_b"]/a/img/@src|./div[@class="thumbs_b"]/a/img/@data-original')[0] for i in items]
        urls = [i.xpath('./div[@class="thumbs_b"]/a/@href')[0] for i in items]
        titles = [i.xpath('./div[@class="indexs"]/h2/a/text()')[0]
                  for i in items]
        sums = [re.sub('<.*?>|\s{4,}', '', i).strip()
                for i in re.findall('<h2>[\s\S]*?</h2>[\s\S]*?<a[\s\S]*?>([\s\S]*?)<a', scode)]
        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_36kr_next():
    '''<a style="color:#000000;" target="_blank" href="http://www.next.36kr.com/posts" title="36氪是一个关注互联网创业的科技博客，旗下NEXT栏目的宗旨是不错过任何一个新产品。不错，简洁明了信息量大">36kr-NEXT</a>'''
    starttime = time.time()
    my_title = pyld_36kr_next.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 7
    iscover = 0
    try:
        r = requests.get('http://www.next.36kr.com/posts')
        xpath = fromstring(r.text).xpath
        items = xpath('//div/section[2]/ul/li')
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
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_kaiyan():
    '''<a style="color:#000000;" target="_blank" href="http://www.wandoujia.com/eyepetizer/list.html" title="开眼，是豌豆荚出品的一款精品短视频日报应用。在这里，我们会每天为你推荐精心挑选的短视频，它们可能是创意惊人的大牌广告，可能是鲜为人知的美丽风景，也可能是专业的美食攻略或有品位的穿衣指导。挺多“外面”的视频……话说，流量预警啊">开眼-每日精选</a>'''
    starttime = time.time()
    my_title = pyld_kaiyan.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 6
    iscover = 0
    try:
        r = requests.get('http://baobab.wandoujia.com/api/v1/feed')
        items = r.json()['dailyList'][0]['videoList']
        titles = [i['title'] for i in items]
        covers = [''] * len(titles)
        urls = [i['rawWebUrl'] for i in items]
        desc = ['<video height=200 width=100% src="{}" controls="controls"><a href="{}">您的浏览器不支持 video 标签</video></a><p>{}</p>'.format(
            i['playUrl'], i['rawWebUrl'], i['description']) for i in items]
        column = len(titles)
        aa = list(zip(covers, titles, urls, desc))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
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
        aa = list(zip(covers, titles, urls, sums))

    except Exception as e:
        print('%s  %s' % (title_clean, e))
        aa = [['error'] * 4]
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
        result = list(zip(covers, titles, urls, sums))[:22]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        result = [['error'] * 4]
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, result, column, iscover]


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
        result = list(zip(covers, titles, urls, sums))[:]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        result = [['error'] * 4]
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    column = len(titles)
    return [my_title, result, column, iscover]


def pyld_chinaz():
    '''<a style="color:#000000;" target="_blank" href="http://www.chinaz.com/" title="站长之家(中国站长站)为个人站长与企业网络提供全面的站长资讯、最新最全的源代码程序下载、海量建站素材、强大的搜索优化辅助工具、网络产品设计与运营理念以及一站式网络解决方案。做网站的应该都用过。">站长之家-首页推荐</a>'''
    starttime = time.time()
    my_title = pyld_chinaz.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 7
    iscover = 1
    try:
        r = requests.get('http://www.chinaz.com/')
        items = fromstring(r.content.decode('utf8')).xpath(
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
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, aa, column, iscover]


def pyld_gankio():
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
        r = requests.get('http://feeds.appinn.com/appinns/')
        ss = unescape(r.text)
        xpath = fromstring(re.sub('<.*?>', '', ss, 1)).xpath
        titles = xpath('//item/title/text()')
        covers = re.findall('<content:encoded>[\s\S]*?<img.*?src="(.*?)"', ss)
        sums = xpath('//description/text()')[1:]
        urls = re.findall('<link>(.*?)</link>', ss)[1:]
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        sums = [''.join(i) for i in list(zip(sums, ptime))]
        result = list(zip(covers, titles, urls, sums))[:14]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, result, column, iscover]


def pyld_iplaysoft():
    '''<a style="color:#000000;" target="_blank" href="http://www.iplaysoft.com/" title="很有特色的软件博客!推荐精选实用的软件,并提供相当详细且精美的图文评测，有大量绿色、实用软件及资源下载。评测语气相对客观，是通过软件提升效率的一大门户。">异次元软件世界（RSS）</a>'''
    starttime = time.time()
    my_title = pyld_iplaysoft.__doc__
    title_clean = re.sub('<.*?>', '', my_title)
    column = 5
    iscover = 1
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
        result = list(zip(covers, titles, urls, sums))[:10]
    except Exception as e:
        print('%s  %s' % (title_clean, e))
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    runtime1 = round(time.time() - starttime, 3)
    print(title_clean, 'finished in %s seconds' % runtime1)
    return [my_title, result, column, iscover]


def _pyld_tuicool():
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
    return [my_title, aa, column, iscover]


if __name__ == '__main__':
    print('请使用其他模块进行调用')
