from pytube import YouTube
def download (link)
    youtubeObject=YouTube(link)
    youtubeObject=youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download
    except:
        print("an error has occured")
    print("downloaded sucesfully")

link=input("please enter the link>> ")
download link