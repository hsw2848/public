# -*- coding: utf-8 -*-
'''
Created on 2015. 9. 27.

@author: swhan
'''

import pymysql
import time

while 1 :
    conn = pymysql.Connect(host='save.gonetis.com', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8')
    cur = conn.cursor()
    
#     cur.execute("select distinct ipaddress from xe_documents where document_srl and title like '?%'")
#     for col in cur.fetchall() :
#         ip = col[0]
#         print(ip)
#         cur.execute("insert into xe_spamfilter_denied_ip(ipaddress,description,regdate)values('"+ip+"','spam',now());")
#     
#         
#     cur.execute("delete from xe_documents where document_srl and title like '?%'")
    

    cur.execute("select distinct ipaddress from xe_documents where 1=1 and comment_status = 'DENY'")
    for col in cur.fetchall() :
        ip = col[0]
        print(ip)
        try :
            cur.execute("insert into xe_spamfilter_denied_ip(ipaddress,description,regdate)values('"+ip+"','spam',now());")
        except :
            continue
        
    cur.execute("delete from xe_documents where 1=1 and comment_status = 'DENY'")
        
    conn.commit()
    conn.close()
    
    time.sleep(60)