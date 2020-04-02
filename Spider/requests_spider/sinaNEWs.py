import requests
import re
import pymysql
import datetime
import time
from lxml import etree

def search_article(url):
    """
    请求所传的url
    args：
        url: 所要请求的url
    return:
        类lxml.etree._Element的元素, 可以直接用xpath解析
    """

    header = {
        'Accept': '*/*',
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/66.0.3359.181 Safari/537.36'
    }
    resp = requests.get(url, headers=header)
    html_str = str(resp.content, 'utf-8')
    selector = etree.HTML(html_str)
    return selector


def parse_html(selector):
    """
    解析提取的lxml.etree._Element的元素
    return:
        type:dict
            key:news title
            value: contents of news
    """
    try:
        title_text = selector.xpath('//h3/text()')[0]
        url_text = selector.xpath("//@href")
        # 获取class=article的div下面的p标签的所有text()
        article_text = selector.xpath('//div[@class="article"]/p//text()')

        return {title_text: article_text}
    except Exception as e:
        return {'解析错误': [e]}


def write_article(article):
    """
    将所传的新闻字典写入文件news.txt中
    args：
        article：dict {news_title:[contents,]}
    No return
    """
    file_name = 'news.txt'
    f = open(file_name, 'a', encoding='utf-8')
    title = list(article.keys())[0]
    f.write("题目："+title + '\n')
    for content in article[title]:
        f.write(content+"\n")
    f.write("\n\n")
    f.close()


def extract_url(url):
    href_lists = search_article(url).xpath("//div[@id='fin_tabs0_c0']//a//@href")
    return href_lists

"""
    将所传的新闻字典写入mysql中
    args：
        article：dict {news_title:[contents,]}
    No return
    """
def mysql_create():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "flaskdb")
    sql_create = """CREATE TABLE tNews (news_title VARCHAR(265),news_content VARCHAR(3908))"""
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS tNews")
    cursor.execute(sql_create)# 执行SQL语句
    db.close()  # 关闭数据库连

def IntoMysql(article):
    db = pymysql.connect("localhost", "root", "123456", "flaskdb")
    cursor = db.cursor()
    title = list(article.keys())[0]

    for content in article[title]:
        sql = """
                    INSERT INTO tNews(news_title,news_content)VALUES ('%s', '%s' )
                  """ % (title,content)

        try:
            sql = sql.encode('utf-8')
            cursor.execute(sql)
            db.commit()
        except:pass
    db.close()


if __name__ == '__main__':
    url = "http://finance.sina.com.cn/"
    href_list = extract_url(url=url)
    for href in href_list:
        # 排除非新浪连接
        if href.startswith("http://finance.sina.com.cn/"):
            try:
                html = search_article(href)
                article = parse_html(html)
                write_article(article)
                mysql_create()
                IntoMysql(article)
            except Exception as e:
                print(e)