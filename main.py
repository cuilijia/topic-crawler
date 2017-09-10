#-*- coding: utf-8 -*-

import geturl
import crawler

if __name__ == '__main__':

  print("主题爬虫系统：")

  for x in range(1000):
     print("功能： A 爬取新的页面  B 识别已爬取的页面  Q退出")
     content = raw_input("input:")

     if(content=="A" or content=="a"):
        print ("爬取中...")
        geturl.gettemurl()

     if(content=="B" or content=="b"):
        print ("输入解析页面个数：")
        num = raw_input("number=")
        print ("解析中...")
        num=int(num)
        crawler.recognize(num)

     if(content=="Q" or content=="q"):
        break

