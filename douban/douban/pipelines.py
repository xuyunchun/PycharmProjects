# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import copy
# import logging
# twisted: 用于异步写入(包含数据库)的框架，cursor.execute()是同步写入
from twisted.enterprise import adbapi



class DoubanPipeline(object):
    def __init__(self):
        self.file = open("./movie.json", "wb")

    def process_item(self, item, spider):
        # 编码的转换
        for k in item:
            item[k] = item[k].encode("utf8")
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


# class MySQLTwistedPipeline(object):
#     def __init__(self, pool):
#         self.dbpool = pool
#
#     @classmethod
#     def from_settings(cls, settings):
#         """
#         这个函数名称是固定的，当爬虫启动的时候，scrapy会自动调用这些函数，加载配置数据。
#         :param settings:
#         :return:
#         """
#         params = dict(
#             host=settings['MYSQL_HOST'],
#             port=settings['MYSQL_PORT'],
#             db=settings['MYSQL_DB'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             charset=settings['MYSQL_CHARSET'],
#             cursorclass=pymysql.cursors.DictCursor
#         )
#
#         # 创建一个数据库连接池对象，这个连接池中可以包含多个connect连接对象。
#         # 参数1：操作数据库的包名
#         # 参数2：链接数据库的参数
#         db_connect_pool = adbapi.ConnectionPool('pymysql', **params)
#
#         # 初始化这个类的对象
#         obj = cls(db_connect_pool)
#         return obj
#
#     def process_item(self, item, spider):
#         """
#         在连接池中，开始执行数据的多线程写入操作。
#         :param item:
#         :param spider:
#         :return:
#         """
#         # 参数1：在线程中被执行的sql语句
#         # 参数2：要保存的数据
#         result = self.dbpool.runInteraction(self.insert, item)
#         # 给result绑定一个回调函数，用于监听错误信息
#         result.addErrback(self.error)
#
#     def error(self, reason):
#         print('--------', reason)
#     # 下面这两步分别是数据库的插入语句，以及执行插入语句。这里把插入的数据和sql语句分开写了，跟何在一起写效果是一样的
#     def insert(self, cursor, item):
#         insert_sql = "INSERT INTO movieslist(score_num, movie_name, ranking, score) VALUES (%s, %s, %s, %s)"
#         cursor.execute(insert_sql, (item['score_num'], item['movie_name'], item['ranking'], item['score']))
#         # 不需要commit()

class MySQLPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("pymysql",
                                           host="122.51.185.225",   #本机"127.0.0.1",
                                           port=3306,               #端口，本机3308
                                           db = "tinyweb",            # 数据库名 本机moviedb
                                           user = "root",       # 数据库用户名
                                           passwd = "19921118",     # 密码 本机123456
                                           cursorclass = pymysql.cursors.DictCursor,
                                           charset = "utf8"
                                           )
    def process_item(self, item, spider):
        asynItem = copy.deepcopy(item)
        query = self.dbpool.runInteraction(self._conditional_insert, asynItem)
        #query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):

        tb.execute("insert into movieslist (score_num, movie_name, ranking, score,movie_url) values (%s, %s, %s, %s,%s)",\
                   (item['score_num'], item['movie_name'], item['ranking'], item['score'],item['movie_url']))
        #logging.info("Item data in db: %s" % item, level=logging.DEBUG)

    #def handle_error(self, e):
     #   logging.ERROR (e)