import threading,requests
import urllib.request
from threading import Lock,Thread
import time,os
import re
from bs4 import BeautifulSoup as bs
from lxml import etree
from fake_useragent import UserAgent

class ip:
    def __init__(self):
        self.ippool = []
        self.headers = {}
        self.lock = threading.RLock()

    def ret_augst(self):
        ua = UserAgent()

        return {'User-Agent':ua.random}

    def delete_chong(self):
        f = open("C:\\Users\\Administrator\\Desktop\\1.txt", "r+")
        lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
        f.truncate(0)
        f1 = open("C:\\Users\\Administrator\\Desktop\\1.txt", "r+")
        lines1 = []
        for line in lines:
            if line not in lines1:
                f1.write(line)
                lines1.append(line)
        f.close()
        f1.close()

    def ip1(self):
        self.headers = self.ret_augst()
        ip = []
        for i in range(1,1): #几千页
            thisurl = "https://www.kuaidaili.com/free/inha/"+str(i)+"/"
            try:
                responser = requests.get(thisurl, headers=self.headers,timeout = 0.1)
                date = responser.content.decode()
                pat = '<td data-title="IP">((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))</td>'
                res1 = re.compile(pat, re.S).findall(date)
                print(res1)

                for i in res1:
                    res = re.sub(r'</td>\n                    <td data-title="PORT">', ':', i[0])
                    print(res)
                    ip.append(res)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip1")
        return ip

    def ip2(self):
        self.headers = self.ret_augst()
        ip = []
        for j in range(0, 20): # 100多页
            try:
                thisurl = "https://www.89ip.cn/index_" + str(j) + ".html"
                responser = requests.get(thisurl, headers=self.headers,timeout = 0.1)
                date = responser.content.decode()
                pat = pat = '<td>.*?((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+)).*?</td>.*?<td>'
                res1 = re.compile(pat, re.S).findall(date)

                for i in res1:
                    res = re.sub(r'\t\t</td>\n\t\t<td>\n\t\t\t', ':', i[0])
                    print(res)
                    ip.append(res)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip2")
        return ip

    def ip3(self):
        self.headers = self.ret_augst()
        ip = []
        for j in range(1, 6):
            try:
                thisurl = "https://ip.jiangxianli.com/?page="+str(j)
                responser = requests.get(thisurl, headers=self.headers,timeout = 0.1)
                date = responser.content.decode()
                pat = '(\\d+\\.\\d+\\.\\d+\\.\\d+:\\d+)">'
                res1 = re.compile(pat, re.S).findall(date)

                for i in res1:
                    print(i)
                    ip.append(i)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip3")
        return ip

    def ip4(self):
        self.headers = self.ret_augst()
        thisurl = "https://seofangfa.com/proxy/"
        try:
            responser = requests.get(thisurl,headers = self.headers,timeout = 0.1)
            date = responser.content.decode()
            pat = '((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))'
            res1 = re.compile(pat, re.S).findall(date)
            ip = []
            for i in res1:
                res = re.sub(r'</td><td>', ':', i[0])
                ip.append(res)
            return ip
        except requests.exceptions.RequestException as e:
            print(e)
            print("ip4")

    def ip5(self):
        self.headers = self.ret_augst()
        ip = []
        for i in range(1,11):
            try:
                # 10页
                url = "https://www.dieniao.com/FreeProxy/"+str(i)+".html"
                responser = requests.get(url, verify=False,headers = self.headers,timeout = 0.1)
                date = responser.content.decode()
                pat = '<span class=\'f-address\'>((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))</span>'
                res1 = re.compile(pat, re.S).findall(date)
                for i in res1:
                    res = re.sub(r'</span>\n<span class=\'f-port\'>', ':', i[0])
                    print(res)
                    ip.append(res)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip5")
        return ip

    def ip6(self):
        self.headers = self.ret_augst()
        ip = []
        for i in range(1,11):#　共10页
            try:
                thisurl = "http://www.ip3366.net/?stype=1&page="+str(i)
                responser = requests.get(thisurl, verify=False, headers=self.headers, timeout=3)
                encoding = responser.apparent_encoding
                responser.encoding = encoding
                soup = bs(responser.text, 'html.parser')
                date = soup.decode()
                pat = '<td>((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))</td>'
                res1 = re.compile(pat, re.S).findall(date)
                for i in res1:
                    res = re.sub(r'</td>\n<td>', ':', i[0])
                    print(res)
                    ip.append(res)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip6")
        return ip

    def ip7(self):
        self.headers = self.ret_augst()
        ip = []
        for i in range(1, 3):  # 共10页
            try:
                thisurl = "http://www.66ip.cn/"+ str(i)+".html"
                responser = requests.get(thisurl, verify=False, headers=self.headers, timeout=3)
                encoding = responser.apparent_encoding
                responser.encoding = encoding
                soup = bs(responser.text, 'html.parser')
                date = soup.decode()
                pat ='<tr><td>((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))</td><td>'
                res1 = re.compile(pat, re.S).findall(date)
                for i in res1:
                    res = re.sub(r'</td><td>', ':', i[0])
                    print(res)
                    ip.append(res)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip7")
        return ip

    def ip8(self):
        self.headers = self.ret_augst()
        ip = []
        for i in range(1, 11):  # 共10页
            try:
                thisurl = "http://www.kxdaili.com/dailiip/1/"+str(i)+".html"
                responser = requests.get(thisurl, verify=False, headers=self.headers, timeout=3)
                encoding = responser.apparent_encoding
                responser.encoding = encoding
                soup = bs(responser.text, 'html.parser')
                date = soup.decode()
                pat = '<td>((\\d+\\.\\d+\\.\\d+\\.\\d+).*?(\\d+))</td>'
                res1 = re.compile(pat, re.S).findall(date)
                for i in res1:
                    res = re.sub(r'</td>\n<td>', ':', i[0])
                    print(res)
                    ip.append(res)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip8")
        return ip

    def ip9(self):
        headers = self.ret_augst()
        url = "http://www.xsdaili.cn/"
        response = requests.get(url, headers=headers)
        data = response.content.decode()
        html = etree.HTML(data)
        ret = html.xpath("//div[@class ='col-md-12']//div//@href")
        new_url = "http://www.xsdaili.cn" + ret[0]
        # print(new_url)
        new_response = requests.get(new_url, headers=headers)
        new_data = new_response.content.decode()
        # print(new_data)

        new_html = etree.HTML(new_data)
        new_ret = html.xpath("//div[@class ='cont']/text()")
        ip = []
        for i in new_ret:
            # print(i)
            pat = '(\\d+\\.\\d+\\.\\d+\\.\\d+:\\d+)'
            res1 = re.compile(pat, re.S).findall(i)
            # print(res1)

            for j in res1:
                if len(j) > 0:
                    ip.append(j)
        return ip

    def ip10(self):
        self.headers = self.ret_augst()
        ip = []
        for i in range(1, 10):
            try:
                # 10页
                url = "http://www.xiladaili.com/gaoni/" + str(1) + "/"
                responser = requests.get(url, verify=False, headers=self.headers, timeout=0.1)
                date = responser.content.decode()
                # print(date)
                pat = '    <td>((\\d+\\.\\d+\\.\\d+\\.\\d+:\\d+))</td>'
                res1 = re.compile(pat, re.S).findall(date)
                # print(res1)
                for i in res1:
                    ip.append(i[0])
                time.sleep(1)
            except requests.exceptions.RequestException as e:
                print(e)
                print("ip5")

        return ip

    # def opener(self,number):
    #
    #
    #     thisip = self.ippool
    #     thisip = thisip[number]
    #     proxy = urllib.request.ProxyHandler({"http": thisip})  # 转成特定格式
    #     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)  # 将代理ip添加到系统
    #     urllib.request.install_opener(opener)

    def run(self,t):

        #ip  = {1:self.ip1(),2:self.ip2(),3:self.ip3(),4:self.ip4(),5:self.ip5(),6:self.ip6()}
        if t ==1:
            self.ippool = self.ip1()
        elif t ==2:
            self.ippool = self.ip2()
        elif t ==3:
            self.ippool = self.ip3()
        elif t ==4:
            self.ippool = self.ip4()
        elif t ==5:
            self.ippool = self.ip5()
        elif t ==6:
            self.ippool = self.ip6()
        elif t ==7:
            self.ippool = self.ip7()
        elif t ==8:
            self.ippool = self.ip8()
        elif t ==9:
            self.ippool = self.ip9()
        elif t ==10:
            self.ippool = self.ip10()

        for i in self.ippool:
            self.lock.acquire()
            print("加锁")
            try:
                proxies = {'http':i,'https':i}
                url = "http://www.baidu.com"
                data = requests.get(url,proxies=proxies,headers = self.headers,timeout = 0.1).content.decode()
                print(len(data))


                if len(data):
                    #print(self.ippool[i])

                    f = open("C:\\Users\\Administrator\\Desktop\\1.txt", "a")  # 设置文件对象
                    f.write(i + "\n")
                    print("写入成功" + i)
                    f.close()
            except Exception as err:
                print("*"*100)
                print(err)
            self.lock.release()
            print("解锁")
         #去重写入2.txt
        self.delete_chong()

