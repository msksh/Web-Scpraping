
import requests
from bs4 import BeautifulSoup


# [오늘의 날씨]
# 흐림, 어제보다 00℃ 높아요
# 현재 00℃ (최저 00˚ / 최고 00˚)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 00㎍/㎥좋음
# 초미세번지 00㎍/㎥좋음

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
# 흐림, 어제보다 00℃ 높아요
    cast = soup.find("p", atrrs={"class":"cast_txt"}).get_text()
# 현재 00℃ (최저 00˚ / 최고 00˚)
    curr_temp = soup.find("p", atrrs={"class":"info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", atrrs={"class":"min"}).get_text() #최저온도
    max_temp = soup.find("span", atrrs={"class":"max"}).get_text() #최고온도
# 오전 강수확률 00% / 오후 강수확률 00%
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip() #오전 강수확률
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip() #오후 강수확률

# 미세먼지 00㎍/㎥좋음
# 초미세번지 00㎍/㎥좋음
    dust = soup.find("dl", attrs={"class":"idicator"})
    pm10 = dust.find_all("dd")[0].get_text #미세먼지
    pm25 = dust.find_all("dd")[1].get_text #초미세먼지
#출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크 : {})".format(link))
    print()

if __name__ == "__main__":
#    scrape_weather() #오늘의 날씨 정보 가져오기
   scrape_headline_news()














