# 1glimpse
http://clericpy.github.io/

---


>注：所有代码只是学习使用，大体思路都来自于深蓝阅读和豌豆荚一览

---

*modified：2015年9月10日 00:57:09*

### 更新日志
```
2015年9月10日 00:48:10 貌似什么都没做



```
  
  
  
 
* 

---

###待完成功能

>赶快把RULE搭配好，尽快多放几个有价值的应用，但是也要考虑到同时打开图片过多的问题

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
> √：成功 ×：失败 #：舍弃 -：进行中
#####sourceName  channel starturl    status
- 36kr    首页  http://36kr.com/    
- 80s 电影  http://www.k5.cc/   
- CSDN    APP首页       
- del.icio.us 待定  https://del.icio.us/    
- Feedly  待定  http://feedly.com/  
- Flipboard   待定  https://www.flipboard.cn/   
- flitto  首页  https://www.flitto.com/content  #
- FreeBuf 待定  http://www.freebuf.com/ 
- GitHub  待定  https://github.com/ 
- HackNews    首页  https://news.ycombinator.com/   
- InfoQ   待定  http://www.infoq.com/cn 
- IT之家    首页  http://www.ithome.com/  
- OSCHINA Python  http://www.oschina.net/translate/tag/python     
- OSCHINA 首页  http://www.oschina.net/news     
- Python日报    今日  http://py.memect.com/   
- Reddit  待定  https://www.reddit.com/ 
- Reeder  待定  http://www.reeder.com.tr/   
- Stack Overflow  待定  http://stackoverflow.com/   
- Unread  待定  http://supertop.co/unread/  
- WooYun  待定  http://drops.wooyun.org/    
- Zaker   待定  http://www.myzaker.com/index.html   
- 伯乐在线    python  http://top.jobbole.com/tag/python/  
- 博客园 Python  http://www.cnblogs.com/cate/python/     
- 大眼仔 首页  http://www.dayanzai.me/     
- 电脑报 网页版 http://www.icpcw.com/Newspaper/Hot  
- 电脑报 APP 暂无  
- 电影天堂    首页  http://www.dytt8.net/   
- 豆瓣一刻    首页或APP  http://moment.douban.com/app/   
- 干货集中营   首页  http://gank.io  
- 公众号 根据公众号   http://weixin.sogou.com/gzh?openid=oIWsFty1hyUMkLf4Q6_fYVeBilnM 
- 果壳  首页  http://www.guokr.com/   
- 果壳精选    APP 暂无  
- 虎嗅  首页  http://www.huxiu.com/   √
- 极客头条    首页  http://geek.csdn.net/hotest 
- 脚本之家    Python  http://www.jb51.net/list/list_97_1.htm  
- 今日头条    首页  http://toutiao.com/     
- 快递  单号  http://www.kiees.cn/    #
- 绿色下载吧   文章  http://www.xiazaiba.com/news/index.html 
- 码农网 资讯  http://www.codeceo.com/article/category/news    
- 蟒周刊 首页  http://weekly.pychina.org/      
- 慕课网 课程  http://www.imooc.com/course/list    
- 慕课网 文章  http://www.imooc.com/article    
- 软件小品    首页  http://www.appcheers.com/   
- 深蓝阅读    待定  http://bluereader.org/  
- 推酷  文章  http://www.tuicool.com/ah/0/0?lang=1    √
- 小众软件    RSS http://www.appinn.com/  √
- 一点资讯    首页  http://www.yidianzixun.com/     
- 异次元软件   RSS http://www.iplaysoft.com/   √
- 站长之家    推荐  http://www.chinaz.com/  
- 知乎日报    首页  http://daily.zhihu.com/     

   


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