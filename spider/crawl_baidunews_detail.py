# -*- coding:utf-8 -*-
# author: lsl
# date: 2017.10.17
# purpose: 爬取基金业协会的产品数据库中的专户一对多列表的详情页面

import requests, pymongo, pymysql, datetime, time, random, threading
from bs4 import BeautifulSoup
import chardet
# import config
# import cx_Oracle
import sys, os

# reload(sys)
# sys.setdefaultencoding('utf-8')
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# 标准化爬虫模板 2017-10-18 start
CRAWL_ID = 'A0005'
CRAWL_VERSION = '1'
OPERATOR = 'ZSW'  # 请运行的工程师改为自己的代号
# 分布式节点ID
NODE_ID = '01'
OP_TIME = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
TASK_ID = OPERATOR + CRAWL_ID + str(CRAWL_VERSION) + NODE_ID + OP_TIME
ROWCOUNT = 0
TIME_START = datetime.datetime.now()
max_try = 10  # 每个页面如失败则重新爬取的最大次数

thread_count = 5  # 存在运行中的最大线程数
alive_thread_count = 0  # 运行中的线程数
finished_thread_count = 0  # 完成的线程数


# 记录爬虫任务日志
def crawl_task_logger(is_begin, is_end, is_error, rows_insterted):
    conn, cursor = get_conn()
    if conn == None or cursor == None:
        return False
    try:
        # % ( CRAWL_ID, CRAWL_VERSION)
        sql = "select count(crawl_id) as id from mdm_crawl_home where crawl_id = {}and crawl_version = {}".format(
            CRAWL_ID, CRAWL_VERSION)

        cursor.execute(sql)
        if cursor.fetchone()['id'] == 0:
            sql = 'insert into mdm_crawl_home(crawl_id,crawl_version,crawl_name,crawl_dept,crawl_datatype,crawl_desc,version_diff,crawl_frequency,crawl_author,crawl_operator) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (
                CRAWL_ID, CRAWL_VERSION, 'crawl_baidunews.py', u'金融科技部', u'发债主体新闻动态', u'从baidu新闻爬取发债主体的新闻', None,
                u'持续运行',
                'fhx', 'zsw'))
        sql = 'INSERT INTO log_tasks (operator,crawl_id,crawl_version,task_id,node_id,is_begin,is_end,is_error,rows_inserted) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, (
            OPERATOR, CRAWL_ID, CRAWL_VERSION, TASK_ID, NODE_ID, is_begin, is_end, is_error, rows_insterted))
        conn.commit()
        return True
    except Exception as e:
        print(repr(e))
        return False
    finally:
        # 关闭游标
        if cursor != None:
            cursor.close()
        # 关闭数据库连接
        if conn != None:
            conn.close()


# 记录爬虫异常日志
def crawl_exception_logger(task_params, exception_kind, exception_output):
    conn, cursor = get_conn()
    if conn == None or cursor == None:
        return False
    try:
        sql_e = 'INSERT INTO log_exceptions (crawl_id,task_id,node_id,task_params,exception_kind,exception_output) VALUES (%s,%s,%s,%s,%s,%s)'
        print(u'写入错误日志')
        cursor.execute(sql_e, (CRAWL_ID, TASK_ID, NODE_ID, task_params, exception_kind, exception_output))
        # 提交错误日志语句
        conn.commit()
        return True
    except Exception as e:
        print(repr(e))
        return False
    finally:
        # 关闭游标
        if cursor != None:
            cursor.close()
        # 关闭数据库连接
        if conn != None:
            conn.close()


USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"]

headers = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate'
}


# 页面解析模块
def crawl_analysis(url, flag=False):
    try:
        req = requests.Session()
        res = None
        if not flag:
            # 返回原始socket respons，需要加参数stream=True
            # proxies=config.proxy_conf  暂时不代理
            res = req.get(url, headers=headers, stream=True, timeout=20)
        else:
            res = req.get(url, timeout=20)
        if res.status_code == 200:
            return res.content
        else:
            print(u'状态码:%d' % res.status_code)
            return None
    except Exception as e:
        raise Exception(e)


