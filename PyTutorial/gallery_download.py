# -*- coding: utf-8 -*-

'''
Created on 2015. 12. 5.

@author: 한성우
'''
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def slr(url):
    
    cookie = '__cfduid=d6aa39df9e450cfbad53b54e450e51ca11448978519; f33d2ed86bd82d4c22123c9da444d8ab=MTQ0ODk3ODQ3OQ%3D%3D; 96b28b766b7e0699aa91c9ff3d890663=aHR0cDovL3RndXJpcy5jb20v; 2a0d2363701f23f8a75028924a3af643=MTIxLjE2OC45OC45Mg%3D%3D; _ga=GA1.1.1251343212.1448978521; uchat_name=%25uC190%25uB2D8%252880bee%2529; PHPSESSID=0li24jm5ptjddu11nmcoh1gcd0; _gat=1' 
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'})
    req.add_header('Cookie', cookie)
    req.add_header('Referer', 'http://www.slrclub.com/bbs/zboard.php?id=work_gallery')
    req.add_header('host', '121.69.37.72')
    
    response = urlopen(req).read()
    
    title = BeautifulSoup(response, 'html.parser').find('tr', {'class':'first_part'})
    for t in title.td.strings :
        title = str(t).strip()
        break;
    print(title) 
    
    
    bs = BeautifulSoup(response, 'html.parser')
    bs = bs.find_all('div',{'id':'userct'})
    
    for item in bs :
#         if str(item).find('id=\"userct\"') > -1 :
        url = str(item.img.get('src'))
        print(url)
        
    if url :    
        req2 = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'})
        req2.add_header('Cookie', cookie)
        req2.add_header('Referer', 'http://www.slrclub.com/bbs/zboard.php?id=work_gallery')
        req2.add_header('Host', '121.69.37.72')
        
        pic = urlopen(req2).read()
    
        f = open('d:/torrent/'+title+'.jpg', 'wb')
        f.write(pic)
        f.close()
    
    print('end')
    
    return

#1144505
for i in range(400000,1144505):
    try:
        slr('http://www.slrclub.com/bbs/vx2.php?id=work_gallery&no='+str(i))
    except:
        print('error')
    
# slr('http://www.slrclub.com/bbs/vx2.php?id=work_gallery&no=1144505')
