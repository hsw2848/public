
# -*- coding: utf-8 -*-
'''
Created on 2015. 1. 28.
네이버 쇼핑
@author: sw.han
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen

import time
import pymysql
from urllib.parse import quote
from random import randint

while 1 :
    try:
        conn = pymysql.Connect(host='192.168.1.2', port=3306, user='root', passwd ='dkelektm1.', db='xe', charset='utf8')
        cur = conn.cursor()

        base_url = ("http://shopping.naver.com/best100v2/main.nhn")
        html = urlopen(base_url).read()#.decode('cp949','ignore')
         
        searchList = BeautifulSoup(html, 'html.parser')
         
        searchList = searchList.find('ul', {'id':'popular_srch_lst'} )
         
        searchList = searchList.findAll('a', {'class':'_popular_srch_lst_li'})
         
        for l in searchList:
            
            text = quote(l.get('title'))
            print(text)
            #http://shopping.naver.com/search/all_search.nhn?query=%EB%A7%A8%ED%88%AC%EB%A7%A8&pagingIndex=2&pagingSize=40&productSet=total&viewType=list&sort=rel&searchBy=none&frm=NVSHPAG
            
            base_url = ("http://shopping.naver.com/search/all_search.nhn?query="+text+"&cat_id=&frm=NVSHATC&nlu=true&=&=&=&=")
            html = urlopen(base_url).read()#.decode('cp949','ignore')     
            
            soup = BeautifulSoup(html, 'html.parser')

            soup = soup.find('ul', {'class':'goods_list'})
            
            titList = soup.findAll('a', {'class':'tit'})
            priceList = soup.findAll('span', {'class':'num _price_reload'})
            imgList = soup.findAll('img', {'class':'_productLazyImg'})
            detailList = soup.findAll('span', {'class':'detail'})
            print(len(titList), len(priceList), len(imgList), len(detailList))
            
             
            #for i in range(len(titList)) :
            i =  randint(0, len(priceList)-1)
            title = titList[i].get('title')
            try : 
                price = priceList[i].string
            except :
                price = 'error'
            img = "<p><img src=\"" + str(imgList[i].get('data-original')).replace('?type=f140','') +"\"/></p><br/><br/>"
            link = titList[i].get('href')
            
            if(link.find('http')<0):
                link = 'http://shopping.naver.com' + link
            try :
                detail = str(detailList[i]) + '<br/><br/>'
            except :
                detail = '<br/>'
            
            print(title, price,detail, img, link)
            cur.execute("select max(seq) seq from xe_sequence")
            for seq in cur.fetchall() :
                order = -(seq[0]+1)
                 
            order =  str(order)
            print(order)
            cur.execute("insert into xe_documents(document_srl, module_srl, category_srl, lang_code, is_notice, title, title_bold, title_color, content, readed_count, voted_count, blamed_count, comment_count, trackback_count, uploaded_count, password, user_id, user_name, nick_name, member_srl, email_address, homepage, tags, extra_vars, regdate, last_update, last_updater, ipaddress, list_order, update_order, allow_trackback, notify_message, status, comment_status)values(nextseq(), 2444, 0, 'ko', 'N', '"+title+"("+price+")', 'N', 'N', '"+img+detail+link+"', 0, 0, 0, 0, 0, 0, 'sha256:0008192:pSKxS3kIZ0fi:NXEWgJSDMhZWg0lv08wAhPLpmzjMC5SV', '', 'admin', '루디먼트', 4, 'swhan.nas@gmail.com', '', NULL, 'N;', DATE_FORMAT(NOW(),'%Y%m%d%H%i%s'), DATE_FORMAT(NOW(),'%Y%m%d%H%i%s'), NULL, '121.168.98.92', '"+order+"', '"+order+"', 'N', 'N', 'PUBLIC', 'ALLOW')")
            conn.commit()
            time.sleep(60)

        conn.close()
    except:
        conn.close()

    

    #print(soup.prettify())