if __name__ == '__main__':
    ip = ip()
    t1 = threading.Thread(target=ip.run, args=(1,))
    t2 = threading.Thread(target=ip.run, args=(2,))
    t3 = threading.Thread(target=ip.run, args=(3,))
    t4 = threading.Thread(target=ip.run, args=(4,))
    t5 = threading.Thread(target=ip.run, args=(5,))
    t6 = threading.Thread(target=ip.run, args=(6,))
    t7 = threading.Thread(target=ip.run, args=(7,))
    t8 = threading.Thread(target=ip.run, args=(8,))
    t9 = threading.Thread(target=ip.run, args=(8,))
    t10 = threading.Thread(target=ip.run, args=(8,))


    t1.setDaemon(True)    #把子线程设置为守护线程，必须在start()之前设置
    t2.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t3.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t4.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t5.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t6.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t7.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t8.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
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



    t1.join()     #设置主线程等待子线程结束
    t2.join()
    t3.join()  # 设置主线程等待子线程结束
    t4.join()
    t5.join()     #设置主线程等待子线程结束
    t6.join()     #设置主线程等待子线程结束
    t7.join()     #设置主线程等待子线程结束
    t8.join()     #设置主线程等待子线程结束
    t9.join()     #设置主线程等待子线程结束
    t10.join()     #设置主线程等待子线程结束
