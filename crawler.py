# -*- coding:utf-8 -*-
import recognition
import cutwords
import mysqluser

def testfunc(url):

  document = open("file/urlanalyse.data", "w+");
  document.close()
  S=cutwords.finddata(url, 1, "file/urlanalyse.data")
  if(S==0):
      return 0
  else:
      return 1

def recognize(num):
    urlist = []
    results=mysqluser.search2( "TEMURL")
    for i in range(num):
        print results[i][0]
        urlist.append(results[i][0])
        mysqluser.delete1("TEMURL",urlist[i])

    for aurl in urlist:
        S=testfunc(aurl)
        if(S==1):
           document = open("file/urlanalyse.data", "r");
           if(document is None):
             print ("none!")
             document.close()
             break
           document.close()
           key=recognition.analysis()
           if(key==1):
               mysqluser.insert1("APTURL",aurl)
               mysqluser.insert1("APTLIB", aurl)

        else:
           return 0

#S=recognize(1)