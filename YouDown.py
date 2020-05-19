import time
import win32clipboard
from pytube import YouTube
import os


LAST_URL_FILE = "last_url.json"
OUTPUT_FOLDER = "videos"


def init_clipboard():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText("Launched YouDown!")
    win32clipboard.CloseClipboard()

    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)


init_clipboard()
last_url = ""
while True:
    win32clipboard.OpenClipboard()
    url = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    if url and last_url != url:
        if url.startswith("https://www.youtube.com/watch?v"):
            print("Video detectado, descargando...")
            YouTube(url).streams.get_highest_resolution().download(OUTPUT_FOLDER)
            print("Video descargado")
            print("#########################################################")

            last_url = url

    time.sleep(0.1)
