import requests
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

res = requests.get(url, headers=headers)
print("응답코드: ", res.status_code)

res.raise_for_status()
print("웹 스크래핑을 진행합니다.")

print(len(res.text))

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
