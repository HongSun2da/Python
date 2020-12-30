
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# 실행 브라우저 숨기기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome("chromedriver.exe")
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 1920*1080

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    if prev_height == curr_height:
        break
    
    prev_height = curr_height    

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")


soup = BeautifulSoup(browser.page_source, "lxml")
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)
    
    # SUZt4c djCuy
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, " <할인되지 않은 영화 제외>")
        continue

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()     

    link = movie.find("a", attrs={"class":"JC71ub"})["href"]     
    
    print(f"title : {title}")
    print(f"original_price : {original_price}")
    print(f"price : {price}")
    print(f"link : https://play.google.com{link}")
    print("*"*200)


