"""
read_db.py
pymysql 读操作演示
"""

import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 生成游标对象 (操作数据库,执行sql语句)
cur = db.cursor()
# (('Tony',), ('Abby',), ('make',), ('rubbot',))
# 执行各种对数据库的读写操作
name = input("name:")
sql = "select * from interest where name=%s"
cur.execute(sql,name)
# for i in cur:
#     print(i)

# 获取一个查询结果
print(cur.fetchone())
# print(cur.fetchmany())


# 关闭游标和数据库连接
cur.close()
db.close()
