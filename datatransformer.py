# -*- coding: UTF-8 -*-
import MySQLdb as mdb
import datetime
import re

def getconnect():
    # consor =mdb.connect('localhost', 'root', 'cuilijia', 'mysql');
    consor = mdb.connect(host='123.206.16.129',  # 远程主机的ip地址，
                       user='pink',  # MySQL用户名
                       db='apt',  # database名
                       passwd='pink_man',  # 数据库密码
                       port=3306,  # 数据库监听端口，默认3306
                       charset="utf8")  # 指定utf8编码的连接
    return consor

def search1(TABLE):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM %s " % (TABLE)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        return results

        for row in results:
            time1 = row[0]
            time2 = row[1]
            time3 = row[2]
            time4 = row[3]
            time5 = row[4]
            time6 = row[5]
            time7 = row[6]
            time8 = row[7]
            time9 = row[8]
            #time10 = row[9]

            pattern = re.compile(r'<script.*?>.*?</script.*?>', re.S)
            #time4 = re.sub(pattern, "", time4)
            time4 = re.sub("<p>", "", time4)
            time4 = re.sub("</p>", "", time4)
            time4 = re.sub("<P>", "", time4)
            time4 = re.sub("</P>", "", time4)
            time4 = re.sub("<b>.*?</b>", "", time4)

            #print "%s   %s   %s   %s   %s   %s   %s   %s   %s"\
             #     % (time1,time2,time3,time4,time5,time6,time7,time8,time9)
            print "%s "  % (time8)

    except:
        print "Error: unable to fecth data"
    con.close()

def search2(TABLE):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM %s " % (TABLE)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        #return results
        for row in results:
            time1 = row[0]
            time2 = row[1]
            time3 = row[2]
            time4 = row[3]
            time5 = row[4]
            time6 = row[5]
            time7 = row[6]
            time8 = row[7]
            time9 = row[8]
            #time10 = row[9]

            pattern2 = re.compile(r'<span class="vb-cTag">(.*?)</span>', re.S)
            items = re.findall(pattern2, time9)
            for item in items:
                print item
                TID=search_tag(item)
                IID=search_IN(time7)
                insert_TAG(IID,TID)
                #insert(item)

            '''
            time9 = re.sub("<span class=.*?>", "", time9)
            time9 = re.sub("</span>", "", time9)
            '''

            print "%s " % (time1)
            #print "%s   %s   %s   %s   %s   %s   %s   %s   %s"\
            #      % (time1,time2,time3,time4,time5,time6,time7,time8,time9)

    except:
        print "Error: unable to fecth data"
    con.close()

def search3(TABLE):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM %s " % (TABLE)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        #return results
        for row in results:
            time1 = row[0]
            time2 = row[1]
            time3 = row[2]

            print "%s   %s   %s  "\
                  % (time1,time2,time3)

    except:
        print "Error: unable to fecth data"
    con.close()

def search_tag(tag):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM Tag_info where name='%s'" % (tag)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        #return results
        for row in results:
            time1 = row[0]
            time2 = row[1]
            time3 = row[2]

            print "%s   %s   %s  "\
                  % (time1,time2,time3)
            con.close()
            return time1

    except:
        print "Error: unable to fecth data"
    con.close()

def search_IN(url):
    con = getconnect()
    cur = con.cursor()
    sql = "SELECT * FROM Intelligence_info where URL='%s'" % (url)
    try:
        # 执行SQL语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        #return results
        for row in results:
            time1 = row[0]
            time2 = row[1]
            time3 = row[2]

            print "%s   %s   %s  "\
                  % (time1,time2,time3)
            con.close()
            return time1

    except:
        print "Error: unable to fecth data"
    con.close()

def transform(TABLE,list=[]):
  con = getconnect()
  cur = con.cursor()
  dt = datetime.datetime.now().strftime("%Y-%m-%d")
  n=1
  for item in range(len(list)):

    time4 = re.sub("<p>", "", list[item][3])
    time4 = re.sub("</p>", "", time4)
    time4 = re.sub("<P>", "", time4)
    time4 = re.sub("</P>", "", time4)
    time4 = re.sub("<b>.*?</b>", "", time4)

    print list[item][1],list[item][2],time4,list[item][4],dt,dt,list[item][6],list[item][7]
    sql = """INSERT INTO %s(title,author,content,site,publishtime,crawltime,URL,sourceid) 
              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""\
          %(TABLE,list[item][1],list[item][2],time4,list[item][4],dt,dt,list[item][6],list[item][7])
    try:
      # 执行sql语句
      cur.execute(sql)
      # 提交到数据库执行
      con.commit()
    except:
      # Rollback in case there is any error
      con.rollback()

    #break

  con.close()

def delete1(TABLE):
 # 如果数据表已经存在使用 execute() 方法删除表。
 # SQL 删除语句
 con = getconnect()
 cur = con.cursor()
 for x in range(1,9):

  sql = "DELETE FROM %s where id=%d" % (TABLE,x)

  try:
     # 执行SQL语句
     cur.execute(sql)
     # 提交修改
     con.commit()
  except:
     # 发生错误时回滚
     con.rollback()
 con.close()

def insert(tag):
    con = getconnect()
    cur = con.cursor()
    #print dt
    sql = """CALL create_tag ('%s','%s');""" %(tag,"")
    try:
      # 执行sql语句
      cur.execute(sql)
      # 提交到数据库执行
      con.commit()
      print ("!!!")
    except:
      # Rollback in case there is any error
      con.rollback()

    con.close()

def insert_TAG(IID,TID):
    con = getconnect()
    cur = con.cursor()
    #print dt
    sql = """INSERT INTO intelligencetag_info (intelligenceid,tagid) VALUES ('%s', '%s')""" % (IID, TID)

    try:
      # 执行sql语句
      cur.execute(sql)
      # 提交到数据库执行
      con.commit()
      print ("!!!")
    except:
      # Rollback in case there is any error
      con.rollback()

    con.close()

a=[]
list=[]
list=search2("threatbook")
#a=search2("Intelligence_info")
#transform("Intelligence_info",list)
#insert("Tag_info","APT")
#delete1("Intelligence_info")
#Tag_info
#search3("Tag_info")
#search_tag("APT")