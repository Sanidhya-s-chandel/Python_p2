from pytube import YouTube

try:
    link = input("Please provide your YouTube link: ")
    check = input("Press 1 for video and press 2 for audio only: ")

    youtube = YouTube(link, use_oauth=True, allow_oauth_cache=True)

    if check == "1":
        youtube_1 = YouTube(link)
        videos = youtube_1.streams.filter(progressive=True)
        vid = list(enumerate(videos))
        for i in vid:
            print(i)
        strm = int(input("Please provide which stream you want to download: "))
        videos[strm].download()
        print("Video successfully downloaded.")

    elif check == "2":
        youtube_1 = YouTube(link)
        audio = youtube_1.streams.filter(only_audio=True)
        aud = list(enumerate(audio)) 
        for i in aud:
            print(i)
        strm = int(input("Please provide which stream you want to download: "))
        audio[strm].download()
        print("Audio successfully downloaded.")
    else:
        print("Invalid input. Please enter 1 or 2.")
except Exception as e:
    print(f"An error occurred: {e}")