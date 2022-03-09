from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option(
    'prefs', {'download.default_directory': '/Users/gwonminjeong/Desktop/web'})

browser = webdriver.Chrome(
    '/Users/gwonminjeong/Desktop/web/chromedriver', options=chrome_options)
browser.get(
    'https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

time.sleep(5)

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()
