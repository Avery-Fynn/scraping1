from selenium import webdriver
import time

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()
url = "https://www.w3schools.com"
browser.get(url)

elem = browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]')
elem.click()

elem = browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]')
elem.click()


#### Contact Form 찾아서 클릭 ######
# xpath 로 찾기
# elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]')
# elem.click()

# 이름으로 찾기
# elem = browser.find_element_link_text('Contact Form')
# elem.click()

# xpath+ 텍스트값으로 찾기 (a[117]번째 a태그가 아닌 a태그중 텍스트 이름이 ""인것 찾기)
# elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]')
# elem.click()

# 일부텍스트만 같은 것 찾기
# elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text()="Contact")]')
# elem.click()


# 변수 써서 내용 입력
fname = "hello"
lname = "world"
country = "canada"
subject = "퀴즈 완료"
elem = browser.find_element_by_xpath('//*[@id="fname"]').send_keys(fname)
elem = browser.find_element_by_xpath('//*[@id="lname"]').send_keys(lname)
elem = browser.find_element_by_xpath(
    '//*[@id="country"]/option[text()="{}"]'.format(country)).click()
elem = browser.find_element_by_xpath(
    '//*[@id="main"]/div[3]/textarea').sen_keys(subject)
elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()
time.sleep(3)
browser.quit()
##########################

# elem = browser.find_element_by_xpath('//*[@id="fname"]')
# elem.send_keys("hello")

# elem = browser.find_element_by_xpath('//*[@id="lname"]')
# elem.send_keys("world")

# elem = browser.find_element_by_xpath('//*[@id="country"]/option[2]')
# elem.click()

# elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
# elem.send_keys("퀴즈 완료")

# time.sleep(3)

# elem = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a')
# elem.click()


