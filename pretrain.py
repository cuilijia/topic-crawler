# -*- coding:utf-8 -*-

import urllib2
import re
import tool
import jieba
import pandas as pd
import sys

def finddata(url,number,txt):

   reload(sys)
   sys.setdefaultencoding('utf-8')


   docx = number
   beforedocx = docx-1
   news1 = []
   num1 = []#记录每个单词出现个数
   key = 0

   numtxt = txt
   datatxt = "file/vocabulary.txt"

   vocSrc = r'file/vocabulary.txt'
   voc = pd.read_table(vocSrc, names=['voc'])
   if ( beforedocx != docx):
       for j in range(0, len(voc['voc'])):
              num1.append(0)

   stopwords = {}.fromkeys(['的', '包括', '等', '是', '我', ' ', '.', '', '  ',
                          '。', '，', ',', ':', ';', '"', '_', '>', '；', '-',
                          '/', '“', '”', '（', '）', '(', ')', '&', '？',  '：'])

     #with open(numtxt, 'r') as f:
     # for line in f:
     #     str_docIdx, str_wordIdx, str_cnt = line.split()
     #     docIdx = int(str_docIdx)
     #    wordIdx = int(str_wordIdx)
     #     cnt = int(str_cnt)

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


   pattern = re.compile(r'<script.*?>.*?</script.*?>',re.S)
   pageCode2 = re.sub(pattern, "", pageCode)
   pattern = re.compile(r'<style.*?>.*?</style.*?>',re.S)
   pageCode2 = re.sub(pattern, "", pageCode2)
   # print pageCode2
   pattern2 = re.compile(r'>(.*?)<',re.S)
   # pattern = re.compile(r'div class="cTag-list">(.*?)<',re.S)
   pattern3 = re.compile(r'href="http(.*?)"',re.S)
   items1 = re.findall(pattern2, pageCode2)
   items2 = re.findall(pattern3, pageCode)

   if(items1 is None):
       print ("one no-webpage!")
       return 0

   print ("analysing...")

   for item in items1:
     item = item.strip().strip()
     if item != '':
       text = item
       print ('>'),

       seg_list = jieba.cut(text, cut_all=False)
       for i in list(seg_list):
        if ( i not in stopwords ):
         key = 0
         for a in voc['voc']:
             if ( i == a ):
                 key = 1
                 break
             else :
                 key = 0
         if ( key == 0 ):
                  voc.loc[i] = {'voc': i}
                  num1.append(1)
         else:
            for j in range(0, len(voc['voc'])):
                    if ( voc['voc'][j] == i ):
                        num1[j] += 1


   document = open(datatxt, "w+");

   if ( docx != beforedocx):
       documentnum = open(numtxt, "a")
   else:
       documentnum = open(numtxt, "w+")

   for k in range(0, len(voc['voc'])):
    # print ("%-5d  %-20s %-5d" % (k+1, voc['voc'][k],num1[k]))
      document.write(str(voc['voc'][k]));
      document.write("\n");

      if( num1[k] != 0 ):
       documentnum.write(str(docx))
       documentnum.write(" ")
       documentnum.write(str(k+1))
       documentnum.write(" ")
       documentnum.write(str(num1[k]))
       documentnum.write("\n")

   document.close()
   documentnum.close()

   return 1

def test():
    print ("this is test!!")
    return 1