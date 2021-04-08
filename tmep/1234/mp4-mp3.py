from moviepy.editor import *
#获取文档绝对路径下 所有视频的绝对路径
#逐个转换
#保存为MP3




#修改文件夹下所有xml文件中的中文路径
def changesku(inputpath):
    listdir = os.listdir(inputpath)#获得所有文件名
    for file in listdir:

        filepath = os.path.join(inputpath, file)#将根路径与文件名路径组合成绝对路径
        video = VideoFileClip(filepath)
        list_filepath = list(filepath)
        if list_filepath[-1] == '4':
            list_filepath[-1] = '3'
            filepath = ''.join(list_filepath)
            print(filepath)
            audio = video.audio
            audio.write_audiofile(filepath)


if __name__ == '__main__':
    vediopath = 'mp3转mp4'  # 这是xml文件的文件夹的绝对地址
    changesku(vediopath)
