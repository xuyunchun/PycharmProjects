#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "flaskdb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO tNews(news_title,news_content) \
       VALUES ('%s', '%s' )" % \
      ('test_title', 'test_content')
#
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#     LAST_NAME, AGE, SEX, INCOME) \
#     VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#       ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()