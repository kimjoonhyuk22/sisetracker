# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# import pandas as pd
# pd.set_option('display.float_format', lambda x: '%.3f' % x)    # DataFrame 숫자데이터가 소수점 셋째자리까지 나오도록 설정
# pd.set_option('max_columns', None)  # DataFrame에서 모든 컬럼을 다 볼 수 있게 설정

import requests
import bs4

from datetime import datetime
import requests

#------------------------------------
# 학교 교직원인사말 퍼오기
# res = requests.get("https://dpsc.djsch.kr/sub/info.do?m=0101&s=dmis") #res는 리스폰스의 약자다.

# soup = bs4.BeautifulSoup(res.text,"lxml")

# td_elements=soup.select("td > p > span")
# print(type(td_elements))
# for i in td_elements:
#     print(i.text)

# ------------------------------------------
#네이버 뉴스 퍼오기
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# res = requests.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105", headers=headers) #res는 리스폰스의 약자다.
# soup = bs4.BeautifulSoup(res.text,"lxml")

# td_elements=soup.select("div.classfy.sd > ul.list_txt > li > a")# > a.list_tit nclicks('rig.renws2')
# print(type(td_elements))
# print(len(td_elements))
# for i in td_elements:
#     print(i.text)

#에러 : ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')) >> 봇을허용하지 않는다.헤더추가하니됨!


#####-네이버 카페 안됨####
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# res = requests.get("https://cafe.naver.com/rhocloud", headers=headers) #res는 리스폰스의 약자다.
# soup = bs4.BeautifulSoup(res.text,"lxml")

# td_elements=soup.select("tr > td.td_article > div.board-list > div.inner_list > a.article")
# print(type(td_elements))
# print(len(td_elements))
# for i in td_elements:
#     print(i.text)

#

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}
# res = requests.get("https://cafe.naver.com/rhocloud", headers=headers) #res는 리스폰스의 약자다.
# soup = bs4.BeautifulSoup(res.text,"lxml")

# td_elements=soup.select("g.highcharts-label > g.highcharts-label")
# print(type(td_elements))
# print(len(td_elements))
# for i in td_elements:
#     print(i.text)

import pandas as pd

my_headers = {
    "referer": "https://finance.naver.com/item/sise_day.nhn?code=005930&page=3",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
}

page_number = 1
url = "https://aptgin.com/home/gin05/gin0501"
res = requests.get(url=url, headers=my_headers)
# print(type(pd.read_html(res.text)))

df = pd.read_html(res.text)[0]
df = df.dropna()
df.head()
