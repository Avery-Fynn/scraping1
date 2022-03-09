import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

print("응답코드: ", res.status_code)


res.raise_for_status()
print("웹 스크래핑을 진행합니다.")


print(len(res.text))

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
