from pytubefix import YouTube
import time 
import os
videoUrl = str(input("what is the video URL? \n"))

yt = YouTube(videoUrl)
os.system("cls")
while True:
    yt = YouTube(videoUrl)
    views = yt.views
    print("Views :",views, end="\r")
    time.sleep(1)
