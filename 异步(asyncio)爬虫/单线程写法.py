from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time

start = time.perf_counter()
ua = UserAgent()
a=ua.random  #随机的一个user-agent
headers={"User-Agent": a}

url = 'https://movie.douban.com/cinema/later/beijing/'
r = requests.get(url,headers=headers)
demo = r.text  # 服务器返回响应
soup = BeautifulSoup(demo, "lxml")

all_movies = soup.find('div', id="showing-soon")
for each_movie in all_movies.find_all('div', class_="item"):
    all_a_tag = each_movie.find_all('a')
    all_li_tab = each_movie.find_all('li')

    movie_name = all_a_tag[1].string
    url_to_fetch = all_a_tag[1]['href']
    movie_date = all_li_tab[0].string

    response_item = requests.get(url_to_fetch,headers=headers).content
    soup_item = BeautifulSoup(response_item, "lxml")
    img_tag = soup_item.find('img').get('src')  #字典格式，按字典取值，也可以soup_item.find('img')['src']

    print('{} {} {}'.format(movie_name, movie_date,img_tag))

end = time.perf_counter()
print(end - start)