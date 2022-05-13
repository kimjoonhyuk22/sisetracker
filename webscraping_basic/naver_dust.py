from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from requests import Response

html: Response = requests.get('https://search.naver.com/search.naver?query=날씨')
pprint(html.text)