from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.naver')

elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선 마우스')
time.sleep(1)
elem.send_keys(Keys.ENTER)

# 스크롤
browser.execute_script('window.scrollTo(0, 900)')
browser.execute_script('window.scrollTo(0, 1800)')

# 가장 아래로 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막까지 스크롤 반복
interval = 2

prev_height = browser.execute_script('return document.body.scrollHeight')
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

# 스크롤 맨 위로 올리기
browser.execute_script('window.scrollTo(0, 0)')

time.sleep(5)
browser.quit()
