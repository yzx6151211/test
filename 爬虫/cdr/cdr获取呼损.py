import requests
import json
import time
import pandas as pd
import random
from fake_useragent import UserAgent
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64

class Cdr:
    def __init__(self):

        self.ua = UserAgent()

        self.session = requests.session()
        self.url_husun = (
            "http://cdr.114yun.net:8001/cdr!downLoadXls.act?callType=CALL_FAIL&startTime={}%2000:00:00&endTime={}%2023:59:59")
        self.url_huru = (
            "http://cdr.114yun.net:8001/cdr!downLoadXls.act?callType=CALL_IN&startTime={}%2000:00:00&endTime={}%2023:59:59&isDail=Y")
        session = requests.session()

        self.post_url = "http://cdr.114yun.net:8001/login!login.act"
        self.post_data = {"companyCode":"7686233840","account":"admin","password":self.get_rsa("a751360j24")}
        self.headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Host": "cdr.114yun.net:8001",
"Referer": "http://cdr.114yun.net:8001/cdr!inboundFailPage.act?callType=CALL_IN",
"Upgrade-Insecure-Requests": "1",
"User-Agent":self.ua.random
}
    def get_rsa(self,message):
        public_key = "-----BEGIN PUBLIC KEY-----" + "\n" + "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQ1SFRAqjqhbrD39HEBWEGDmmU" + "\n" + "lyYhX9PmnezMuAQkD0QEp2mYtx5efMvpokXSfFj0TZ5rcjIVpd3OnBs9+gX7mNLB" + "\n" + "8uu2mn9yFdg1V8g1+e96QM3lpLHzoC9SvHbwcADM4skCP+jdHOq42psb08FuruMA" + "\n" + "WBjXYpwfRytNpHrdXwIDAQAB" + "\n" + "-----END PUBLIC KEY-----"
        cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(public_key))
        cipher_text = base64.b64encode(cipher.encrypt(message.encode())).decode()
        return cipher_text
    # 获取时间
    def date(self):
        while True:
            try:
                time_s_e = input("请输入：（1：获取一天、2：获取多天）")
                if time_s_e == "1":
                    #startTime = "2021-01-26"
                    startTime = input("请输入时间，格式为xxxx-xx-xx")
                    startTime = startTime[0:4] + "-" + startTime[4:6] + "-" + startTime[6:8] + ""
                    endTime = startTime
                elif time_s_e == "2":
                    startTime = input("请输入开始时间，格式为xxxx-xx-xx")
                    startTime = startTime[0:4] + "-" + startTime[4:6] + "-" + startTime[6:8] + ""

                    endTime = input("请输入结束时间，格式为xxxx-xx-xx")
                    endTime = endTime[0:4] + "-" + endTime[4:6] + "-" + endTime[6:8] + ""

                else:
                    print("结束")
                #print(startTime)
                #print(endTime)
                return startTime, endTime


            except(Exception):
                print("请输入1或者2")
    # 获取excel
    def get_parse_excel(self,startTime, endTime):

        rep = self.session.post(self.post_url, data=self.post_data, headers=self.headers)
        print(rep.content.decode())
        #发起呼损
        url_husun = self.url_husun.format(startTime, endTime)
        ret_sun = self.session.get(url_husun, headers=self.headers)
        with open("呼损" + startTime + "至" + endTime+".xls", "wb") as f:
            f.write(ret_sun.content)

        #获取cookie
        dic_cookies = requests.utils.dict_from_cookiejar(self.session.cookies)
        #print(dic_cookies)
        #self.session.close()
        #发起呼入
        time.sleep(5)
        #session = requests.session()
        #rep = self.session.post(self.post_url, data=self.post_data, headers=self.headers)
        url_huru = self.url_huru.format(startTime, endTime)
        ret_huru = self.session.get(url_huru, headers=self.headers)
        with open("呼入" + startTime + "至" + endTime+".xls", "wb") as f:
            f.write(ret_huru.content)
        # 获取cookie
        dic_cookies = requests.utils.dict_from_cookiejar(self.session.cookies)
        #print(dic_cookies)
        return ("呼入" + startTime + "至" + endTime+".xls"),("呼损" + startTime + "至" + endTime+".xls"),startTime, endTime
    def set_excel(self,call_in,call_fail,startTime, endTime):
        data_in = pd.read_excel(call_in,converters={"a": str, "b": str, "c": str, "d": str, "e": str})
        data_fail = pd.read_excel(call_fail,converters={"a": str, "b": str, "c": str, "d": str, "e": str})
        un_in = data_in['主叫号码'].unique()
        un_fail = data_fail['来电号码'].unique()
        #print(un_in)
        #print(un_fail)
        temp_in = []
        for i in un_in:
            if not i in temp_in:
                temp_in.append(i)
        #print(len(temp_in))
        temp_fail = []
        for i in un_fail:
            if not i in temp_fail:
                temp_fail.append(i)
        #print(len(temp_fail))
        temp_husun =[]
        for i in temp_fail:
            if not i in temp_in:
                temp_husun.append(i)
        #print(len(temp_husun))
        #print(temp_husun)

        savedata = pd.DataFrame(temp_husun)
        savedata.to_excel("呼入"+str(len(data_in))+"呼损"+str(len(temp_husun))+"    "+startTime+"至"+endTime+".xls",sheet_name='sheet1', index=False, encoding="gbk",float_format=None,header=False)


    def run(self):
        startTime,endTime = self.date()
        call_in,call_fail,startTime, endTime=self.get_parse_excel(startTime,endTime)
        #print(call_in,call_fail)
        #husun = input("请输入：1、获取呼损，2、结束")
        self.set_excel(call_in,call_fail,startTime, endTime)

if __name__ == '__main__':
    cdr = Cdr()
    cdr.run()

