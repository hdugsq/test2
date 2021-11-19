import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='gaoshiqi21',
                     database='pythondb')
 
mycursor = db.cursor()
 
mycursor.execute("insert into test(id,name) values(2,'涛哥')")
 
db.commit()    # 数据表内容有更新，必须使用到该语句
 
print(mycursor.rowcount, "记录插入成功。")
db.close()