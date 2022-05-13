
# 1. 사전 세팅 필요사항들

# [selenium, tqdm 모듈 설치]

# 해당 방법을 하기 위해서 아래의 모듈을 추가로 설치를 했다.

# selenium, tqdm

# 설치방법은 cmd 창에서 하는 방식이 있는데, 정석은 아나콘다 프롬프트에서 관리자권한으로 실행 후 나오는 도스창같은 것에서, pip install '각각의 모듈명'을 넣고 엔터를 치면 설치가 된다.

# pip install selenium

# pip install tqmd


# # [크롬드라이버 설치]

# # 그리고 크롬드라이버도 설치를 했다.

# # 자동으로 설치를 할 수 있는 방법도 있는데, 우선은 경로 등을 지정하는 방법으로 진행하는 방식으로 배웠다.

# # 크롬드라이버를 설치하기 전에, 크롬의 버전을 먼저 확인한다.

# # 도움말 > 크롬정보를 눌르면 아래와 같은 버전을 확인할 수 있다.


# # ​

# # 버전을 확인했으면, 구글에서 크롬드라이버를 검색 후 버전에 맞는 것을 다운로드한다.

# # 그리고, 다운로드한 파일을 파이썬을 실행하는 경로의 폴더에 넣어준다.

# # ​

# # 2. 파이썬에서 제목과 URL 엑셀로 크롤링하기

# # 파이썬에서 크롤링할 때는 크롬으로 네이버 창을 띄우고, 실제 검색을 하고 제목과 URL을 가져온다.

# # ​

# #Step 0. 필요한 모듈과 라이브러리를 로딩

import sys # 시스템

import os # 시스템



import pandas as pd # 판다스 : 데이터분석 라이브러리

import numpy as np # 넘파이 : 숫자, 행렬 데이터 라이브러리



from bs4 import BeautifulSoup # html 데이터를 전처리

from selenium import webdriver # 웹 브라우저 자동화

import time # 서버와 통신할 때 중간중간 시간 지연. 보통은 1초

from tqdm import tqdm_notebook # for문 돌릴 때 진행상황을 %게이지로 알려준다.



# # 워닝 무시

# import warnings

# warnings.filterwarnings('ignore')



# # [검색어 입력]

# query_txt = input('1.크롤링할 키워드는 무엇입니까?: ')

# # 앞서 배웠던 input()함수를 활용해 검색하고자 하는 키워드를 입력한다.

# # ​

# #Step 1. 크롬 웹브라우저 실행

# path = "chromedriver.exe" 

# # 윈도우는 "chromedriver.exe", 이를 위해 파이썬이 실행되는 폴더 안에 크롬드라이버를 넣어야 한다. 

# #    만약, 그렇지 않으면 경로를 넣어주고 앞에 r을 붙여주어야 되는 것 같다.   

# #    (r'C:\Users\BDH\Desktop\Untitled Folder/chromedriver.exe')

# # 맥은 절대경로 (크롬드라이버 우클릭 후 경로 복사)

# driver = webdriver.Chrome(path)

# #webdriver.Chrome('크롬드라이버경로') => 크롬 창 Open


# # 사이트 주소는 네이버

# driver.get('http://naver.com')

# time.sleep(2) # 2초간 정지



# # => 크롬 브라우저가 열리고 네이버 메인 화면이 오픈된다.

# # ​

# # Step 2. 네이버 검색창에 "검색어" 검색

# element = driver.find_element_by_id("query")  # 'element'변수를 id가 "query"로 되있는 검색창 부분으로 지정

# element.send_keys(query_txt) # query_txt는 위에서 입력한 키워드

# element.submit()

# time.sleep(1)



#  # 아래 개발자도구에서 보면 검색창의 ID는 'query'인 것을 확인할 수 있다.


# # => 네이버 검색창에 위에서 입력한 검색어가 입력되고 검색되어진 화면이 보여진다.

# # ​

# # Step 3. 크롤링 영역 지정 및 검색 옵션 설정

# # > 'VIEW' 클릭

# driver.find_element_by_link_text("VIEW").click( )    # 링크가 있는 텍스트 중 view를 클릭

# time.sleep(1)

# # > '블로그' 클릭

# driver.find_element_by_link_text("블로그").click( )

# time.sleep(1)

# # > '옵션' 클릭

# driver.find_element_by_link_text("옵션").click( )

# time.sleep(1)



# # 검색옵션 확인

# item_li = driver.find_elements_by_css_selector('.option .txt')    # option 클래스의 자손 txt 클래스



# for i in range(0, len(item_li)):                       # 0부터 item_li의 갯수만큼 반복하고

#     print(item_li[i].text)                                    # item_li[i]를 텍스트로 출력

# # => 아래의 검색 옵션의 선택이 가능한 13개가 리스트로 출력이 된다.


# # 검색옵션 설정 > 기간 '3개월' 클릭 예시

# item_li[10].click()    # item_li의 13가지 요소 중 10번째 해당하는 값(0부터 시작)

# # 1주로 설정한다면, [10] 을 [8]로 수정하면 된다.


# # Step 4. 크롤링할 페이지 영역 스크롤하기

# # 스크롤을 밑으로 내려주는 함수

# def scroll_down(driver):

#     driver.execute_script("window.scrollTo(0, 19431049)")

#     time.sleep(1)

# # 스크롤할 횟수 설정 및 실행

# n = 5

# i = 0

# while i < n:

#     scroll_down(driver)

#     i = i+1


# # Step 5. 크롤링 시작

# # 블로그 url과 타이틀 리스트 생성하기

# url_list = []

# title_list = []

# # URL_raw 크롤링 시작

# articles = ".api_txt_lines.total_tit"

