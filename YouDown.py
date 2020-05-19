import time
import win32clipboard
from pytube import YouTube, Playlist
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
            if "list" not in url:
                print("Video detected, downloading...")
                YouTube(url).streams.get_highest_resolution().download(OUTPUT_FOLDER)
                print("Video downloaded")
                print("#########################################################")
            else:
                print("Playlist detected, downloading...")
                playlist = Playlist(url)

                for i in range(len(playlist)):
                    print("downloading video number {}, {} more to go".format(i + 1, len(playlist) - (i + 1)))
                    try:
                        YouTube(playlist[i]).streams.get_highest_resolution().download(OUTPUT_FOLDER)
                    except:
                        print("This video is not available, skipping...: {0}".format(playlist[i]))

                print("Playlist descargada")
                print("#########################################################")

        last_url = url

    time.sleep(0.1)
