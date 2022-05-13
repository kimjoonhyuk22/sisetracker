# -*- coding: utf-8 -*-

import requests
import json
import logging

URL = "https://new.land.naver.com/api/complexes/single-markers/2.0?cortarNo=1147010200&zoom=18&priceType=RETAIL&markerId=659&markerType=COMPLEX&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AABYG%3AJGC&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=95.9&areaMax=125.6&oldBuildYears&recentlyBuildYears&minHouseHoldCount=300&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=126.8637504&rightLon=126.8706168&topLat=37.5293148&bottomLat=37.5265495"

param = {
    'hscpNo': '19672',
    'tradTpCd': 'A1',
    'order': 'date_',
    'showR0': 'N',
}

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36",
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

resp = requests.get(URL, params=param, headers=header)
data = json.loads(resp.text)
print(data)

# while True:
#     page += 1
#     param['page'] = page

#     resp = requests.get(URL, params=param, headers=header)
#     if resp.status_code != 200:
#         logging.error('invalid status: %d' % resp.status_code)
#         break

#     data = json.loads(resp.text)
#     result = data['result']
#     if result is None:
#         logging.error('no result')
#         break
    
#     for item in result['list']:
#         if float(item['spc2']) < 80 or float(item['spc2']) > 85:
#             continue
#         logging.info('[%s] %s %s층 %s만원' % (item['tradTpNm'], item['bildNm'], item['flrInfo'], item['prcInfo']))
    
#     if result['moreDataYn'] == 'N':
#         break

