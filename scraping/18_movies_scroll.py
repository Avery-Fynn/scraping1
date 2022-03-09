from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1440x900")

browser = webdriver.Chrome(
    "/Users/gwonminjeong/Desktop/merge/web/chromedriver", options=options)
browser.maximize_window()

url = "https://pedia.watcha.com/ko-KR/staffmades/278"  # 278
browser.get(url)

# 스크롤 내리기
# 모니터 높이인 위치로 (900)스크롤 내리기, 1440x900
# browser.execute_script("window.scrollTo(0,1800)")

# #화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

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

print("스크롤 완료")

# =============================================================================================

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("li", attrs={
                       "class": "css-8y23cj"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "css-niy0za"}).get_text()

    score = movie.find("div", attrs={"class": "css-m9i0qw"})
    if score:
        score = score.get_text()
        score = score[5:]

    if float(score) >= 3.8:
        # print(f"평점: {score} \t" f"제목 : {title}")
        print(title, score)
        print("-"*100)

        data = score + "\t" + title + "\n"

        f = open("영화목록.txt", 'a', encoding="utf8")
        f.write(data)
        f.close()

    # link = movie.find("a", attrs={"class": "/ko-KR/contents/mW4L2XW"})["href"]

    # print("바로가기 : {}".format("https://pedia.watcha.com/" + link))

browser.quit()

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