# article_raw = driver.find_elements_by_css_selector(articles)


# # 크롤링한 url 정제 시작

# for article in article_raw:

#     url = article.get_attribute('href')

#     url_list.append(url)

# time.sleep(1)

# # 제목 정제 시작

# for article in article_raw:

#     title = article.text

#     title_list.append(title)


# print("")

# print('url갯수: ', len(url_list))

# print('title갯수: ', len(title_list))

# # # 수집된 url, 제목 확인

# # URL 확인 : url_list

# # 제목 확인 : title_list


# # Step 6. 크롤링된 데이터 저장하기

# # 수집된 url_list, title_list로 판다스 데이터프레임 만들기

# df = pd.DataFrame({'url':url_list, 'title':title_list})

# # 저장하기

# df.to_excel("blog_url.xlsx", encoding='utf-8-sig')

#    # df.to_csv("blog_url.csv")

#    # 한글 문서의 경우, encoding 부분을 넣어 깨지지 않게 만들어준다.

# # ​
# # [출처] [크롤링] 네이버 블로그 크롤링하기 - 1|작성자 호룡핸리더


# 3. 블로그 URL을 활용해 블로그 내용 크롤링하기

# Step 1. URL 리스트 불러오기

url_load = pd.read_excel("blog_url.xlsx")              # 앞서, 저장한 파일의 경로를 가져온다.

url_load = url_load.drop("Unnamed: 0", axis=1) # 불필요한 칼럼 삭제


num_list = len(url_load)

print(num_list)

url_load


# Step 2. 리스트에서 하나씩 반복하여 데이터를 수집하기

# 전체 크롤링할 데이터를 담을 그릇 만들기

dict = {}          

# 수집할 글 갯수 정하기

number = 20 

# 수집한 URL 반복하여 데이터 수집

for i in tqdm notebook(range(0, number)):      # 0번부터 위에서 지정한 number까지 반복

    # 1_글 띄우기

    url = url_load['url'][i]                                          # 위에서 불러온 url_load에서 url 컬럼의 i번째 값(url)

    path = "chromedriver.exe"

    driver = webdriver.Chrome(path)            

    driver.get(url)                                                       # 글 띄우기

    # 2_크롤링

    try :

        # iframe 접근

        driver.switch_to.frame('mainFrame')

        # 개별 블로그별 내용을 담을 딕셔너리 생성

        target_info = {}

        # 제목 크롤링 시작

        overlays = ".se-module.se-module-text.se-title-text"   # F12 개발자도구에서 확인(아래 참고)

        tit = driver.find_element_by_css_selector(overlays)     # tlt에 위의 경로에 대한 내용을 가져온다.

        title = tit.text                                                                          # text로 가져오는 것을 title로 지정한다.


# F12를 누르고, 제목 영역을 지정하여 나오는 class 부분을 가져온다.

# class이기 때문에, 맨 앞에 .을 붙여주고, 공백 부분에는 .을 찍어준다.

# tit는 아래과 같은 형태로 보여지며, tit에 .text를 넣어주면 텍스트로 내용을 보여주게 된다.

# <selenium.webdriver.remote.webelement.WebElement (session="bcfedc64274eee6490c91c3601b6658b", element="78b3102f-d9c2-4436-bfe9-c2787a4cc938")>

# 같은 방식으로 나머지 요소들도 가져온다.

# ​

        # 글쓴이 크롤링 시작

        overlays = ".nick" 

        nick = driver.find_element_by_css_selector(overlays) # nickname

        nickname = nick.text

        # 날짜 크롤링

        overlays = ".se_publishDate.pcol2" 

        date = driver.find_element_by_css_selector(overlays) # datetime

        datetime = date.text

        # 내용 크롤링 시작

        overlays = ".se-component.se-text.se-l-default"    

        contents = driver.find_elements_by_css_selector(overlays)

        # 위의 값들은 본문에서 한개씩만 가져오면 되기 때문에 element로 단수형인데, 내용의 경우 각 문단을 

        #    다 가져와야하기 때문에 elements 복수형으로 써준다.

        # contents 역시 위의 tit에서 보여지는 것과 같은 형태로 여러개가 보여진다. 이 때문에 contents에서 

        #    텍스트 형태로 내용을 변경해줘야 한다.

        content_list = []  

        for content in contents:                           # contents의 요소 하나씩을 반복하고 이를 content라고 한다.

            content_list.append(content.text)    # content_list안에 content를 텍스트로 가져온 것을 차례대로

                                                                                #   가져온다.

        content_str = ' '.join(content_list)         # content_list의 각 문장 사이를 합치고 공백으로 구분한다.


        # 각 요소를 하나의 target_info 딕셔너리에 담기

        target_info['title'] = title

        target_info['nickname'] = nickname

        target_info['datetime'] = datetime

        target_info['content'] = content_str


        # 각각의 글을 dict 딕셔너리에 차례로 담기

        dict[i] = target_info

        time.sleep(1)

        # 크롤링 성공 이후, 창 닫기

        print(i, title)

        driver.close() 


    # 3_예외 처리

    except:

        driver.close()

        time.sleep(1)

        continue

print('수집한 글 갯수: ', len(dict))

print(dict)


# Step 3. 수집된 내용을 파일로 만들어내기

# 판다스로 데이터 프레임 만들기

import pandas as pd

result_df = pd.DataFrame.from_dict(dict, 'index')   # index를 넣지않으면 컬럼 기준으로 데이터프레임을 만든다.

result_df

# 엑셀로 저장하기

result_df.to_excel("blog_content.xlsx", encoding='utf-8-sig')

# ​
# [출처] [크롤링] 네이버 블로그 크롤링하기 - 2|작성자 호룡핸리더