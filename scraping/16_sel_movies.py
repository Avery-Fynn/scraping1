import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Accept-Language": "ko-KR,ko"
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={
                       "class": "hP61id"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class": "Epkrse"}).get_text()
    print(title)


# with open("movie1.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
