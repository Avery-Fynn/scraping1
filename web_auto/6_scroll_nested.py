from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()
browser.get('https://www.w3schools.com/html/')
time.sleep(1)

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]')

# ActionChain
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

# 방법2

xy = elem.location_once_scrolled_into_view
print("type:", type(xy))  # dict

# 방법3: elem 좌표를 아래것으로 바꾼다음 클릭 inner"] 뒤에 /a[61]
elem.click()


time.sleep(5)
browser.quit()