# 页面抓取模块
def crawl_attempt(url, max_try=10):
    attempts = 0
    is_first = True
    flag = False
    while attempts < max_try:
        try:
            html = crawl_analysis(url, flag)
            if html != None:
                return html
        except Exception as e:
            if is_first:
                is_first = False
                crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
            print(repr(e))
            if 'Exceeded 30 redirects' in str(repr(e)):
                flag = True
        finally:
            attempts += 1
            time.sleep(3)
        print(u'第%d次请求失败' % attempts)
    return None


# 基础爬虫框架
def crawl_frame(word, page_index):
    url = 'http://news.baidu.com/ns?word=%s&&pn=%d&cl=2&ct=0&tn=news&rn=20&ie=utf-8&bt=0&et=0' % (
        word, (page_index - 1) * 20)
    global ROWCOUNT
    ROWCOUNT = page_index
    html = crawl_attempt(url)
    is_next_page = False
    datas = []
    if html != None:
        print(u'请求成功')
        try:
            print(u'解析第%d页' % page_index)
            bs = BeautifulSoup(html, 'html.parser')
            # 判断是否还有下一页
            p_next = bs.find('p', id='page')
            if p_next != None and u'下一页' in p_next.text:
                is_next_page = True

            results = bs.find('div', id='content_left').find_all('div', class_='result')
            total = len(results)
            cur_num = 0
            for result in results:
                cur_num += 1
                data = dict()
                data['word'] = word
                title_a = result.find('a')
                data['title'] = title_a.text.strip().strip('\n')  # 标题
                data['url'] = title_a.attrs['href']  # 链接
                p = result.find('p', class_='c-author').text.split(u'\xa0')
                data['source'] = p[0]  # 来源
                data['newstime'] = calc_date(p[-1])  # 发布日期
                if data['title'][-3:] == '...':
                    print(u'请求新闻页面......')
                    html = crawl_attempt(data['url'])
                    if html != None:
                        try:
                            print(u'请求成功，获取完整标题')
                            charset = chardet.detect(html)['encoding'].lower()
                            bs = BeautifulSoup(html.decode(charset, 'ignore'), 'html.parser')
                            # 获取完整标题
                            full_title = bs.title.text.strip().strip('\n')
                            if full_title != None and len(full_title) > 0:
                                data['title'] = full_title
                            print(u'获取成功')
                        except Exception as e:
                            print(u'获取失败')
                            crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
                            print(repr(e))
                    else:
                        print(u'请求新闻页面失败')
                data['savetime'] = str(time.strftime('%Y-%m-%d %H:%M:%S'))
                insert(data)
                datas.append(data)
                print(u'关键字:%s\r\n标题:%s\r\n链接:%s\r\n来源:%s\r\n发布日期:%s\r\n' % (
                    word, data['title'], data['url'], data['source'], data['newstime']))
            print(u'解析成功')

            return True, is_next_page, datas
        except Exception as e:
            print(u'解析失败:%d,%d' % (total, cur_num))
            crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
            print(repr(e))
    else:
        print(u'请求失败')

    return False, is_next_page, datas


# 通过时分秒计算具体的时间
def calc_date(s):
    words = {u'小时': 3600, u'分钟': 60, u'秒': 1}
    second = 0
    for k, v in words.items():
        temp = s.split(k)
        if len(temp) == 2:
            second = int(temp[0]) * v
            break
    if second != 0:
        return time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time() - second))
    else:
        return s.replace(u'年', '-').replace(u'月', '-').replace(u'日', '')


# 将数据写入到数据库表中
def insert(data):
    conn, coll = get_conn1()
    coll.insert(data)
    print("插入成功")


# def insert(datas):
#     sql = 'INSERT INTO crawl_baidunews_test_fhx2 (word,source,title,newstime,savetime,url) VALUES (%(word)s,%(source)s,%(title)s,%(newstime)s,%(savetime)s,%(url)s)'
#     conn, cursor = get_conn()
#     try:
#         for data in datas:
#             cursor.execute(sql, data)
#         # 提交sql语句
#         conn.commit()
#         print(u'入库成功')
#     except Exception as e:
#         # 错误回滚
#         conn.rollback()
#         crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
#         print(repr(e))
#         print(u'入库失败')
#     finally:
#         # 关闭游标
#         if cursor != None:
#             cursor.close()
#         # 关闭数据库连接
#         if conn != None:
#             conn.close()


