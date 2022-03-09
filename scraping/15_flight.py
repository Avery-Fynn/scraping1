from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()

url = "https://flight.naver.com/"
browser.get(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# 도착지 클릭
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]').click()
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/div/button[2]').click()

# 가는 날 클릭
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

time.sleep(2)

browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button').click()

time.sleep(2)

# 오늘 날 클릭
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/button').click()

time.sleep(2)

# 항공권 검색 클릭
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()


# 로딩 기다리기

try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[2]/div[2]')))
    print(elem.text)
except:
    print("출력 실패")


time.sleep(5)
browser.quit
