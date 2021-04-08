from moviepy.editor import *

mp4FileName = r'D:\test\tmep\1234\mp3转mp4\test.mp4'
mp3FileName = r'D:\test\tmep\1234\mp3转mp4\test.mp3'
video = VideoFileClip(mp4FileName)
video.audio.write_audiofile(mp3FileName)
