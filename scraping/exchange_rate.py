import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


data_rows = soup.find("table", attrs={"class": "rate_table_info"}).find(
    "tbody").find_all("tr", limit=4)
for row in data_rows:
    name = row.find("th")
    columns = row.find_all("td")

    print(name.get_text())
    print("매매기준율: ", columns[0].get_text())
    print("전일대비: ", columns[1].get_text()[4:])
    print("등락율: ", columns[2].get_text())
    print("-"*30)
