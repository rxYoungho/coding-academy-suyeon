import requests 
from bs4 import BeautifulSoup


url = "https://www.coupang.com/np/search?component=&q=%EB%B9%A8%EB%8C%80"
response = requests.get(url)
print(response)
if response.status_code == 200:
    html = response.text 
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.select_one('ul.productList')
    print(ul)
    # titles = ul.select('li > dl > dt > a')
    # for title in titles:
    #     print(title.get_text())

else:
    print(response.status_code)

# params = {
#     'pageNo':1,
#     'rangeType':'ALL',
#     'orderBy':'recentData',
#     'keyword':'파이썬'
# }

# response = requests.get('https://section.blog.naver.com/Search/Post.nhn', params=params)

# print(response.status_code)
# print(response.url)