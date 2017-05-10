
# -*- coding: utf-8 -*-
'''
Created on 2015. 1. 28.
다음 실시간 검색어
@author: sw.han
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

import pymysql
import time

while 1:
        
    conn = pymysql.Connect(host='192.168.1.2', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8')
    cur = conn.cursor()
    
    base_url = ("http://www.daum.net/")
    html = urlopen(base_url).read()#.decode('cp949','ignore')
    
    soup = BeautifulSoup(html, 'html.parser')
    
    soup = soup.find('ol', attrs={'class':'list_issue #searchrank'})
    i = 0
    site = 'daum'
    for item in soup.findAll('a', {'class':'ellipsis_g', 'tabindex':'-1'}) :
        i = i + 1
        if( item.strong == None):
            print(str.strip(item.string))
            keyword = str.strip(item.string)
        
        else:
            print(str.strip(item.strong.string))
            keyword = str.strip(item.strong.string)
            
        cur.execute("insert into xe_search_history(site, regdate, rank, keyword)values('"+site+"',now(), "+str(i)+",'"+keyword+"')")
        conn.commit()
    
    conn.close()
    time.sleep(60)        

