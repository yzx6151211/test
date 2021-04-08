import win32com.client
import threading
from multiprocessing import Pool
import pythoncom
def get_datafram1(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\1.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram2(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\2.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram3(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\3.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram4(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\4.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram5(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\5.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram6(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\6.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram7(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\7.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram8(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\8.xlsx"
        xlApp = win32com.client.Dispatch("Excel.Application")
        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\2.txt","a")
            f.write(str(i))
            f.close()
            break
        except Exception :
            print(i)
def get_datafram9(start,end):
    """
    参数一：文件路径
    参数二：文件密码
    return: 解密后输出的df
    """
    pythoncom.CoInitialize()

    for i in range((start),(end)):
        filename = "C:\\Users\\Administrator\\Desktop\\新建文件夹 (2)\\9.xlsx"
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

t1 = threading.Thread(target=get_datafram1, kwargs={"start": 51000, "end": 1000000000})
t2 = threading.Thread(target=get_datafram2, kwargs={"start": 1000173000, "end": 2000000000})
t3 = threading.Thread(target=get_datafram3, kwargs={"start": 2000173000, "end": 3000000000})
t4 = threading.Thread(target=get_datafram4, kwargs={"start": 3000173000, "end": 4000000000})
t5 = threading.Thread(target=get_datafram5, kwargs={"start": 4000173000, "end": 5000000000})
t6= threading.Thread(target=get_datafram5, kwargs={"start": 5000000001, "end": 6000000000})
t7 = threading.Thread(target=get_datafram6, kwargs={"start": 6000173000, "end": 7000000000})
t8 = threading.Thread(target=get_datafram7, kwargs={"start": 7000173000, "end": 8000000000})
t9= threading.Thread(target=get_datafram8, kwargs={"start": 8000173000, "end": 9000000000})
t10 = threading.Thread(target=get_datafram9, kwargs={"start": 9000173000, "end": 9999999999})





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
