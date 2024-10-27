import os
from pytube import YouTube
from moviepy.editor import*

#ask the link from the user
link = input("Enter the link of the youtube video you want to download: ")
yt = YouTube(link)
opinion = input("Do you want to convert ur video to audio?(y or n): ")

#Showing details
print("Title: ", yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
vid_title = ((((str(yt.title)).replace('.', '')).replace(',', '')).replace("'", "")).replace('|', '') + ".mp4"

#starting download
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download(r'C:\Users\amrit\Videos')
print("Download completed!!")

#the mp4 to mp3 process
if opinion in ['y', ' Y', ' y', 'Y']:
	print("Converting your video to audio...")
	def MP4toMP3(mp4, mp3):
		FILETOCONVERT = AudioFileClip(mp4)
		FILETOCONVERT.write_audiofile(mp3)
		FILETOCONVERT.close()
	VIDEO_FILE_PATH = ((r"C:\Users\amrit\Videos\ ").replace(' ', '') + vid_title)
	AUDIO_FILE_PATH = ((r"C:\Users\amrit\Music\ ").replace(' ', '') + (vid_title).replace('.mp4', '') + ".mp3")
	MP4toMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
elif opinion in ['n', 'N', ' n', ' N']:
	print("Its ur choice, I won't judge")
else:
	print("Error 400: invalid response or bad request")
