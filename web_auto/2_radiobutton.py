from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()

browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="html"]')

if elem.is_selected() == False:
    elem.click()
else:
    pass

browser.switch_to.default_content()

time.sleep(5)

browser.quit()
