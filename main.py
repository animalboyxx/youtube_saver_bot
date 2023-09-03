from pytube import YouTube
import pytube
import os


def get_audio(url):
    if get_video_duration(url) < 600:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print('success')
    else:
        print('too long')


def get_video_duration(url):
    youtube = pytube.YouTube(url)
    duration = youtube.length
    return duration


get_audio('https://www.youtube.com/watch?v=iB9YYC-8jwY')
