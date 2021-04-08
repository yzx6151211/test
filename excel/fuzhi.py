import os
names = os.listdir('.//1')  #路径
i=0  #用于统计文件数量是否正确，不会写到文件里
for name in names:
    index = name.rfind('.')
    name = name[:index]
    i=i+1

