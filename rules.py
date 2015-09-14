import requests
import re
from lxml.html import fromstring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def news36kr_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://36kr.com/" title="36氪是一个关注互联网创业的科技博客，旨在帮助互联网创业者实现创业梦。我们相信每个人都可以像来氪星人超人那样强大无比。还行吧，比没有强">36kr-首页</a>'''
    my_title = news36kr_pyld.__doc__
    column = 6
    iscover = 1
    try:
        r = requests.get('http://36kr.com/')
        items = r.json()['posts']
        items = [
            i for i in items if i['published_at'].startswith(thisday.strftime('%Y-%m-%d'))]

        urls = ['http://36kr.com/p/%s.html' % i['id'] for i in items]
        covers = [i['cover'] + '!feature' for i in items]
        titles = [i['title'] for i in items]
        sums = [i['summary'] for i in items]
        ptime = ['<div align="right"><br>%s</div>' % re.sub('\..*', '', i['published_at'].replace('T', ' '))
                 for i in items]
        sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
        aa = list(zip(covers, titles, urls, sums))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


def movie80s_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.80s.cn/" title="专业提供MP4格式的手机视频下载,电影,电视剧,动漫,综艺,音乐短片，平时下电影的去处">80s-热门电影</a>'''
    my_title = movie80s_pyld.__doc__
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
        print(e)
        result = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def youku_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.youku.com/" title="视频服务平台,提供视频播放,视频发布,视频搜索,视频分享...对于这个网站，不想多做评论">优酷-热门</a>'''
    my_title = youku_pyld.__doc__
    column = 7
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
        result = list(zip(covers, titles, urls, sums))[:6]
    except:
        result = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def chinaz_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.chinaz.com/" title="站长之家(中国站长站)为个人站长与企业网络提供全面的站长资讯、最新最全的源代码程序下载、海量建站素材、强大的搜索优化辅助工具、网络产品设计与运营理念以及一站式网络解决方案。做网站的应该都用过。">站长之家-首页推荐</a>'''
    my_title = chinaz_pyld.__doc__
    column = 6
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
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


def gankio_pyld():
    '''<a style="color:#000000;" href="http://gank.io/" title="每日分享妹子图和技术干货，还有供大家中午休息的休闲视频。妹子质量大约在70分以上，技术偏向于移动开发或前端，视频是真好东西，和“开眼”的逼格不一样。">干货集中营</a>'''
    my_title = gankio_pyld.__doc__
    column = 6
    iscover = 0
    try:
        r = requests.get('http://gank.io/')
        scode = re.findall('<div class="outlink">(.*?)/div>', r.text)[0]
        # print(scode)
        items = ['<a href="{}"><img src="{}" width=100% /></a>'.format(i,i) for i in re.findall(
            '<h1.*?<img.*?src="(.*?)".*?</h1>', scode)]
        # print(items)
        scode = re.sub('.*(<img.*?</h1>){1,}', '', scode)
        ss = ['<p><span style="color:#000000;"><strong>%s</strong></span></p>%s' %
              (i[0], i[1])for i in re.findall('<h1.*?>(.*?)</h1>(.*?</ul>)', scode)]
        # print(ss)
        sums = items + ss

        urls = [''] * len(sums)
        titles = [''] * len(sums)
        covers = [''] * len(sums)
        aa = list(zip(covers, titles, urls, sums))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


def huxiu_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.huxiu.com/focus" title="虎嗅网是一个有视角的、个性化商业资讯与交流平台,核心关注对象是包括公众公司与创业型企业在内的一系列明星公司。部分重要内容在推酷有收录，其他焦点资讯仍值得看一下">虎嗅网-看点</a>'''
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
                 [0]).replace('//', '/').replace('http:/', 'http://') for i in items]
        covers = [i.xpath('./a//img/@src')[0] + '!200x300' for i in items]
        titles = [i.xpath('./a//b/text()')[0] for i in items]
        sums = [i.xpath('./a//p[@class="p2"]/text()')[0].strip()
                for i in items]
        ptime = ['<div align="right"><br>%s</div>' %
                 (i.xpath('./p//time/@title')[0]) for i in items]

        sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
        aa = list(zip(covers, titles, urls, sums))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


def appinn_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.appinn.com/" title="分享免费、小巧、实用、有趣、绿色的软件。“我最喜欢的软件”栏目非常有价值，并且不定期更新优秀软件测评与推荐，值得一看。">小众软件（RSS）</a>'''
    my_title = appinn_pyld.__doc__
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
    except:
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def iplaysoft_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.iplaysoft.com/" title="很有特色的软件博客!推荐精选实用的软件,并提供相当详细且精美的图文评测，有大量绿色、实用软件及资源下载。评测语气相对客观，是通过软件提升效率的一大门户。">异次元软件世界（RSS）</a>'''
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
        sums = [i.text_content()
                for i in xpath('//item/description/div[1]/p[1]')]
        urls = xpath('//item/description/p[1]/a/@href')
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        sums = [''.join(i) for i in list(zip(sums, ptime))]
        result = list(zip(covers, titles, urls, sums))[:6]
    except:
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def tuicool_pyld():
    '''<a style="color:#000000;" target="_blank" href="http://www.tuicool.com/ah" title="推酷网是面向IT人的个性化阅读网站,其背后的推荐引擎通过智能化的分析,向用户推荐感兴趣的科技资讯、产品设计、网络营销、技术文章等内容。它最大的收录价值在于，不但汇聚了当前主流IT资讯类网站的内容，并且在其中进行了精选，省去了浏览冷门知识的时间。">推酷-文章</a>'''
    my_title = tuicool_pyld.__doc__
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
            covers = list(map(lambda x: x[0] if x else '', covers))
            titles = xpath('//a[@class="article-list-title"]/text()')
            sums = [i.strip()
                    for i in xpath('//div[@class="article_cut"]/text()')]
            ptime = xpath('//div[@class="tip meta-tip"]')
            ptime = ['<div style="font-size:15px;" align="right"><br>%s</div>' % re.sub('\s{2,}', '&nbsp&nbsp&nbsp&nbsp', i.text_content().replace('稍后阅读', '').strip())
                     for i in ptime]
            # print(ptime)
            sums = ['<br>'.join(i) for i in list(zip(sums, ptime))]
            aa += list(zip(covers, titles, urls, sums))
        # print('推酷——finished……')
    except Exception as e:
        print(e)
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


if __name__ == '__main__':
    print('请使用其他模块进行调用')
