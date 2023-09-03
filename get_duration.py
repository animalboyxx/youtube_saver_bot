import pytube


def get_video_duration(url):
    youtube = pytube.YouTube(url)
    duration = youtube.length
    print(duration)

get_video_duration('https://www.youtube.com/watch?v=iB9YYC-8jwY')