import time
import win32clipboard
from pytube import YouTube

last_url = ""
while True:
    try:
        win32clipboard.OpenClipboard()
        url = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except:
        url = ""

    if url and last_url != url:
        if url.startswith("https://www.youtube.com/watch?v"):
            print("Video detectado, descargando...")
            YouTube(url).streams.get_highest_resolution().download()
            print("Video descargado")
            print("#########################################################")

            last_url = url

    time.sleep(0.1)
