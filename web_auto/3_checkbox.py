from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()

browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
# elem = browser.find_element(By.XPATH, '//[*@id="vehicle1"]')
elem = browser.find_element(By.LINK_TEXT, 'vehicle1')
