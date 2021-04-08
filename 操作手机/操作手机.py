import os
import time


def execute(cmd):
    adbstr = "adb shell {}".format(cmd)
    print(adbstr)
    os.system(adbstr)

if __name__ == '__main__':
    execute("am start -n com.sankuai.meituan/com.meituan.android.pt.homepage.activity.MainActivity")
    time.sleep(2)
    execute("input tap 30 822")
