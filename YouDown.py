from pytube import YouTube

while True:
    url = input("Introduce la url del video que quieres descargar: ")
    YouTube(url).streams.get_highest_resolution().download()
    print("Video descargado")
    print("#########################################################")
