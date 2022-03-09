from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('http://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle)

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a')

handles = browser.window_handles
for handle in handles:
    print(handle)
    browser.swith_to.window(handle)
    print(browser.title)
    print()

print("현재 핸들 닫기")
browser.close()

print("처음 핸들로 돌아오기")
browser.swith_to.window(curr_handle)

print(browser.title)

time.sleep(5)
browser.quit
