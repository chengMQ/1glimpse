import requests
import re
from lxml.html import fromstring
import datetime
import time
from html import unescape

thisday = datetime.datetime.today()


def youku_pyld():
    '''<a style="color:#000000;" href="http://www.youku.com/" title="视频服务平台,提供视频播放,视频发布,视频搜索,视频分享...对于这个网站，不想多做评论">优酷</a>'''
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
        desc = [''] * len(titles)
        urls = xpath('//div[@class="yk-container"]/div[2]//div[@class="v-title"]/a/@href')
        ptime = ['<div align="right"><br>%s</div>' %i for i in xpath('//div[@class="yk-container"]/div[2]//span[@class="v-time"]/text()')]
        desc = [''.join(i) for i in list(zip(desc, ptime))]
        result = list(zip(covers, titles, urls, desc))[:6]
    except:
        result = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def huxiu_pyld():
    '''<a style="color:#000000;" href="http://www.huxiu.com/focus" title="虎嗅网是一个有视角的、个性化商业资讯与交流平台,核心关注对象是包括公众公司与创业型企业在内的一系列明星公司。部分重要内容在推酷有收录，其他焦点资讯仍值得看一下">虎嗅网-看点</a>'''
    my_title = huxiu_pyld.__doc__
    column = 6
    iscover = 1
    try:
        s = requests.Session()
        today1 = thisday.strftime('%Y-%m-%d')
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
            dates = [re.sub(' .*', '', i)
                     for i in xpath('//time[@class="time"]/text()')]
            if today1 not in dates:
                break
            pagenum += 1
            urls = ['http://www.huxiu.com' + i for i in xpath(
                '//div[@class="clearfix shadow-box-noshadow mod-info-flow"]//h3/a/@href')]
            covers = xpath('//div[@class="clearfix mod-b mod-art"]/a/img/@src')
            titles = xpath(
                '//div[@class="clearfix shadow-box-noshadow mod-info-flow"]//h3/a/text()')
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
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


def appinn_pyld():
    '''<a style="color:#000000;" href="http://www.appinn.com/" title="分享免费、小巧、实用、有趣、绿色的软件。“我最喜欢的软件”栏目非常有价值，并且不定期更新优秀软件测评与推荐，值得一看。">小众软件（RSS）</a>'''
    my_title = appinn_pyld.__doc__
    column = 7
    iscover = 1
    try:
        r = requests.get('http://feeds.appinn.com/appinns/')
        ss = unescape(r.text)
        xpath = fromstring(re.sub('<.*?>', '', ss, 1)).xpath
        titles = xpath('//item/title/text()')
        covers = re.findall('<content:encoded>[\s\S]*?<img.*?src="(.*?)"', ss)
        desc = xpath('//description/text()')[1:]
        urls = re.findall('<link>(.*?)</link>', ss)[1:]
        ptime = ['<div align="right"><br>%s</div>' % datetime.datetime.strptime(i, '%a, %d %b %Y %H:%M:%S GMT').strftime(
            '%Y-%m-%d %H:%M:%S') for i in xpath('//pubdate/text()')[1:]]
        desc = [''.join(i) for i in list(zip(desc, ptime))]
        result = list(zip(covers, titles, urls, desc))[:14]
    except:
        result = [['error'] * 4]
        # print('异次元软件世界——finished……')
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def iplaysoft_pyld():
    '''<a style="color:#000000;" href="http://www.iplaysoft.com/" title="很有特色的软件博客!推荐精选实用的软件,并提供相当详细且精美的图文评测，有大量绿色、实用软件及资源下载。评测语气相对客观，是通过软件提升效率的一大门户。">异次元软件世界（RSS）</a>'''
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
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, result, column, iscover]


def tuicool_pyld():
    '''<a style="color:#000000;" href="http://www.tuicool.com/ah" title="推酷网是面向IT人的个性化阅读网站,其背后的推荐引擎通过智能化的分析,向用户推荐感兴趣的科技资讯、产品设计、网络营销、技术文章等内容。它最大的收录价值在于，不但汇聚了当前主流IT资讯类网站的内容，并且在其中进行了精选，省去了浏览冷门知识的时间。">推酷-文章</a>'''
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
    except:
        aa = [['error'] * 4]
    print(re.sub('<.*?>', '', my_title), 'finished')
    return [my_title, aa, column, iscover]


if __name__ == '__main__':
    print('请使用其他模块进行调用')
