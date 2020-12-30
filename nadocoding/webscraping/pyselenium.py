from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("chromedriver.exe")

browser.get("https://flight.naver.com/flights/")
browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("30")[0].click()
browser.find_elements_by_link_text("12")[1].click()

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    if elem:
        print(elem.text)            

finally:
    browser.quit()

