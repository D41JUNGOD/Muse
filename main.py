from parse import chart_parse,video_parse
from video_downloader import video

def chart_50():
    chart_list = chart_parse()

    print("실시간 TOP50")
    ct = 1
    for key in chart_list:
        print(ct,". ",key," - ", chart_list[key])
        ct+=1

def yt_search(search):
    yt_list = video_parse(search)

    print("검색어 리스트")
    ct = 1
    for key in yt_list:
        print(ct,". ",key," - ", yt_list[key])
        ct+=1

if __name__ == '__main__':
    chart_50()
    yt_search("주지마 - 로꼬")



