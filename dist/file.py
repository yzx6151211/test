import os
def text_create(name):
    names = os.listdir('1')
    desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
    full_path = desktop_path + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    i = 0  # 用于统计文件数量是否正确，不会写到文件里
    str=""
    for name in names:

            index = name.rfind('.')
            name = name[:index]
            str =str+ name+"\n"
            i = i + 1
    file.write(str)   #msg也就是下面的Hello world!
text_create("导出的文件名")