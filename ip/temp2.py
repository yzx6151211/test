import win32com.client
import threading
import pythoncom,math


def get_datafram1(start,end,bool):

    pythoncom.CoInitialize()
    filename = "C:\\Users\\Administrator\\Desktop\\2.xlsx"
    xlApp = win32com.client.Dispatch("Excel.Application")
    for i in range((start),(end),bool):
        print(i)

        try:
            xlApp.Workbooks.Open(filename, False, True, None, Password=i)
            f = open("C:\\Users\\Administrator\\Desktop\\1.txt","a")
            f.write(str(i)+"\n")
            f.close()
            break
        except Exception :
            #print(i)
            pass




if __name__ == '__main__':
    if __name__ == '__main__':
        start = 0
        end = 0
        start = int(input("输入开始数字"))
        end = int(input("输入结束数字"))
        mod = (end-start)%10
        inpu = math.floor((end-start)/10)
        print(inpu)
        T_POOL = []
        for i in range(10):
            t = "th" + str(i)
            #print(t)

            t = threading.Thread(target=get_datafram1, kwargs={"start": start+inpu*i, "end": start+inpu*(i+1),"bool":1})
            t.setDaemon

            t.start()
            T_POOL.append(t)

        for t in T_POOL:
            t.join()
