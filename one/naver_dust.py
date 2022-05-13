from bs4 import BeautifulSoup
from pprint import pprint
import requests
import json

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://www.naver.com/")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

# pprint(soup)
#요일별 웹툰영역 추출하기
data1_list=soup.findAll('strong',{'class':'content_title'})
pprint(data1_list.text)

# #전체 웹툰 리스트
# li_list = []
# for data1 in data1_list:
#     #제목+썸내일 영역 추출
#     li_list.extend(data1.findAll('li')) #해당 부분을 찾아 li_list와 병합
# # pprint(li_list)

# #각각 썸네일과 제목 추출하기
# for li in li_list:
#     img = li.find('img')
#     title = img['title']
#     img_src = img['src']
#     print(title,img_src)