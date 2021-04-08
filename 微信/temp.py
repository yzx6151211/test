import pyautogui
import pyperclip
import time
time.sleep(10) # 提前打开微信，等待十秒
while True:
    pyperclip.copy('早起的鸟儿有霾吸') # 需要发送的内容
    pyautogui.hotkey('ctrl', 'v') # 按下 ctrl + v 粘贴内容
    pyautogui.mouseUp()  # 模拟鼠标将左键抬起
    pyautogui.moveTo(1315, 800)  # 鼠标点击发送按钮
    pyautogui.mouseDown()  # 模拟鼠标将左键按下
    pyautogui.mouseUp() # 模拟鼠标将左键抬起
