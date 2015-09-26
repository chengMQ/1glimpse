# 1glimpse
http://clericpy.github.io/

---


>注：所有代码只是学习使用，如有侵权，请在issue留言

---

* 2015年9月20日 14:24:33

---

<p style="font-size:18px;"><strong>当前订阅列表：</strong><a title="36氪是一个关注互联网创业的科技博客，旨在帮助互联网创业者实现创业梦。我们相信每个人都可以像来氪星人超人那样强大无比。还行吧，有质有量还有料" href="#36kr-首页" style="color:#000000;">36kr-首页</a> | <a title="36氪是一个关注互联网创业的科技博客，旗下NEXT栏目的宗旨是不错过任何一个新产品。不错，简洁明了信息量大" href="#36kr-NEXT" style="color:#000000;">36kr-NEXT</a> | <a title="分享免费、小巧、实用、有趣、绿色的软件。“我最喜欢的软件”栏目非常有价值，并且不定期更新优秀软件测评与推荐，值得一看。" href="#小众软件（RSS）" style="color:#000000;">小众软件（RSS）</a> | <a title="站长之家(中国站长站)为个人站长与企业网络提供全面的站长资讯、最新最全的源代码程序下载、海量建站素材、强大的搜索优化辅助工具、网络产品设计与运营理念以及一站式网络解决方案。做网站的应该都用过。" href="#站长之家-首页推荐" style="color:#000000;">站长之家-首页推荐</a> | <a title="每日分享妹子图和技术干货，还有供大家中午休息的休闲视频。妹子质量大约在70分以上，技术偏向于移动开发或前端，视频是真好东西，和“开眼”的逼格不一样。" href="#干货集中营" style="color:#000000;">干货集中营</a> | <a title="虎嗅网是一个有视角的、个性化商业资讯与交流平台,核心关注对象是包括公众公司与创业型企业在内的一系列明星公司。部分重要内容在推酷有收录，其他焦点资讯仍值得看一下" href="#虎嗅网-看点" style="color:#000000;">虎嗅网-看点</a> | <a title="很有特色的软件博客!推荐精选实用的软件,并提供相当详细且精美的图文评测，有大量绿色、实用软件及资源下载。评测语气相对客观，是通过软件提升效率的一大门户。" href="#异次元软件世界（RSS）" style="color:#000000;">异次元软件世界（RSS）</a> | <a title="地球上没有新鲜事……Whatever..." href="#煎蛋-首页" style="color:#000000;">煎蛋-首页</a> | <a title="专为学生打造的第一款知识互动百科应用!精选词条百科开拓眼界,话题分类投你所好,脑洞大开思维碰撞,还能随时随地在线学习,用知识传播正能量!对于我这种懒得看百科的来说，看看这个也不错" href="#酱知-每日一蘸" style="color:#000000;">酱知-每日一蘸</a> | <a title="开眼，是豌豆荚出品的一款精品短视频日报应用。在这里，我们会每天为你推荐精心挑选的短视频，它们可能是创意惊人的大牌广告，可能是鲜为人知的美丽风景，也可能是专业的美食攻略或有品位的穿衣指导。挺多“外面”的视频……话说，流量预警啊" href="#开眼-每日精选" style="color:#000000;">开眼-每日精选</a> | <a title="专业提供MP4格式的手机视频下载,电影,电视剧,动漫,综艺,音乐短片，平时下电影的去处" href="#80s-热门电影" style="color:#000000;">80s-热门电影</a> | <a title="视频服务平台,提供视频播放,视频发布,视频搜索,视频分享...对于这个网站，不想多做评论" href="#优酷-热门" style="color:#000000;">优酷-热门</a></p>

---

### 更新日志
```
2015年9月26日 23:48:12 增加移动端页面展示
2015年9月26日 22:26:08 收录煎蛋
2015年9月26日 17:29:58 收录36kr-NEXT
2015年9月25日 00:09:40 最喜欢的推酷因为DDOS被下线了，36kr规则更新
2015年9月21日 21:50:50 给列表页的页首添加锚点链接
2015年9月20日 01:05:37 收录开眼-每日精选
2015年9月19日 22:59:03 收录酱知-每日一蘸
2015年9月15日 00:52:43 收录我一直想看的干货集中营
2015年9月13日 03:26:10 收录36kr
2015年9月12日 21:06:51 收录虎嗅网-看点
2015年9月12日 20:25:31 收录80s-热门电影
2015年9月10日 00:57:09 收录 小众软件（RSS）、 异次元软件世界（RSS）、 推酷-文章、优酷

```


