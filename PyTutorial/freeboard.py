# -*- coding: utf-8 -*-
'''
Created on 2015. 1. 28.

@author: sw.han
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen

import pymysql
from test.test_strftime import escapestr


conn = pymysql.Connect(host='save.gonetis.com', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8')
cur = conn.cursor()

cur.execute("select max(seq) from xe_freeboard_seq")
for bbsSeq in cur.fetchall() :
    lastSeq = bbsSeq[0]

print(lastSeq)
 
# base_url = ("http://www.ppomppu.co.kr/zboard/zboard.php?id=freeboard")
base_url = ("http://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=828&no="+str(lastSeq))
html = urlopen(base_url).read().decode('cp949','ignore')

 
soup = BeautifulSoup(html, "html.parser")


exitCode = soup.find('div', {'class':'error2'})
title = str(soup.find('font', {'class':'view_title2'})).replace('<!--DCM_TITLE-->','').replace('<!--/DCM_TITLE-->','').replace('<font class="view_title2">','').replace('</font>','')


if exitCode : #없는 게시물
    #for i in range(1,5) :
    for i in range(1,5) :
        lastSeq = lastSeq + 1
        base_url = ("http://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=828&no="+str(lastSeq))
        html = urlopen(base_url)
        soup = BeautifulSoup(html, 'html.parser')
        exitCode = soup.find('div', {'class':'error2'})
        
        title = str(soup.find('font', {'class':'view_title2'})).replace('<!--DCM_TITLE-->','').replace('<!--/DCM_TITLE-->','').replace('<font class="view_title2">','').replace('</font>','')
        if exitCode and i == 5 :
            exit()
        elif exitCode :
            continue
        elif title.find('자동폭파된 게시물입니다.') > -1 :
            continue
        else :
            break


elif title.find('자동폭파된 게시물입니다.') > -1 :        
    for i in range(1,5) :
        lastSeq = lastSeq + 1
        base_url = ("http://www.ppomppu.co.kr/zboard/view.php?id=freeboard&page=1&divpage=828&no="+str(lastSeq))
        html = urlopen(base_url)
        soup = BeautifulSoup(html, 'html.parser')
        exitCode = soup.find('div', {'class':'error2'})
        
        title = str(soup.find('font', {'class':'view_title2'})).replace('<!--DCM_TITLE-->','').replace('<!--/DCM_TITLE-->','').replace('<font class="view_title2">','').replace('</font>','')
        if exitCode and i == 5 :
            exit()
        elif exitCode :
            continue
        elif title.find('자동폭파된 게시물입니다.') > -1 :
            continue
        else :
            break
else: 
    print('continue')


print(title)

title = '[펌] ' + title
try:
    wr = soup.find('font', {'class':'view_name'}).string
except :
    wr ='익명'
     
print(wr)
contents = soup.findAll('table',{'class':'pic_bg'})
#print(contents[2])
 
# s = BeautifulSoup(str(contents[2]), 'html.parser')
 
#s = s.findAll('td', {'class':'han'})

 
text = str(contents[2])

# for l in s :
#     text = text + str(l)
 
text = text + '<br/><br/>출처  : ' + base_url
print(text)
 
 
cur.execute("select max(seq) seq from xe_sequence")
for seq in cur.fetchall() :
    order = -(seq[0]+1)
     
order =  str(order)
print(order)

# try     :
cur.execute("insert into xe_documents(document_srl, module_srl, category_srl, lang_code, is_notice, title, title_bold, title_color, content, readed_count, voted_count, blamed_count, comment_count, trackback_count, uploaded_count, password, user_id, user_name, nick_name, member_srl, email_address, homepage, tags, extra_vars, regdate, last_update, last_updater, ipaddress, list_order, update_order, allow_trackback, notify_message, status, comment_status)values(nextseq(), 1266, 0, 'ko', 'N', '"+title+"', 'N', 'N', "+text+", 0, 0, 0, 0, 0, 0, 'sha256:0008192:pSKxS3kIZ0fi:NXEWgJSDMhZWg0lv08wAhPLpmzjMC5SV', '', '', '"+wr+"', 0, '', '', NULL, 'N;', DATE_FORMAT(NOW(),'%Y%m%d%H%i%s'), DATE_FORMAT(NOW(),'%Y%m%d%H%i%s'), NULL, '121.168.98.92', '"+order+"', '"+order+"', 'N', 'N', 'PUBLIC', 'ALLOW')")

# except :
#     print()
cur.execute("insert into xe_freeboard_seq(site,bbs,seq)values('ppomppu','freeboard','"+str(lastSeq+1)+"')")
print(lastSeq)
 
conn.commit();
conn.close();




