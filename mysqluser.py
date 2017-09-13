# -*- coding: UTF-8 -*-
# 安装 MYSQL DB for python
import MySQLdb as mdb
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def getconnect():
    #consor =mdb.connect('localhost', 'root', 'cuilijia', 'mysql');
    ''''''
    consor = mdb.connect(host='123.206.16.129',  # 远程主机的ip地址，
                       user='pink',  # MySQL用户名
                       db='apt',  # database名
                       passwd='pink_man',  # 数据库密码
                       port=3306, # 数据库监听端口，默认3306
                       charset="utf8")  # 指定utf8编码的连接

    return consor

def getfarconnect():
    conn = mdb.connect( host='123.206.16.129',  # 远程主机的ip地址，
                        user='pink',  # MySQL用户名
                        db='apt',  # database名
                        passwd='pink_man',  # 数据库密码
                        port=3306)  # 数据库监听端口，默认3306
                        #charset="utf8")  # 指定utf8编码的连接
    return conn

def test():
    con = getfarconnect()
    cur = con.cursor()
    # 使用execute方法执行SQL语句
    cur.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据库。
    data = cur.fetchone()

    print "Database version : %s " % data

    # 关闭数据库连接
    con.close()

def search1(TABLE):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM %s " % (TABLE)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        for row in results:
            url = row[0]
            time = row[1]

            # 打印结果
            print "url=%s   time=%s" % (url, time)

    except:
        print "Error: unable to fecth data"
    con.close()


def search2(TABLE):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM %s " % (TABLE)
    cur.execute(sql)
    # 获取所有记录列表
    results = cur.fetchall()
    con.close()
    return results


def search3(TABLE,url):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT 1 FROM %s WHERE url ='%s' limit 1" % (TABLE,url)
    #sql = """SELECT * FROM %s """%(TABLE)
    try:
     cur.execute(sql)
     # 获取所有记录列表
     results = cur.fetchall()
     con.close()
     if (len(results) ==0):
         return 0
     else:
         return 1
    except:
        print "Error: unable to fecth data"
    con.close()

def ifexist(TABLE,url):

    key = search3(TABLE,url)
    if (key ==0):
       return 0
    else:
       return 1

def searchword(word):
    con = getconnect()
    cur = con.cursor()
    word=word.replace('\n', '')
    word = word.replace('\r', '')
    word = word.replace(' ', '')
    word = word.replace('　', '')
    sql = "SELECT * FROM WORDTOTAG WHERE word ='%s' limit 1" % (word)
    #sql = """SELECT * FROM %s """%(TABLE)
    try:
     cur.execute(sql)
     # 获取所有记录列表
     results = cur.fetchall()
     con.close()
     return results
    except:
        print "Error: unable to fecth data"
    con.close()

def insert1(TABLE,url):
    con = getconnect()
    cur = con.cursor()
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    #url='www.baidu111.com'
    sql = """INSERT INTO %s(url,time) VALUES ('%s', '%s')"""%(TABLE,url,dt)
    try:
     # 执行sql语句
     cur.execute(sql)
     # 提交到数据库执行
     con.commit()
    except:
     # Rollback in case there is any error
     con.rollback()
    con.close()

def insertword(word,num):
    con = getconnect()
    cur = con.cursor()
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    result=searchword(word)
    #print word
    #if(len(result)!=0):
    #   print result[0][0]
    if(len(result)==0):
      sql = """INSERT INTO WORDTOTAG (word,num,time) VALUES ('%s', '%d', '%s')"""%(word,num,dt)
      try:
       # 执行sql语句
       cur.execute(sql)
       # 提交到数据库执行
       con.commit()
      except:
       # Rollback in case there is any error
       con.rollback()

    con.close()

def createtable(TABLE):
 # 如果数据表已经存在使用 execute() 方法删除表。
 #set character_set_database=utf8;
 #set character_set_server=utf8;
 #cur.execute("DROP TABLE IF EXISTS %s")%(TABLE)
 con = getconnect()
 cur = con.cursor()
 # 创建数据表SQL语句
 sql = """CREATE TABLE %s (
             word  CHAR(255) NOT NULL,
             num   INT ,
             time  DATE )
             ENGINE = MyISAM
             DEFAULT
             CHARSET = utf8;"""%(TABLE)


 cur.execute(sql)
 print ("create table %s successful!"%(TABLE))
 con.close()


def delete1(TABLE,url):
 # 如果数据表已经存在使用 execute() 方法删除表。
 # SQL 删除语句
 con = getconnect()
 cur = con.cursor()
 sql = "DELETE FROM %s WHERE url = '%s'" % (TABLE,url)

 try:
     # 执行SQL语句
     cur.execute(sql)
     # 提交修改
     con.commit()
 except:
     # 发生错误时回滚
     con.rollback()
 con.close()


#http://www.freebuf.com/?s=APT
#search1("APTLIB")
#createtable("WORDTOTAG")
#insert1("APTURL","http://www.freebuf.com/articles/web/27639.html")
#insert1("APTLIB","http://www.freebuf.com/articles/web/27639.html")
#test()
#insertword("安全",3)
#searchword(" ")