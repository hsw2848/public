
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

while 1:
        
    conn = pymysql.Connect(host='save.gonetis.com', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8')
    cur = conn.cursor()
    
    base_url = ("http://www.naver.com")
    html = urlopen(base_url).read()#.decode('cp949','ignore')
    
    soup = BeautifulSoup(html, 'html.parser')
    
    soup = soup.find('select', attrs={'name':'query'})
    
    i = 0
    site = 'naver'
    for ct in soup.findAll('option') :
        i = i + 1
        print(ct.get('value')) 
        keyword = ct.get('value');
        cur.execute("insert into xe_search_history(site, regdate, rank, keyword)values('"+site+"',now(), "+str(i)+",'"+keyword+"')")
    
    conn.commit()
    conn.close()
    time.sleep(60)

# print(soup.prettify())

