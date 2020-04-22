import requests
from bs4 import BeautifulSoup as bs

def get_web_page(url):
    headers={'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64)'
                              'AppleWebKit/537.36(KHTML, like Gecko)'
                              'Chrome/66.0.3359.181 Safari/537.36'}
    resp = requests.get(url=url,headers=headers)

    if resp.status_code!=200:
        print('Invaild url',url)
        return None
    else:
        return resp.text

def get_web_Info(dom):
    soup=bs(dom,'html5lib')
    stock=dict()
    sections=soup.find_all('g-card-section')
    #https://stackoverflow.com/questions/44620432/beautifulsoup-cannot-locate-table-with-specific-class
    
    stock['name']=sections[1].find('div',{'class':'oPhL2e'}).text.strip()
    spans=sections[1].find_all('span',recursive=False)[0].find_all('span')
    stock['current_price']=spans[0].text.strip()
    
    for table in sections[3].find_all('table'):
        for tr in table.find_all('tr')[:3]:
            label=tr.find_all('td')[0].text.strip()
            value=tr.find_all('td')[1].text.strip()
            stock[label]=value
    return stock
        
if __name__=='__main__':
    web_url='https://www.google.com/search?q=TPE:2330'
    page_info=get_web_page(web_url)

    if page_info:
        stock_info=get_web_Info(page_info)
        for i,j in stock_info.items():   #字典的for迴圈用法
            print(i+':'+j)

    