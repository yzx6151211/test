import requests
from fake_useragent import UserAgent
import math,random,json
from pprint import pprint

class renshe:
    def __init__(self):
        self.headers = self.ret_augst()

        self.data = {"mobile": "13600586831",
                     "password": "fb7de2a8e80f8a280690bdb0c14c6111",
                     "verifyCode": "0000"

                     }
        self.session = requests.session()
        self.url = "https://bw.chinahrt.com.cn/api/candidate/login"
        self.url2 = "https://bw.chinahrt.com.cn/api/questionPractice/listQuestions?chapterId=6244&questionType=001001&number=5&RandomCode={}"

    def randomcode(self):
        RandomCode = ""

        for i in range(0, 32):
            t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            RandomCode = RandomCode+str(t[math.floor(36*random.random())])
       # print(RandomCode)
        RandomCode = str.lower(RandomCode)[0:8]+"-"+str.lower(RandomCode)[8:12]+"-"+str.lower(RandomCode)[12:16]+"-"+str.lower(RandomCode)[16:20]+"-"+str.lower(RandomCode)[20:32]
       # print(RandomCode)
        return RandomCode

    def ret_augst(self):
        ua = UserAgent()
        return {'User-Agent': ua.random}

    def parse(self):
        response =  self.session.post(self.url,headers = self.headers,data = self.data)
        #print(response.content.decode())

    def parse2(self):
        response = self.session.get(self.url2.format(self.randomcode()),headers = self.headers)

        return response.content.decode()

    def json1(self,json1):
        ret = json.loads(json1)

        content = ret["data"]

        for i in content:
            print(i["id"])
    def run(self):
        self.parse()
        json_temp =  self.parse2()
        self.json1(json_temp)



if __name__ == '__main__':
    renshe =  renshe()

    renshe.run()