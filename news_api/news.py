# coding=utf-8
# author:uliontse
'''
pymysql_conn = pymysql.connect(host='xxx.xx.xx.xx',
                               port=3306,
                               user='xxxx',
                               password='xxxx',
                               database='xxxx',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

'''


import re
import time
import datetime
import random
import pymysql
import requests
import jieba.analyse
from snownlp import SnowNLP
from html import unescape
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from true_encoding.debug import debug
from .news_config import *



class BaiduNews:
    def __init__(self,pymysql_conn=None,tableName='News'):
        self.host = 'http://news.baidu.com/ns?'
        self.tm = time.time()
        self.tm0 = int(self.tm * 1000)
        self.tm1 = int(self.tm)
        self.headers = {
            'Host': 'news.baidu.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://news.baidu.com/ns?ct=1&rn=20&ie=utf-8&bs=intitle%3A%28%E9%99%8C%E9%99%8C%29&rsv_bp=1'
                       '&sr=0&cl=2&f=8&prevct=no&tn=news&word=%E9%99%8C%E9%99%8C',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cookie': 'BAIDUID=9C7D1834BF0ADA92C4F080B41C5E873E:FG=1; PSTM={0}; BIDUPSID=BE2B0CF40FCC2740442B2882F395DD5C; '
                      'LOCALGX=%u5317%u4EAC%7C%30%7C%u5317%u4EAC%7C%30; Hm_lvt_e9e114d958ea263de46e080563e254c4={1},{2}; '
                      'Hm_lpvt_e9e114d958ea263de46e080563e254c4={3}; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; '
                      'BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; WWW_ST={4}; BDRCVFR[uLXjBGr0i56]=mbxnW11j9Dfmh7GuZR8mvqV; '
                      'BD_CK_SAM=1; PSINO=1; BDSVRTM=143; H_PS_PSSID='.format(self.tm1 - 82207, self.tm1 - 81353,
                                                                              self.tm1 - 798, self.tm1 - 798, self.tm0)
        }
        self.web = '<!DOCTYPE HTML><html><head><title></title></head><body> </body></html>'
        if pymysql_conn:
            self.tableName = tableName
            self.conn = pymysql_conn
            self.cur = self.conn.cursor()
            self.create_sql = '''
                                CREATE TABLE IF NOT EXISTS {}
                                    (
                                          title VARCHAR(64) NOT NULL PRIMARY KEY
                                        , crawlTime INT(10) NOT NULL
                                        , keyword VARCHAR(16) NOT NULL
                                        , field VARCHAR(16) NOT NULL 
                                        , length INT(8) NOT NULL
                                        , publish VARCHAR(32) NOT NULL
                                        , pubDate VARCHAR(32) NOT NULL
                                        , word_TF VARCHAR(64) NULL
                                        , word_RANK VARCHAR(64) NULL
                                        , emotion DECIMAL(5,2) NULL
                                        , image VARCHAR(256) NULL
                                        , video VARCHAR(128) NULL
                                        , link VARCHAR(256) NOT NULL
                                        , content TEXT NULL
                                    );'''.format(self.tableName)
            self.cur.execute(self.create_sql)



    def transTime(self, tm):
        pool = {'日': 0, '小时': 3600, '分钟': 60, '秒': 1}
        for X in pool.keys():
            if ((X in tm) and (X != '日')):
                patt = re.compile('(.*?)' + X)
                num = int(re.findall(patt, tm)[0])
                stmp = int(time.time()) - num * pool[X]
                see_time = datetime.datetime.fromtimestamp(stmp).strftime("%Y-%m-%d %H:%M:%S")
                return see_time
            if ((X in tm) and (X == '日')):
                see_time = tm.replace('年', '-').replace('月', '-').replace(X, '')
                return see_time + ':00'

    def get_baidu(self, keyword, page=0):
        if page == 0:
            # 'ct'=0: TimeOrder, 'ct'=1: FocusOrder; 'tn'='news' or 'newstitle'.
            param = {'ct': 0, 'rn': 20, 'ie': 'utf-8', 'cl': 2, 'tn': 'newstitle', 'word': keyword, 'bs': keyword,
                     'rsv_bp': 1, 'sr': 0, 'f': 8, 'prevct': 'no'}
        else:
            pageN = 20 * page
            param = {'ct': 0, 'rn': 20, 'ie': 'utf-8', 'cl': 2, 'tn': 'newstitle', 'word': 'intitle:(' + keyword + ')',
                     'bt': 0, 'et': 0, 'pn': pageN}
        self.headers.update({'User-Agent': random.choice(UA_POOL)})
        self.tm = time.time()
        res = requests.get(self.host, params=urlencode(param), headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')

        # get `title`,`link`.
        data = soup.find_all('h3', {'class': 'c-title'})
        tt_pool, lk_pool = [], []
        for dt in data:
            tt_pool.append(dt.find_all('a')[0].get_text().strip())
            lk_pool.append(dt.find_all('a')[0].attrs['href'])

        # get `publish`,`pubDate`.
        item = soup.find_all('div', {'class': 'c-title-author'})
        org_publish, org_date = [], []
        for it in item:
            org = it.get_text().split('\xa0\xa0')  # space
            org_publish.append(org[0])
            org_date.append(self.transTime(org[1]))
        return {'publish': org_publish, 'pubDate': org_date, 'title': tt_pool, 'link': lk_pool}


    def judgeOnly(self, only, html):
        if isinstance(only, list):
            for x in only:
                if x in html: return True
            return False
        if only in html: return True

    def getSentiment(self, text):
        try:
            s = SnowNLP(text)
            return round(s.sentiments,2)
        except:
            return None


    def get_content(self, link):
        try: #solve zero index in baidu && network error.
            global res
            res = requests.get(link, headers={'User-Agent': random.choice(UA_POOL)},timeout=5)
            res.encoding = debug(res)
            html = res.text
        except:
            html = self.web
        soup = BeautifulSoup(html, 'lxml')

        for parser in PARSE_POOL.keys():
            if (parser == 'articleInfo: {' and self.judgeOnly(PARSE_POOL[parser]['only'], html)):
                pattern = re.compile("content: '(.*?)'")
                contents = re.findall(pattern, html)[0]
                para = BeautifulSoup(unescape(contents), 'lxml').get_text()
                return {
                    'parser': PARSE_POOL[parser]['who'],
                    'encoding': res.encoding,
                    'para': para,
                    'length': len(para.replace('\n', '').replace(' ', ''))
                }

            elif (parser == 'article') and (parser in html) and self.judgeOnly(PARSE_POOL[parser]['only'], html):
                contents = soup.find_all('article')
                para = contents[0].get_text()
                return {
                    'parser': PARSE_POOL[parser]['who'],
                    'encoding': res.encoding,
                    'para': para,
                    'length': len(para.replace('\n', '').replace(' ', ''))
                }


            elif (parser in html) and (parser != 'article') and (parser != 'articleInfo: {') and self.judgeOnly(
                    PARSE_POOL[parser]['only'], html):
                try:
                    kk, vv = parser.split('=')[0], parser.split('=')[1][1:-1]
                    if ' ' in vv:
                        vv = vv.split(' ')[PARSE_POOL[parser]['space']]
                    if PARSE_POOL[parser].get('div'):
                        contents = soup.find_all(PARSE_POOL[parser]['div'], {kk: vv})
                    else:
                        contents = soup.find_all('div', {kk: vv})
                    if PARSE_POOL[parser].get('p'):
                        para = contents[0].get_text()
                    else:
                        para = ''
                        for content in contents[0].find_all('p'):
                            para += content.get_text()
                    para = para.replace('\u3000\u3000', '\n').replace('\xa0', '').replace('\t', '').replace('\r\n','\n')
                    para = para.replace('\n\n', '\n').replace('\n \n', '\n').replace('   ', '').replace('\t\n', '')
                    return {
                        'parser': PARSE_POOL[parser]['who'],
                        'encoding': res.encoding,
                        'para': para,
                        'length': len(para.replace('\n', '').replace(' ', ''))
                    }
                except:
                    print('id-class parser error.')
        return {'parser': 'Unknown', 'encoding': res.encoding, 'para': '', 'length': 0}


    def nlp_word(self, content):
        def ext(sentence, method='TF-IDF'):
            if method == 'TF-IDF':
                result = jieba.analyse.extract_tags(sentence, topK=10, allowPOS=('ns', 'n', 'vn', 'v'))
                return ','.join(result)
            if method == 'TextRank':
                result = jieba.analyse.textrank(sentence, topK=10, allowPOS=('ns', 'n', 'vn', 'v'))
                return ','.join(result)

        pool = []
        for method in ['TF-IDF', 'TextRank']:
            pool.append(ext(content, method=method))
        return pool

    # ITEM_POOL
    def gen_it(self,items):
        for item in items.keys():
            for keyword in items[item]:
                yield (item, keyword)


    def gene_data(self, ITEM_POOL, page,sentimentApi=None):
        for it in self.gen_it(ITEM_POOL):
            field,keyword = it

            dic = self.get_baidu(keyword, page)
            con_pool, len_pool = [], []
            parse_pool, encode_pool = [], []
            word_tf, word_rank = [], []
            sentiment = []
            for link in dic['link']:
                # print(keyword,': ', link)
                para_dic = self.get_content(link)
                para = para_dic['para'].strip()
                word_tf.append(self.nlp_word(para)[0])
                word_rank.append(self.nlp_word(para)[1])
                con_pool.append(para)
                len_pool.append(para_dic['length'])
                parse_pool.append(para_dic['parser'])
                encode_pool.append(para_dic['encoding'])
                sentiment.append(self.getSentiment(para) if not sentimentApi else sentimentApi(para))

            cont_dic = {'content': con_pool, 'length': len_pool, 'parser': parse_pool, 'encoding': encode_pool,
                        'word_tf': word_tf, 'word_rank': word_rank, 'sentiment': sentiment}
            dic.update(cont_dic)
            for i, j in enumerate(dic['link']):
                yield {
                    'field': field,
                    'keyword': keyword,
                    'title': dic['title'][i],
                    'link': dic['link'][i],
                    'pubDate': dic['pubDate'][i],
                    'publish': dic['publish'][i],
                    'length': dic['length'][i],
                    'content': dic['content'][i],
                    'parser': dic['parser'][i],
                    'encoding': dic['encoding'][i],
                    'word_tf': dic['word_tf'][i],
                    'word_rank': dic['word_rank'][i],
                    'sentiment': dic['sentiment'][i]
                }


    def save_data(self, dt):
        save_sql = '''
                    INSERT INTO {0} 
                        (title,crawlTime,keyword,field,length,publish,pubDate,word_TF,word_RANK,emotion,image,video,link,content) 
                    VALUES ('{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}');
                    '''.format(
                                self.tableName,dt['title'], int(time.time()), dt['keyword'], dt['field'],dt['length'], dt['publish'],
                                dt['pubDate'],dt['word_tf'], dt['word_rank'], dt['sentiment'], '', '', dt['link'], dt['content']
        )
        try:
            self.cur.execute(save_sql)
            self.conn.commit()
            print('Save successfully!\r\n{}'.format(dt['link']))
            return 1
        except pymysql.IntegrityError as e1:
            print(e1)
            return 0
        except pymysql.err.ProgrammingError as e2:
            print(e2)
            return 0


    def save_end(self):
        self.cur.close()
        self.conn.close()

    def filter(self, dt, outTitle, outContent, minLength):
        outTitle = outTitle or []
        outContent = outContent or []
        minLength = minLength or 0

        for nokey1 in outTitle:
            if nokey1 in dt['title']: return True
        for nokey2 in outContent:
            if nokey2 in dt['content']: return True
        if dt['length'] < minLength: return True
        return False



def generate(keyPool=None,outTitle=None,outContent=None,minLength=200,perKeyNum=20,pymysql_conn=None,tableName='News',sentimentApi=None):
    '''
    :param keyPool: dict, eg: {'新闻': ['科技', '财经', '体育'],}
    :param outTitle:  list, eg: ['怎么', '好用吗', '什么是', '有什么', '直播：', '视频：']
    :param outContent: list, eg: ['http://', 'var', 'function']
    :param minLength: int,
    :param perKeyNum: int, 20 times better
    :param pymysql_conn: object, pymysql_conn = pymysql.connect()
    :param tableName: str,
    :param sentimentApi: function, score = sentimentApi(text), default score = snownlp.SnowNlp(text).sentiments
    :return: yield dict like json
    '''
    begin = time.time()
    keyPool = keyPool or ITEM_POOL
    outTitle = outTitle or NO_TITLE
    outContent = outContent or NO_CONTENT

    news = BaiduNews(pymysql_conn,tableName)
    saveNum = 0
    try:
        page = perKeyNum // 20 - 1 if perKeyNum >= 20 else 0
        data = news.gene_data(keyPool, page,sentimentApi)
        for dt in data:
            if not news.filter(dt,outTitle,outContent,minLength):
                if pymysql_conn:
                    saveNum += news.save_data(dt)
                else:
                    saveNum += 1
                    yield dt
    finally:
        if pymysql_conn: news.save_end()
        print('saveNumber about: ', saveNum)
        print("useTime: {0} seconds or {1} minutes.".format(round(time.time()-begin,1),round((time.time()-begin)/60,1)))

