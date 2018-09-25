import os,subprocess
import pytube

def video(v_url):
    url = "https://www.youtube.com"
    url += v_url

    yt = pytube.YouTube(url)

    vids,vnum = video_quality(yt)
    path = video_path()

    vids[vnum].download(path)
    filename = vids[vnum].default_filename

    print(os.path.join(path,filename))
    subprocess.call([
                    'ffmpeg',
                     '-i',
                     os.path.join(path, filename),
                     os.path.join(path, "asdf")
                    ])

    print("complete!")

def video_quality(yt):
    vids = yt.streams.all()

    for i in range(len(vids)):
        print(i, '. ', vids[i])

    vnum = int(input("화질 : "))
    return vids,vnum

def video_path():
    path = os.getcwd()
    return path

if __name__ == '__main__':
    video("/watch?v=BzYnNdJhZQw")