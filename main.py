import requests
from chart_parse import chart_parse
from bs4 import BeautifulSoup

chart = chart_parse()
url = "https://www.youtube.com/results?search_query="
url += "우리 그만하자"

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html,'html.parser')
video_item = soup.find("div",{"id":"contents"})
print(video_item)
print(soup)


