from aiogram import Bot, executor, Dispatcher, types
from config import TOKEN_API
from pytube import YouTube
import pytube
import os

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_url(message: types.Message):
    file = open(get_audio(message.text), 'rb')
    await bot.send_video(message.chat.id, file)


def get_audio(url):
    if get_video_duration(url) < 601:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=".")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print('success')
        return(new_file)
    else:
        print('too long')


def get_video_duration(url):
    youtube = pytube.YouTube(url)
    duration = youtube.length
    return duration


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)
