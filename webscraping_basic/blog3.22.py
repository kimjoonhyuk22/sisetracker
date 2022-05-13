from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=1"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
res = requests.get(url,headers=headers)
# print(res)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

blogs=soup.find_all("div",attrs={"class":"desc"})
for blog in blogs:
    title=blog.strong.get_text()
    print(title)