# 爬取所有页面
def crawl_with_pages(word):
    page_index = 1  # 页码
    is_next_page = True  # 是否有下一页
    all_datas = []  # 所有数据
    datas = []  # 当前页的数据
    while is_next_page:
        print(u'第%d页请求中......' % page_index)
        time.sleep(3)
        result, is_next_page, datas = crawl_frame(word, page_index)
        all_datas.extend(datas)
        if not is_next_page:
            # insert(all_datas)
            all_datas = []
            return result
        page_index += 1
    return False


# 爬虫线程类
class CrawlerThread(threading.Thread):

    def __init__(self, word):
        threading.Thread.__init__(self)
        self.word = word

    # 当线程启动就执行该方法
    def run(self):
        global finished_thread_count, alive_thread_count
        try:
            alive_thread_count += 1
            crawl_with_pages(self.word)
        except Exception as e:
            # 所有的错误信息写入日志
            crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
            print(repr(e))
        finally:
            finished_thread_count += 1
            alive_thread_count -= 1


# 从oracle中获取所有的关键字
# def get_words_by_oracle1():
#     oracle_conn = None
#     oracle_cursor = None
#     try:
#         oracle_conn = cx_Oracle.connect(config.o_db_conf['user'], config.o_db_conf['passwd'], config.o_db_conf['db'])
#         oracle_cursor = oracle_conn.cursor()
#         sql = "select distinct s_info_compname from tydw_filesync.cbondissuer where rownum < 14"
#         oracle_cursor.execute(sql)
#         return oracle_cursor.fetchall()
#     except Exception as e:
#         print
#         repr(e)
#         crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
#         return None
#     finally:
#         if oracle_cursor != None:
#             oracle_cursor.close()
#         if oracle_conn != None:
#             oracle_conn.close()


def get_words_by_oracle():
    words = ["窃格拉瓦", "打工", "乐视股票", "腾讯股票", "京东方", "小米", "华为", "胖猪", "广东话", "随便吧", "少数派", "民进党", "黄智贤"]
    return random.choice(words)


# 获取数据库连接
def get_conn():
    try:
        # conn = pymysql.connect(**config.db_conf)
        conn = pymysql.connect(host='localhost', user='root', password='root', database='news', port=3306)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor
    except Exception as e:
        print(repr(e))

        print(u'数据库连接失败')

        crawl_exception_logger('{page:%d}' % ROWCOUNT, repr(e), e.message)
        return None, None


# mongodb版本
def get_conn1():
    try:
        conn = pymongo.MongoClient(host="127.0.0.1", port=27017)
        db = conn['baidu']  # 创建一个数据库,或者conn.mydb 直接连接已存在的

        coll = db['info']  # 创建聚集(mysql中的表),或者直接连接聚集
        return db, coll
    except Exception as e:
        print(e)


# 开始爬虫
def start_crawl():
    print(u'爬虫节点编号：' + NODE_ID)

    start_time = time.time()
    try:
        #        words = list(set([w.decode("gbk").strip("\r\n") for w in file(os.getcwd()+'/bondissuer.txt',"r").readlines()]))
        words = get_words_by_oracle()  # 从oracle中获取关键字
        if words == None or len(words) == 0:
            print(u'没有关键字')

            return
        for i in range(len(words)):  # 遍历所有的关键字
            while True:
                if alive_thread_count < thread_count:  # 判断如果当前运行中的线程数小于最大线程数，则继续启动新线程
                    break
                time.sleep(3)
            print(u'查询关键字:%s' % words[i][0])

            ct = CrawlerThread(words[i][0])  # 实例化爬虫线程
            ct.daemon = True  # 后台运行
            ct.start()  # 开启线程
            time.sleep(2)

        while True:  # 在线程没有跑完的情况下，主程序保持运行状态
            if len(words) == finished_thread_count:  # 如果完成的线程数与关键字数一致则退出循环，随之程序停止
                break
            time.sleep(3)  # 睡眠一段时间，避免执行太过频繁

        print(u'任务完成，总花费时间：%s' % (time.time() - start_time))

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    start_crawl()
