import win32com.client
import threading
from multiprocessing import Pool
import pythoncom
def get_datafram1(start,end,stop):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end),stop):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\10.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)


# get_datafram(0,200)

t1 = threading.Thread(target=get_datafram1, kwargs={"start": 500000000, "end": 0,"stop":1})
t2 = threading.Thread(target=get_datafram1, kwargs={"start": 1000000000, "end": 500000001,"stop":-1})
t3 = threading.Thread(target=get_datafram1, kwargs={"start": 2000000000, "end": 1500000001,"stop":-1})
t4 = threading.Thread(target=get_datafram1, kwargs={"start": 2500000000, "end": 2000000001,"stop":-1})
t5 = threading.Thread(target=get_datafram1, kwargs={"start": 3000000000, "end": 2500000001,"stop":-1})
t6 = threading.Thread(target=get_datafram1, kwargs={"start": 3500000000, "end": 3000000001,"stop":-1})
t7 = threading.Thread(target=get_datafram1, kwargs={"start": 4000000000, "end": 3500000001,"stop":-1})
t8 = threading.Thread(target=get_datafram1, kwargs={"start": 4500000000, "end": 4000000001,"stop":-1})
t9 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 4500000001,"stop":-1})
t10 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 5000000001,"stop":-1})
t11 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t12 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t13 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t14 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t15 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t16 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t17 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t18 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t19 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})
t20 = threading.Thread(target=get_datafram1, kwargs={"start": 5000000000, "end": 9000000001,"stop":-1})





t1.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
t2.setDaemon(True)
t3.setDaemon(True)
t4.setDaemon(True)
t5.setDaemon(True)
t6.setDaemon(True)
t7.setDaemon(True)
t8.setDaemon(True)
t9.setDaemon(True)
t10.setDaemon(True)
t11.setDaemon(True)
t12.setDaemon(True)
t13.setDaemon(True)
t14.setDaemon(True)
t15.setDaemon(True)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()


t1.join()  # 设置主线程等待子线程结束
t2.join()  # 设置主线程等待子线程结束
t3.join()  # 设置主线程等待子线程结束
t4.join()  # 设置主线程等待子线程结束
t5.join()  # 设置主线程等待子线程结束
t6.join()  # 设置主线程等待子线程结束
t7.join()  # 设置主线程等待子线程结束
t8.join()  # 设置主线程等待子线程结束
t9.join()  # 设置主线程等待子线程结束
t10.join()  # 设置主线程等待子线程结束
t11.join()  # 设置主线程等待子线程结束
t12.join()  # 设置主线程等待子线程结束
t13.join()  # 设置主线程等待子线程结束
t14.join()  # 设置主线程等待子线程结束
t15.join()  # 设置主线程等待子线程结束
