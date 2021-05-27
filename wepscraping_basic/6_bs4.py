import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) soup 객체에서 처음 발견되는 a element 출력
#print(soup.a.attrs) # a element 의 속성 정보를 출력
#print(soup.a["href"])# a element 의 href 속성 '값' 정보를 출력

soup.find("a",)