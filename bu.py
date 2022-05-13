from selenium import webdriver
import pandas as pd
import time
import requests
driver = webdriver.Chrome()

driver.get("https://land.naver.com")

from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"
print("pandas version: ", pd.__version__)
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)

headers = {
    "Connection": "keep-alive",
    "Host": "new.land.naver.com",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2MjMyMzkyMzksImV4cCI6MTYyMzI1MDAzOX0.gdgEApo9bDG5IsSsYDWWeHlAN9LtNh6ejEARMS0FGL8",
    "Referer": "https://new.land.naver.com/complexes/28?ms=37.4836023,127.0543296,16&a=APT:ABYG:JGC&e=RETAIL",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
}

df1=[]
page=1
url = "https://new.land.naver.com/api/articles/complex/28?realEstateType=APT%3AABYG%3AJGC&tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={}&complexNo=28&buildingNos=&areaNos=&type=list&order=rank".format('page')

for i in range(2):
    res = requests.get(url, headers=headers)
    time.sleep(1)
    data_dict = res.json()
    df=pd.DataFrame(data_dict['articleList'])
    size=len(df['dealOrWarrantPrc'])
    # df1+=df['dealOrWarrantPrc']
    print(df['dealOrWarrantPrc'])
    if size !=20:
        break
    page+=1