# coding=utf-8
# uliontse

NO_TITLE = ['怎么', '好用吗', '什么是', '有什么', '直播：', '视频：', '视频直播']
NO_CONTENT = ['http://', 'var', 'function']


ITEM_POOL = {'AI': ['pytorch','tensorflow','sklearn']}


PARSE_POOL = {
    'id="main_content"': {'who':'ifeng','only':'http://www.ifeng.com/corp/feedback/'},
    'id="Cnt-Main-Article-QQ"': {'who':'tencent_cnt','only':'http://www.qq.com/map/'},
    'id="js_content"': {'who':'weixin','only':'res.wx.qq.com/'},
    'id="articleContent"': {'who':'sina_auto','only':'http://corp.sina.com.cn/chn/sina_job.html'},
    'id="endText"': {'who':'netease','only':'http://help.163.com/'},
    'id="content-text"': {'who':'btime','only':'www.btime.com/aboutus.html'},
    'class="content-bd"': {'who':'yidian','only':'tousu@yidian-inc.com'},
    'class="article-content-wrap"': {'who':'huxiu','only':'static.huxiucdn.com/www/'},
    'class="article-content"': {'who':'geekpark','only':'contact@geekpark.net'},
    'id="contentMain"': {'who':'gmw','only':'http://en.gmw.cn/'},
    'id="news-con"': {'who':'dzwww','only':'http://www.dzwww.com/map/'},
    'class="page_text"': {'who':'youth','only':'http://news.youth.cn/gn/'},
    'id="ctrlfscont"': {'who':'cankaoxiaoxi','only':'http://www.cankaoxiaoxi.com/about/'},
    'id="p-detail"': {'who':'xinhuanet','only':'http://203.192.6.89/xhs/'},
    'id="rwb_zw"': {'who':'people','only':'http://m.people.cn/'},
    'class="left_zw"': {'who':'chinanews','only':'http://hr.chinanews.com/'},
    'id="text"': {'who':'huanqiu','only':'http://mobile.huanqiu.com/#mobileBox'},
    'id="FineDining"': {'who':'zaobao','only':'http://zproperty.zaobao.com.sg'},
    'class="story-body"': {'who':'ftchinese','only':'http://www.ftchinese.com/m/corp/follow.html'},
    'id="chan_newsDetail"': {'who':'china','only':'http://www.china.com/zh_cn/general/about.html'},
    'class="detail"': {'who':'qdaily','only':'http://img.qdaily.com/user/'},
    'class="left_main"': {'who':'ittime','only':'http://www.ittime.com.cn/newslist.shtml'},
    'class="text-title-tip"': {'who':'szonline','only':'http://www.szonline.net/channel/'},
    'class="detail_content"': {'who':'kejixun','only':'http://www.kejixun.com/html/about/aboutus/'},
    'class="news_txt"': {'who':'thepaper','p':'','only':'http://file.thepaper.cn/www/'},#p
    'id="tdcontent"': {'who':'cfi','p':'','only':'http://vip.cfi.cn/'},#p
    'class="article"': {'who': 'sohu', 'div': 'article', 'only': ['www.sohu.com/tag/','http://www.bitecoin.com/关于我们']},#div,only
    'class="article-cont clearfix"': {'who': 'zol', 'space':0,'only': 'news.zol.com.cn/more'},#space
    'class="article-content fontSizeSmall BSHARE_POP"': {'who':'stnn','space': 0,'only':'http://www.stnn.cc/Copyright/ggfw/wzjs.html'},#space
    'class="content all-txt"': {'who': 'guancha', 'space': 1,'only': 'http://www.guancha.cn/about/Copyright.shtml'},#space
    'class="tpk_text clearfix"': {'who': 'takungpao', 'space': 0,'only': 'http://www.takungpao.com/corp/about.html'},#space
    'id="artibody"': {'who': 'sina&&techweb','only': ['http://corp.sina.com.cn/chn/sina_job.html', 'http://www.techweb.com.cn/about.html']},#only
    'class="content"': {'who': 'bjnews&&xiaohulu&&admin5','only': ['http://static.bjnews.com.cn/www/', 'kf@xiaohulu.com','http://www.admin5.com/about/']},#only
    'id="content"': {'who': 'itbear&&southcn','only': ['http://m.itbear.com.cn/', 'http://www.newsgd.com/']},#only
    'articleInfo: {': {'who': 'toutiao','only': 'pstatp.com/toutiao/static/js/'},#id-class
    'article': {'who': 'qihoo','only': 'http://kc.look.360.cn'}#id-class
}

#'id="content clearfix"': {'who': 'itbear&&southcn','div':'article','p':'','space':1,'only': ['http://m.itbear.com.cn/', 'http://www.newsgd.com/']}

UA_POOL = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
]


# link1 = 'http://e.gmw.cn/2017-11/16/content_26806647.htm' #光明网
# link2 = 'http://tech.ifeng.com/a/20171115/44761603_0.shtml' #凤凰网
# link3 = 'http://news.sina.com.cn/o/2017-07-25/doc-ifyihrwk2265523.shtml' #新浪
# link4 = 'http://www.sohu.com/a/203545097_115980' #搜狐
# link5 = 'http://ent.southcn.com/8/2017-11/10/content_178757607.htm' #南方网
# link6 = 'http://www.itbear.com.cn/html/2017-11/244423.html' #ITBEAR
# link7 = 'http://www.dzwww.com/yule/zy/201711/t20171109_16633719.htm' #大众网
# link8 = 'http://tech.163.com/17/1117/13/D3ER9D5E00099504.html' #NetEase
# link9 = 'https://www.toutiao.com/a6489226045797958158/' #toutiao
# link10= 'https://mp.weixin.qq.com/s?__biz=MjM5MDI1ODUyMA==&mid=2672939627&idx=1&sn=14d587f0ccf8bf459406e3de1b189504&' \
#         'chksm=bce2f65c8b957f4a72acbccb0cba549898bb39a582a67265df5b502823e3a87e1fcb8202ca11&mpshare=1&scene=1&' \
#         'srcid=1117YeA0NLTDwKLvHM9kcnmQ&pass_ticket=W%2FN7x5QMxuwmbIEiD9OZsm%2BZ0U181Ugx3dgWlUW1OEJiHDVyRt5%2F8L4tbKWACFja#rd' #weixin
# link11= 'http://sh.qihoo.com/pc/detail?360newsdetail=1&_sign=searchdet&check=36788aab903e770a&sign=360_e39369d1&' \
#         'url=http://www.yulefm.com/news/2017-10-31/145085.html' # 今日爆点(360)
# link12= 'https://item.btime.com/wm/427iajh3vuq8goruch18qschtuo' #北京时间
# link13= 'https://www.huxiu.com/article/222579.html' # 虎嗅网
# link14= 'http://news.zol.com.cn/659/6590172.html' # 中关村在线
# link15= 'http://new.xiaohulu.com/daily/2017/11/171633.shtml' #小葫芦
# link16= 'https://news.qq.com/a/20170823/001218.htm' #腾讯新闻
# link17= 'http://www.bjnews.com.cn/ent/2017/11/21/465153.html' #新京报
