##---------------爬蟲本週最新電影
import requests
from bs4 import BeautifulSoup as bs

def get_wb_page(url):
    resp=requests.get(url)
    resp.encoding='UTF-8'
    
    if resp.status_code!=200:
        print("Invaild url: ",url)
        return None
    else:
        return resp.text

def get_movie(dom):
    soup=bs(dom,'html.parser')  
    movie=dict()
    movie_file=soup.find('div',{'class':'release_info_text'})
    movie['movie_CH_name']=movie_file.find('a').text.strip()
    movie['movie_EN_name']=movie_file.find('div',{'class':'en'}).text.strip()
    movie['movie_expectation']=movie_file.find('div',{'class':'leveltext'}).span.text.strip()
    movie['movie_CH_briefIntro']=movie_file.find('div','release_text').span.text.strip()
    movie['mocie_id']=movie_file.find('div').a['href'].split('-')[-1]
    print(movie)

## Tab and Shift+Tab
if __name__=='__main__':
    web_url='https://movies.yahoo.com.tw/movie_thisweek.html'
    page=get_wb_page(web_url)
    get_movie(page)
    