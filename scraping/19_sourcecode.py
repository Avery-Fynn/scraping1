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

url = "https://pedia.watcha.com/ko-KR/staffmades/278"
browser.get(url)
interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

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
        print(title, score)
        print("-"*100)

        data = score + "\t" + title + "\n"

        f = open("영화목록.txt", 'a', encoding="utf8")
        f.write(data)
        f.close()

browser.quit()
