import requests
from bs4 import BeautifulSoup


headers = {
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001001046&sumgb=03&FetchSize=40&layout=3&PageNumber={}"
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.select("#category_layout")
for row in data_rows:
    columns = row.find_all("a")

    print("="*60)
    print("제목 : ", columns[0].get_text().strip())
    print("저자 : ", columns[2].get_text().strip())

    # with open("book.html", "a", encoding="utf8") as f:
    #     f.write(soup.prettify())

    # for book in books:
    #     title = book.find(
    #         "a", attrs={"href"}).get_text()
    #     writer = book.find_element_by_xpath(
    #         "//*[@id='category_layout']/tbody/tr/td/p/a").get_text()
    #     company = book.find_element_by_xpath(
    #         "//*[@id='category_layout']/tbody/tr/td/p/a").get_text()
    #     price = book.find_element_by_xpath(
    #         "//*[@id='category_layout']/tbody/tr/td/span/strong").get_text()
    #     link = book.find_element_by_xpath(
    #         "//*[@id='category_layout']/tbody/tr/td/a")["href"]

    #     print(f"제목 : {title}")
    # print(f"저자 : {writer}")
    # print(f"출판사 : {company}")
    # print(f"가격 : {price}")
    # print("바로가기 : {}".format("http://www.yes24.com" + link))
    # print("-"*100)

    # f = open("영화목록.txt", 'a', encoding="utf8")
    # f.write(f"제목 : {title}")
    # f.write(f"저자 : {writer}")
    # f.write(f"출판사 : {company}")
    # f.write(f"가격 : {price}")
    # f.write("바로가기 : {}".format("http://www.yes24.com" + link))
    # f.write("-"*100)

    # f.close()
