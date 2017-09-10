# -*- coding:utf-8 -*-

import cutwords


def testfunc(url):
  number=1
  #urllist=["http://www.freebuf.com/articles/neopoints/126926.html",
           #"http://www.freebuf.com/articles/neopoints/126926.html" ]

  for i in range(0,1):
      number += 1
      S=cutwords.finddata(url, number, "file/train.data")
