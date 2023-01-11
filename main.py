from pytube import YouTube

yt_link = input("link: ")
yt = YouTube(yt_link)
print("Title", yt.title)
print("Views: ", yt.views)
yd = yt.streams.get_highest_resolution()
path = input("Enter the file path: ")
yd.download(path)
