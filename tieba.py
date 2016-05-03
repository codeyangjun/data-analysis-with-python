# -*- coding: utf-8 -*-
"""
Created on Tue May 03 11:14:44 2016

@author: yangjun1
"""

import urllib
#import file

urlPrefixion = "http://tieba.baidu.com/p/100000000"
for i in range(0,10):
    url = urlPrefixion + str(i)
    r = urllib.urlopen(url)
    html = r.read()
    filePrefixion = 100000000 + str(i)+'.txt'
    f = open(filePrefixion, 'wb')
    f.write(html)
    
    