from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
browser.switch_to.frame('iframeResult')

time.sleep(3)

# xpath로 검색
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')

# 텍스트값을 통해 선택
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')

# 텍스트 값이 부분 일치하는 항목 선택
elem = browser.find_element_by_xpath(
    '//*[@id="cars"]/option[contains(text(), "Au")]')

elem.click()

time.sleep(3)

browser.quit()
