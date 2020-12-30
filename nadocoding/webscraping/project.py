import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()   

    soup = BeautifulSoup(res.text, "lxml")
    return soup


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()    # 맑음, 어제보다 2˚ 낮아요
    curr_temp = soup.find("span", attrs={"class":"todaytemp"}).get_text()    
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()    
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()    

    rain_rate_morning = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    rain_rate_afternoon = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {})".format(rain_rate_morning, rain_rate_afternoon))
    print("")

def scrape_headline_new():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)

    hdlines = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
    for idx, hdline in enumerate(hdlines):
        if idx < 3:
            print(hdline.find("a").get_text().strip())
            print(url + hdline.find("a")["href"])
    
    print("")

def scrape_it_new():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    hdlines = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for idx, hdline in enumerate(hdlines):
        print(hdline.find_all("a")[1].get_text().strip())
        print(url + hdline.find_all("a")[1]["href"])
    
    print("")

if __name__ == "__main__":
    scrape_weather()
    scrape_headline_new()
    scrape_it_new()
