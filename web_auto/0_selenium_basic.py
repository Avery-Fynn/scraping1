from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/gwonminjeong/Desktop/web/chromedriver')
browser.maximize_window()

url = "https://www.naver.com/"
browser.get(url)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
}

# 텍스트로 찾기
elem = browser.find_element_by_link_text("카페")

# 주소 정보 불러오기
elem.get_attribute("href")

# 클래스 정보 불러오기
elem.get_attribute("class")

# 동작기능
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()

# id로 찾기
elem = browser.find_element_by_id("query")

# 엔터입력
elem.send_keys(Keys.ENTER)

# 브라우저안에서 첫번째 a 태그 찾기
elem = browser.find_element_by_tag_name("a")

# 브라우저안에서 모든 a 태그 찾기
elems = browser.find_elements_by_tag_name("a")

# 찾은 a 태그들의 주소 정보 불러오기
for e in elems:
    e.get_attribute("href")

# 페이지 이동
browser.get("http://daum.net")

elem = browser.find_element_by_name("q")

# 검색창에 키보드 입력
elem.send_keys("코딩")
elem.send_keys("코딩")

# 지우기
elem.clear()

# 검색 버튼 찾고, 누르기
elem = browser.find_element_by_xpath(
    '//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()

# 스크린샷
browser.save_screenshot('daum.png')

# 소스코드 확인
browser.page_source

# 현재 탭 닫기
browser.close

# 종료
browser.quit()
