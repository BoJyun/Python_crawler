import requests
from bs4 import BeautifulSoup as bs

resp=requests.get('https://www.dcard.tw/f')
soup=bs(resp.text,'html5lib')
#print(type(soup))
dcard=dict()
dcard_info=soup.find_all('div','PostList_entry_1rq5Lf')


print(dcard_info)
