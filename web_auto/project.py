import re
import requests
from bs4 import BeautifulSoup


def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup


def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print(" (링크: {})".format(link))
    print()


def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    curr_temp = soup.find(
        "div", attrs={"class": "temperature_text"}).get_text()

    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text()

    rainfall = soup.find("div", attrs={"class": "cell_weather"})
    morning_rainfall = rainfall.find_all("span", attrs={"class": "rainfall"})[
        0].get_text()
    afternoon_rainfall = rainfall.find_all(
        "span", attrs={"class": "rainfall"})[1].get_text()

    # morning_rain_rate = soup.find(
    #     "span", attrs={"class": "weather_left"}, text).get_text().strip()
    # afternoon_rain_rate = soup.find(
    #     "span", attrs={"class": "point_time afternoon"}).get_text().strip()

    dust = soup.find("ul", attrs={"class": "today_chart_list"})
    pm10 = dust.find_all("li")[0].get_text()
    pm25 = dust.find_all("li")[1].get_text()

    print(" {} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("  강수확률 오전 {} / 오후 {}".format(morning_rainfall, afternoon_rainfall))
    print()
    print("{}".format(pm10))
    print("{}".format(pm25))
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.daum.net/"
    soup = create_soup(url)

    news_list = soup.find(
        "ul", attrs={"class": "list_newsissue"}).find_all("div", attrs={"class": "cont_thumb"}, limit=5)

    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)


def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.daum.net/digital#1"
    soup = create_soup(url)
    itnews_list = soup.find(
        "ul", attrs={"class": "list_newsmajor"}).find_all("li", limit=5)
    for index, news in enumerate(itnews_list):

        # 만일 img 태그 등 중간에 삽입된 태그가 있으면 [0]이 아닌 [1]번째 a 태그 정보를 사용하려면
        #a_idx = 0
        #img = news.find("img")
        # if img:
        #a_idx = 1
        #a_tag = news.find_all("a")[a_idx]
        #title = a_tag.get_text().strip()
        #link = a_tag["href"]

        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()


# def scrape_english():
#     print("[오늘의 영어 회화]")
#     url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
#     soup = create_soup(url)
#     sentences = soup.find_all("div", attrs={"id": re.compile("^conv_kor_t")})

#     print("<한글지문>")
#     for sentence in sentences[:len(sentences)//2]:
#         print(sentence.get_text().strip())
#     print()

#     print("<영어지문>")
#     for sentence in sentences[len(sentences)//2:]:
#         print(sentence.get_text().strip())
#     print()


# if __name__ == "__main__":
#     scrape_weather()
#     scrape_headline_news()
#     scrape_it_news()
#     scrape_english()
