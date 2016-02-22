#coding=utf-8
#!/usr/bin/python
import mysql.connector;

try:
    conn = mysql.connector.connect(host='127.0.0.1', port='3306', user='root', password="", database="information_schema", use_unicode=True);
    cursor = conn.cursor();
    cursor.execute('select * from engines t where t.support = "NO"');
    # 取回的是列表，列表中包含元组
    list = cursor.fetchall();
    print list;

    for record in list:
        print record

except mysql.connector.Error as e:
    print ('Error : {}'.format(e));
finally:
    cursor.close;
    conn.close;
    print 'Connection closed in finally';