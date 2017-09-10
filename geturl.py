#-*- coding: utf-8 -*-
import urllib2
import re
import tool
import sys
import mysqluser

def geturllist(url):

 reload(sys)
 sys.setdefaultencoding('utf-8')

 try:
     headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
     request = urllib2.Request(url, headers=headers)
     response = urllib2.urlopen(request)
     # pageCode = response.read()
     pageCode = response.read().decode('utf-8')
     tool.Tool()

 except urllib2.URLError as e:
     if hasattr(e, 'reason'):
         print '连接threatbook失败，错误原因', e.reason

 print ("get web success!")

 pattern3 = re.compile(r'href="http(.*?)"',re.S)

 items2 = re.findall(pattern3, pageCode)

 for item in items2:
   if item != '':
       te = 'http' + item

       ans=mysqluser.ifexist("URLLIB",te)

       if (ans == 0):
           mysqluser.insert1("URLLIB",te)
           mysqluser.insert1( "TEMURL", te)
           print te

def getoneAPT(url):
    geturllist(url)
    if(mysqluser.ifexist("APTURL",url)):
        mysqluser.delete1("APTURL",url)


def gettemurl():

  results=mysqluser.search2("APTURL")
  if(len(results)!=0):
    for x in range(len(results)):
        print results[x][0]
        getoneAPT(results[x][0]);
  else:
    print ("there is not APT url needed to crawl!")

#geturllist("http://www.freebuf.com/special/144565.html")
#gettemurl()

