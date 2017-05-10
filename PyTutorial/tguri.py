# -*- coding: utf-8 -*-
'''
Created on 2015. 12. 3.

@author: sw.han
'''


from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from builtins import open
import pymysql
from time import sleep


ip = '192.168.1.2'
gap = 0

def getSeq(ip, site, board):
    try:
        conn = pymysql.Connect(host=ip, port=3306, user='root', passwd ='dkelektm1.', db='crawling', charset='utf8')
        cur = conn.cursor()
        
        sql = "select max(num)+1 from tbl_cr_gallery where site = '"+site + "' and board = '" + board +"'"
        print(sql)
        cur.execute(sql)
        
        for item in cur.fetchall() :
            seq = item[0]
    except:
        print('getIndex - db error')
        
    conn.close()
    
    return seq


def insertSeq(ip, site, board, seq, title, url):
    try:
        conn = pymysql.Connect(host=ip, port=3306, user='root', passwd ='dkelektm1.', db='crawling', charset='utf8')
        cur = conn.cursor()
        
        sql = "insert into tbl_cr_gallery(site, board, num, title, path, createtime, createby, updatetime, updateby)value('"+site+"','"+board+"',"+str(seq)+",'"+title+"','"+url+"',now(),'sw2848.han',null,null)"
        print(sql)
        cur.execute(sql)
        conn.commit()
    except:
        print('insertSeq - db error')
        
    conn.close()
    
    return



#board asia
def tguri(index, board):
    banner = 'http://avsarang2.com/page/ad2.php?mb_id=&type=1'
    
    #index = 4264
    domain = 'http://avsarang2.com/bbs'
    #http://avsarang2.com/bbs/download.php?bo_table=asia&wr_id=4266&no=0
    url = 'http://avsarang2.com/bbs/board.php?bo_table='+board+'&wr_id='+str(index)
    cookie = '__cfduid=d6aa39df9e450cfbad53b54e450e51ca11448978519; f33d2ed86bd82d4c22123c9da444d8ab=MTQ0ODk3ODQ3OQ%3D%3D; 96b28b766b7e0699aa91c9ff3d890663=aHR0cDovL3RndXJpcy5jb20v; 2a0d2363701f23f8a75028924a3af643=MTIxLjE2OC45OC45Mg%3D%3D; _ga=GA1.1.1251343212.1448978521; uchat_name=%25uC190%25uB2D8%252880bee%2529; PHPSESSID=0li24jm5ptjddu11nmcoh1gcd0; _gat=1' 
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'})
    req.add_header('Cookie', cookie)
    
    banreq = Request(banner, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'})
    banreq.add_header('Cookie', cookie)
    urlopen(banreq)
    
    link = 'http://avsarang2.com/bbs/link.php?bo_table=link&wr_id=18&no=1'
    
    banreq = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'})
    banreq.add_header('Cookie', cookie)
    urlopen(banreq)
    
    response = urlopen(req).read()
    
    global gap    
    if gap > 10 :
        gap = 0
        return 
    elif response.decode('utf-8').find('삭제') > -1  :
        gap += 1
        tguri(index+1, board)
        return    
    
    bs = BeautifulSoup(response, 'html.parser')
    bs = bs.find_all('a')
    
    for item in bs :
        if str(item.get('href')).find('javascript:file_download') > -1 :
            downloadurl = str(item.get('href')).split('\'')[1].lstrip('.')
            print(downloadurl)
     
    print(cookie)
     
    if downloadurl : 
        req2 = Request(domain+downloadurl)
        print(domain+downloadurl)
        req2.add_header('Cookie', cookie)
        req2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
           
        response2 = urlopen(req2)
          
        data = response2.read()
          
        name = str(index)
        f = open('d:/torrent/'+name+'.torrent', 'wb')
        f.write(data)
        f.close()
        insertSeq(ip,'tguri', board, index, '한국/중국',domain+downloadurl)
        
    else:
        print('end'+name+'no data')        
      
    print('end'+name)

    return    


#torrent_movie_kor 한국영화
def tosarang(index, board):
    
    #index = 12897
    url = 'http://www.tosarang2.net/bbs/board.php?bo_table='+board+'&wr_id='+str(index)
    # url2 = 'http://www.tosarang2.net/bbs/download.php?bo_table=torrent_movie_kor&wr_id='+str(index)+'&no=0'
    cookie = 'vtSclruNo=35; jPath=dir; vtSclruAd=4; vtSclruNo=28; e1192aefb64683cc97abb83c71057733=dG9ycmVudF9tb3ZpZV9rb3I%3D; PHPSESSID=ec6biugpa9v5b2pf1stbp2l1k1; jPath=dir; bnadc=ADC; vtSclruAd=2; __cfduid=db81f41b93cdbe4ca5f1685f4f7e0d5b91442723085; _ga=GA1.2.2035832014.1442723086; _gat=1' 
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'})
    req.add_header('Cookie','vtSclruNo=35; jPath=dir; vtSclruAd=4; vtSclruNo=28; e1192aefb64683cc97abb83c71057733=dG9ycmVudF9tb3ZpZV9rb3I%3D; PHPSESSID=ec6biugpa9v5b2pf1stbp2l1k1; jPath=dir; bnadc=ADC; vtSclruAd=2; __cfduid=db81f41b93cdbe4ca5f1685f4f7e0d5b91442723085; _ga=GA1.2.2035832014.1442723086; _gat=1')
    
    response = urlopen(req).read()
    
    bs = BeautifulSoup(response, 'html.parser')
    stitle = bs.find_all('div')
    for item in stitle:
        if str(item).find('bo_v_title') > -1 :
            title = str(item.h1)
        
        if str(item).find('글이 존재하지 않습니다') > -1 :
            print("글이 존재하지 않습니다")
            return
    
    print(title)
    bs = bs.find_all('a')
    
    for item in bs :
        if item.get('href').find('download.php?') > -1 :
            url2 = item.get('href')
            print(url2)
            
    
    print(cookie)
    if url2 : 
        req2 = Request(url2)
        req2.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
        req2.add_header('Accept-Encoding', 'gzip, deflate, sdch')
        req2.add_header('Accept-Language', 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4')
        req2.add_header('Connection','keep-alive')
        req2.add_header('Cookie', cookie)
        req2.add_header('Host', 'www.tosarang2.net')
        req2.add_header('Referer', url)
        req2.add_header('Upgrade-Insecure-Requests', '1')
        req2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36')
          
        response2 = urlopen(req2)
         
        data = response2.read()
         
        name = str(index)
        f = open('d:/torrent/'+name+'.torrent', 'wb')
        f.write(data)
        f.close()
        
        insertSeq('tosarang', board, index, "한국영화", url2)
    else:
        print('end'+name+'no data')        
     
    print('end'+name)

    return

while 1 : 
    try : 
        seq = getSeq(ip,'tguri', 'asia')
        tguri(seq, 'asia')
        sleep(60)
    except :
        sleep(60)
        print('tguri except')




    