------

### Usage
```
运行main.py即可多线程抓取数据源并存入网页，因为怕流量太大，所以不下载图片以及留下历史存量
rules.py存放的是规则函数，轮子在main里，所以是自动加载所有以pyld_开头的函数名，并自动统计各项参数
rules.py可单独使用，输出是列表形式，现在只是前期试验阶段，注释没有写全
pyld.py是平时测试用的，没有实际意义

```


---


###待完成功能

>赶快把RULE搭配好，尽快多放几个有价值的应用，但是也要考虑到同时打开图片过多的问题。

>准备做个客户端项目采集当日（或某日）的日报，然后按sitename进行过滤，只浏览自己想看的内容，并且客户端要添加 *根据快递号码监视快递进程* 的功能。

>以一个既定轮子为主程序（main.py），以update.py更新rules与重新选择channel。

>借助抽取正文模块或手动抽取实现选中文章来开启一览模式，即所有选中文章在同一页中展示，并给出原始链接。

>更新Python3.5后使用协程代替多线程

>根据多家新闻聚合类网站统计包含权重的资讯信息重要程度计算，尝试“一瞥头条”，话说“一瞥”这名字真难听

>汇总过去的博客、为知笔记，创建“好文存档”栏目，存放过去看过极其难忘的好文章或视频，这名字也真够土的

>暂时没有打算做APP端、邮箱订阅、RSS订阅、数据库存量，虽然都不是太难，还是尽快搞个服务器把详情页抽取放入数据库的好，并支持通过参数选择频道


### 写在前面
>因为早就想做个简易RSS，之后使用了下豌豆荚一览这款APP，感觉想法还不错，内容消费的今天，将详情页采集下来去噪/去广告以后可读性好的不得了，让人想起kindle使用的`readability`那个模块（也是火狐的ireader插件），但是使用过程中感觉还是有不少地方不顺手，所以就尝试继续做这样一个名叫`一瞥`的玩意自用。其实RSS聚合类工具应该不少，但是各种不顺的感觉。

##### 和`一览`不同之处在于：
* 可定制性强一点
* 想在电脑上用啊
* 不用加载不想看的详情页，只展示列表页，详情页自己点开，就不用纠结详情页的渲染问题，并且极为省流量
* 不局限于APP，还是RSS为主

##### 这个所谓的`一瞥`局限之处在于：
* 暂时没打算在服务器上跑，所以不考虑太完善的跨平台
* 只是自己避免忘记编码能力的练习，所以语法和设计上都很粗糙
* 为了兼容和简洁（主要还是省力气……），前端非常难看。。。原生HTML
* 为了省事，所以是以函数驱动的针对每个网站的采集，以后会考虑造轮子+RULE+NOSQL
* 有些APP接口是JSON的，不一定有WEBURL（虽然几乎都有），所以以后考虑准备一个`一览模式`，将详情页放入同一个网页中

##### 将要改进的地方：
* 以后会放到服务器上面，因为不抓详情页，流量会非常少，而放到服务器上的时候要考虑抓取周期
* 用数据库保留历史数据，一方面验证历史数据作为断点；另一方面可以进行历史数据分析。等抓取详情页以后考虑doc2vec算法进行FEED归类
* 考虑到抓详情页还要点开看，可以试试`一览模式`，即汇总当日所有要看的详情页到一个HTML中
* 前端展示考虑下不使用最简单的HTML，展示好看一些
* kivy写个跨平台客户端
* 写个GUI版的，省的打开浏览器麻烦
* 轮子+RULE+数据库

------

### 待录入应用/网址列表：
> √：成功 ×：失败 #：暂时舍弃 -：进行中 

#####sourceName | channel | starturl | status

