from selenium import webdriver

browser = webdriver.Chrome(
    "/Users/gwonminjeong/Desktop/merge/web/chromedriver")

# 네이버로 이동
browser.get("http://naver.com")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# id 새로입력
# browser.find_element_by_id("id").clear()
# browser.find_element_by_id("id").send_keys()

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.close()
browser.quit()
