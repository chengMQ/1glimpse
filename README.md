# 1glimpse
http://clericpy.github.io/

---

>注：所有代码只是学习使用，大体思路都来自于深蓝阅读和豌豆荚一览

---

*modified：2015年8月20日 00:29:50*

###待完成功能
>以一个既定轮子为主程序（main.py），以update.py更新rules与重新选择channel。
下一步借助抽取正文模块或手动抽取实现选中文章来开启一览模式，即所有选中文章在同一页中展示，并给出原始链接。


### 写在前面
>因为早就想做个简易RSS，之后使用了下豌豆荚一览这款APP，感觉想法还不错，内容消费的今天，将详情页采集下来去噪/去广告以后可读性好的不得了，让人想起kindle使用的`readability`那个模块（也是火狐的ireader插件），但是使用过程中感觉还是有不少地方不顺手，所以就尝试继续做这样一个名叫`“一瞥”`的玩意自用。其实RSS聚合类工具应该不少，但是各种不顺的感觉。

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
* 绿色下载吧 文章、下载 http://www.xiazaiba.com/ 
* 小众软件 http://www.appinn.com/ √
* 80s电影 http://www.k5.cc/ 
* 电影天堂 http://www.dytt8.net/ 
* 果壳精选 APP
* 慕课网课程 http://www.imooc.com/course/list  、文章 http://www.imooc.com/article 
* 异次元软件 http://www.iplaysoft.com/ √
* 软件小品http://www.appcheers.com/ 
* 豆瓣一刻 http://moment.douban.com/app/ 或APP
* 推酷 http://www.tuicool.com/ah/0/0?lang=1 √
* 虎嗅 http://www.huxiu.com/ √
* 一点资讯 http://www.yidianzixun.com/ 
* OSCHINA http://www.oschina.net/translate/tag/python   http://www.oschina.net/news  
* 蟒周刊 http://weekly.pychina.org/  
* 大眼仔 http://www.dayanzai.me/ 
* Python日报 http://py.memect.com/ 
* 果壳 http://www.guokr.com/ 
* 脚本之家 http://www.jb51.net/list/list_97_1.htm 
* 博客园 http://www.cnblogs.com/cate/python/  
* 电脑报 APP 和 http://www.icpcw.com/Newspaper/Hot 
* IT之家 http://www.ithome.com/ 
* 快递加单号 http://www.kiees.cn/ 
* 今日头条 http://toutiao.com/ 
* 知乎日报  http://daily.zhihu.com/ 


-----------

~~~过期笔记~~~：

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
