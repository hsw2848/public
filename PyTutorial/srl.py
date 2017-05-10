
# -*- coding: utf-8 -*-
'''
Created on 2015. 1. 28.
네이버 실시간 검색어
@author: sw.han
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

import pymysql
import time
import urllib
import os

import io

import shutil
import base64
    
conn = pymysql.Connect(host='192.168.1.2', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8')
cur = conn.cursor()

base_url = ("http://www.slrclub.com/bbs/vx2.php?id=work_gallery&no=1139624")
html = urlopen(base_url).read()#.decode('cp949','ignore')
 
soup = BeautifulSoup(html, 'html.parser')
soup = soup.find('div', {'id':'userct'})
soup = soup.find('img')
#  
url = print(soup.get('src'))
 
# print(soup.prettify())
 
# html = urlopen(url).read()
#  
# f = open('test.jpg', 'wb')
# f.write(html)
# f.close()



#  with urllib.request.urlopen(url) as response, open(url, 'wb') as out_file:
#      shutil.copyfileobj(response, out_file)

