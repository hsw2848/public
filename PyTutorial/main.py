# -*- coding: utf-8 -*-
'''
Created on 2015. 1. 28.

@author: sw.han
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen

import pymysql

conn = pymysql.Connect(host='192.168.1.2', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8');
cur = conn.cursor()

base_url = ("http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard")

html = urlopen(base_url)

soup = BeautifulSoup(html, 'html.parser')

lists = soup.findAll('font',{'class':'list_title'})
 
i = 0
for l in lists:
    if i > 2: 
        l = str(l).replace("<font class=\"list_title\">", "").replace("</font>", "")
#         cur.execute("insert into xe_documents(document_srl, module_srl, category_srl, lang_code, is_notice, title, title_bold, title_color, content, readed_count, voted_count, blamed_count, comment_count, trackback_count, uploaded_count, password, user_id, user_name, nick_name, member_srl, email_address, homepage, tags, extra_vars, regdate, last_update, last_updater, ipaddress, list_order, update_order, allow_trackback, notify_message, status, comment_status)values(nextseq(), 1266, 0, 'ko', 'N', '자동 글쓰기 테스트', 'N', 'N', '<p>테스트</p>', 0, 0, 0, 0, 0, 0, NULL, 'hsw2848', 'admin', '루디먼트', 4, 'swhan.nas@gmail.com', '', NULL, 'N;', '20150922200429', '20150922200429', NULL, '121.168.98.92', -2599, -2599, 'N', 'N', 'PUBLIC', 'ALLOW')")
#         cur.execute("select * from xe_documents")    
        print(l)
        
    
    i = i+1

conn.commit();
conn.close();




