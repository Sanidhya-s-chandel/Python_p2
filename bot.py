from pytube import YouTube
link = input("please provide your youtube link")
check = input("press 1 for video and press 2 for audio only")

if check == "1":
    youtube_1 = YouTube(link)
    videos = youtube_1.streams.filter(progressive = True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    strm = int(input("please provide which stream you want to download"))
    videos[strm].download()
    print("successfully downloaded")

if check == "2":
    youtube_1 = YouTube(link)
    audio = youtube_1.streams.filter(only_audio = True)
    aud = list(enumerate(videos))
    for i in aud:
        print(i)
    strm = int(input("please provide which stream you want to download"))
    audio[strm].download()
    print("successfully downloaded") 