from chart_parse import chart_parse
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("/Users/oonja/Downloads/Downloads/chromedriver_win32/chromedriver")

chart = chart_parse()
url = "https://www.youtube.com/results?search_query="
url += "우리 그만하자 로이킴"

driver.get(url)
html = driver.page_source
driver.close()

soup = BeautifulSoup(html,'html.parser')
video_item = soup.find("div",{"id":"contents"}).\
    find_all("a",{"class":"yt-simple-endpoint style-scope ytd-video-renderer"})

video_list = {}
for video in video_item:
    video_url = video['href']
    video_title = video['title']
    video_list[str(video_title)] = video_url

print(video_list)

