from pytube import YouTube
from sys import argv

yt_link = input("link: ")
yt = YouTube(yt_link)
print("Title", yt.title)
print("Views: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download("/Users/cdmar/Documents/YT_Downloads")
