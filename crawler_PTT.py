import requests
import re
from bs4 import BeautifulSoup as bs

API_KEY='ea7d4b89265c71a0fe54ef227a2ad1ac'

def get_web(url):
    resp=requests.get(url,cookies={'over18':'1'}) 

    if resp.status_code!=200:
        print('Invaild url:',resp.url)
        return None
    else:
        return resp.text
    
def get_ptt_info(dom):    
    soup=bs(dom,'html5lib')
    article_info=soup.find_all('div','r-ent')
    
    article_file=[]
    for i in article_info:
        if i.find('a'):
#            article=[]
            title=i.find('a').text
            href=i.find('a')['href']
            author=i.find('div','author').text
            article_file.append({'title':title,'href':href,'author':author})
#        article_file.append(article)
    
    return article_file

def get_ip(dom):
    pattern='來自: \d+\.\d+\.\d+\.\d+'
    match=re.search(pattern,dom)   # 可打print(type(match)),match是類別
    if match:
        return match.group(0).replace('來自: ','') #group(0)表示搜尋到的第一筆資料
    else :
        return None

def get_country(ip):
    if ip:
        url='http://api.ipstack.com/{}?access_key={}'.format(ip,API_KEY)
        data=requests.get(url).json()
        country_name=data['country_name'] if data['country_name'] else None
        return country_name
    return None
        
if __name__=='__main__':
    PTT_url='https://www.ptt.cc'
    ptt_web=get_web(PTT_url+'/bbs/Gossiping/index.html')
    ptt_article_file= get_ptt_info(ptt_web)
#    article_file=ptt_article_file[0]
#    article_ip_web=get_web(PTT_url+article_file['href'])
#    ptt_ip=get_ip(article_ip_web)
#    country_ip=get_country(ptt_ip)    
    for article_file in ptt_article_file:
        article_ip_web=get_web(PTT_url+article_file['href'])
        ptt_ip=get_ip(article_ip_web)
        country_ip=get_country(ptt_ip)
        print(article_file,'ip country is '+country_ip)  #dict andd str 不能同時print所以要','
#    for i in ptt_article_file:
#        print(i)