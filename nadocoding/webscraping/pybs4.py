import requests
from bs4 import BeautifulSoup

####  기본 사용법  ##################################################
# url = "https://comic.naver.com/webtoon/weekday.nhn"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
#print(soup.title.get_text())
#print(soup.a.attrs["href"])
#print(soup.find("a", attrs={"class":"Nbtn_upload"}))
#print(soup.find("li", attrs={"class":"rank01"}))

#rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a)
#rank2 = rank1.next_sibling.next_sibling
#print(rank2.a)
#print(rank1.parent)
#print(rank1.find_next_sibling("li").a.get_text())

# webtoons = soup.find_all("a", attrs={"class":"title"})
# for webtoon in webtoons:
#     print(webtoon.get_text())


####  기본 사용법  ##################################################
# url = "https://comic.naver.com/webtoon/list.nhn?titleId=335885"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})
# for cartoon in cartoons:
#     print(cartoon.a.get_text())
#     print("https://comic.naver.com" + cartoon.a["href"])