```
36kr	首页	http://36kr.com/ 	√
80s	电影	http://www.80s.cn/	√
CSDN	APP/首页	暂无	
del.icio.us	待定	https://del.icio.us/	
Feedly	待定	http://feedly.com/	
Flipboard	待定	https://www.flipboard.cn/	
flitto	首页	https://www.flitto.com/content	#
FreeBuf	待定	http://www.freebuf.com/	
GitHub	待定	https://github.com/	
HackNews	首页	https://news.ycombinator.com/	
InfoQ	待定	http://www.infoq.com/cn	
IT之家	首页	http://www.ithome.com/ 	
OSCHINA	Python	http://www.oschina.net/translate/tag/python   	
OSCHINA	首页	http://www.oschina.net/news  	
Python日报	今日	http://py.memect.com/ 	
Reddit	待定	https://www.reddit.com/	
Reeder	待定	http://www.reeder.com.tr/	
Stack Overflow	待定	http://stackoverflow.com/	
Unread	待定	http://supertop.co/unread/	
WooYun	待定	http://drops.wooyun.org/	
Zaker	待定	http://www.myzaker.com/index.html	
伯乐在线	python	http://top.jobbole.com/tag/python/	
博客园	Python	http://www.cnblogs.com/cate/python/  	
大眼仔	首页	http://www.dayanzai.me/ 	
电脑报	网页版	http://www.icpcw.com/Newspaper/Hot 	
电脑报	APP	暂无	
电影天堂	首页	http://www.dytt8.net/ 	
豆瓣一刻	首页或APP	http://moment.douban.com/app/	
干货集中营	首页	http://gank.io	
公众号	根据公众号	http://weixin.sogou.com/	#
果壳	首页	http://www.guokr.com/ 	
果壳精选	APP	暂无	
虎嗅	首页	http://www.huxiu.com/ 	√
极客头条	首页	http://geek.csdn.net/hotest	
脚本之家	Python	http://www.jb51.net/list/list_97_1.htm 	
今日头条	首页	http://toutiao.com/ 	
快递	单号	http://www.kiees.cn/ 	#
绿色下载吧	文章	http://www.xiazaiba.com/news/index.html	
码农网	资讯	http://www.codeceo.com/article/category/news	
蟒周刊	首页	http://weekly.pychina.org/  	
慕课网	课程	http://www.imooc.com/course/list	
慕课网	文章	http://www.imooc.com/article 	
软件小品	首页	http://www.appcheers.com/ 	
深蓝阅读	待定	http://bluereader.org/	
推酷	文章	http://www.tuicool.com/ah/0/0?lang=1 	√
小众软件	RSS	http://www.appinn.com/	√
一点资讯	首页	http://www.yidianzixun.com/ 	
异次元软件	RSS	http://www.iplaysoft.com/ 	√
站长之家	推荐	http://www.chinaz.com/	
知乎日报	首页	http://daily.zhihu.com/ 	
酱知	每日一蘸	http://www.jiangzhi.la/mryz/history_list.html	√
开眼	每日精选	http://www.wandoujia.com/eyepetizer/list.html	√
  
```




-----------

~~~过期笔记（已删除）~~~：

>#### ~~~第零版~~~：
>最简单的以每个入口为函数的不可快速扩展版本。即函数驱动的版本，不支持灵活的用户自定义及在线更新rule。
#### ~~~第一版~~~：
>没有历史数据版本，将只抓特定页数，无法自动翻页并抓全。即规则驱动的版本，主体程序不变，但是比较费时间。
- 从github更新下载RULE（若失败则尝试从本地使用旧规则），从本地设置文件获取下载源（可考虑带GUI多选，先展示当前可用RULE，选中更新RULE）。
- 下载器：根据RULE中下载规则设置，若为空则使用默认（所以要先设置好默认值），包含headers（作为字典，必定包含user-agent）、proxies、GET/POST（POST时注意data变量）、302是否自动跳转、是否登录、token/cookies有效期。考虑线程池大小、进度条
- 解析器：根据RULE选定JSON或Xpath，提取title、description（若没有则抽取正文，可考虑readability，后期第二版再考虑）、cover（考虑是否下载）、url。解析失败考虑是发邮件还是修改github上的报错，尽量在报错位置的断点将错误信息汇集起来。
- 展示层：考虑是用表格还是其他方式，尽量不用第三方，只用原生HTML或HTML5

>#### ~~~第二版~~~：
>依然是网址列表形式，cover依然要，暂时不加载详情页，有历史数据来增量抓取，避免漏抓。
#### ~~~第三版~~~：
>包含内容页展示的版本，考虑用pyqt，开始就设定好是使用离线版本（设置好自动清理旧数据或手动选择清理3天内的）还是用内置浏览器现打开
#### ~~~第四版~~~：
>web端上线，因为是资讯汇总只留标题，不会抢占流量应该不会有法律纠纷，APP端暂时没有必要上线。所以需要一个稳定服务器，在规则里也要写好抓取周期。离线版的可以自定义抓取周期
.