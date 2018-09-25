import requests,re
from bs4 import BeautifulSoup

def chart_parse():
    url = "http://www.mnet.com/chart/TOP100/"
    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html,'html.parser')
    Music_item = soup.find("div",{"class" : "MMLTable jQMMLTable"})
    Music_title = Music_item.find_all("a",{"class":"MMLI_Song"})
    Music_artist = Music_item.find_all("div",{"class":"MMLITitle_Info"})

    title = []
    artist = []
    music = {}
    for t in Music_title:
        t = re.sub('<.+?>', '', str(t), 0, re.I|re.S)
        t = t.replace("&amp;","&")
        title.append(t)

    for art in Music_artist:
        a = ""
        art = art.find_all("a",{"class":"MMLIInfo_Artist"})
        for ar in art:
            ar = re.sub('<.+?>', '', str(ar), 0, re.I|re.S)
            ar = ar.replace("&amp;", "&")
            a += ar+", "
        artist.append(a[:-2])

    for i in range(50):
        music[str(title[i])] = artist[i]

    return music