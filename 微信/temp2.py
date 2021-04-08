from wxpy import *
bot = Bot()
bot = Bot(cache_path=True)
from wxpy import Bot
from pyecharts import Pie
import webbrowser
# 实例化一个微信机器人对象
bot = Bot()
# 获取到微信的所有好友
friends = bot.friends()
# 设定男性\女性\位置性别好友名称
attr = ['男朋友', '女朋友', '人妖']
# 初始化对应好友数量
value = [0, 0, 0]
# 遍历所有的好友,判断这个好友是男性还是女性
for friend in friends:
    if friend.sex == 1:
        value[0] += 1
    elif friend.sex == 2:
        value[1] += 1
    else:
        value[2] += 1
# 实例化一个饼状图对象
pie = Pie('nick的好友们!')
# 图表名称str，属性名称list，属性所对应的值list，is_label_show是否现在标签
pie.add('', attr, value, is_label_show=True)
# 生成一个html文件
pie.render('friends.html')
# 打开html文件
webbrowser.open('friends.html')