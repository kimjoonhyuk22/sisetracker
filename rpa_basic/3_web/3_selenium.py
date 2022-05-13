#크롬에서 f12해서 마우스 클릭하거나, 좌클릭 검사 개발자도구하면 원하는 곳의 태크 검색가능하다
# 그리고 태그에서 오른쪽 버튼 누르면 엑스패스 가지고 올수 있다.
# 환경설적은 pip install selenium 하면됨, 그리고 셀레리움 통해서 웹을 컨트롤할대
# 그 브라우져의 그 브라우져의 드라이버를 찾아서 설치해야된다. 크롬 버전을 확인해서 설치해야한다
# 버전은 항상 버전이 같아야하기때문에 업데이트해야줘야한다.chrome://settings/help 이라고 검색한다. 점3개 누르고 도움말 크롬정보 누른다.
# 그리고 chromedrive 검색하여 들어가서 버전에 맞게 다운받는다. 
# 그리고 그 파일을 파이썬 워크스페이스에 붙여놔야한다. 

from selenium import webdriver  # 모듈가져오고.5시35분18초

#browser = webdriver.Chrome('./chromedriver.exe')
browser = webdriver.Chrome()

# 네이버 이동
browser.get('http://naver.com')

# # 카페 메뉴 찾기
# elem = browser.find_element_by_link_text('카페')

# # 속성 가져오기
# elem.get_attribute('href')
# elem.get_attribute('class')

# # 클릭
# elem.click()

# # 뒤로 가기
# browser.back()

# # 앞으로 가기
# browser.forward()

# # 새로고침
# browser.refresh()

# # 뒤로 가기
# browser.back()

# # 검색창 찾기 (개발자 도구 이용)
# elem = browser.find_element_by_id('query')

# # 글자 입력하기
# elem.send_keys('나도코딩')

# # enter 치기
# from selenium.webdriver.common.keys import Keys
# elem.send_keys(Keys.ENTER)

# # a 태그 찾기
# elem = browser.find_element_by_tag_name('a')
# elem.get_attribute('href')

# # a 태그 모두 찾기
elems = browser.find_elements_by_tag_name('a')
for e in elems:
    e.get_attribute('href')

# # 다음으로 이동
# browser.get('http://daum.net')

# # 검색창 찾기
# elem = browser.find_element_by_name('q')

# # 글자 입력하기
# elem.send_keys("나도코딩")

# # 글자 지우기
# elem.clear()

# # 글자 입력하기
# elem.send_keys("나도코딩")

# # 검색 버튼 찾기
# elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')

# # 클릭하기
# elem.click()

# # 스크린샷 찍기
# browser.save_screenshot('daum.png')

# # 페이지 소스 보기
# browser.page_source

# # 브라우저 종료
# browser.close() # 현재 탭 닫기
# browser.quit() # 브라우저 종료하기

# # 참고 URL : https://selenium-python.readthedocs.io/