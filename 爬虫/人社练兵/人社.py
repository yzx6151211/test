import requests
from fake_useragent import UserAgent
import math,random,json
from pprint import pprint

class renshe:
    def __init__(self):
        self.headers = self.ret_augst()

        self.data = {"mobile": "18968682676",
                     "password": "fb7de2a8e80f8a280690bdb0c14c6111",
                     "verifyCode": "0000"

                     }
        self.session = requests.session()
        self.url = "https://bw.chinahrt.com.cn/api/candidate/login"
        self.url2 = "https://bw.chinahrt.com.cn/api/examination/enterExamination?id={}&RandomCode={}"

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
        response = self.session.get(self.url2.format("cc6de80eeeaa4bd3ab65f7bad74bb9c2",self.randomcode()),headers = self.headers)
        f = open("text_html.txt", 'a', encoding="utf-8")
        f.write(response.content.decode() + "\n"+"\n"+"*"*100)
        f.close()
        return response.content.decode()

    def json1(self,json1):
        ret = json.loads(json1)
        #pprint(ret)
        content = ret["data"]["questionTypeSummaries"]
        open("text.txt", 'w').close()
        for i in content:
            content_down = i["questions"]
            for j in content_down:
                print("id" + ":" + j["id"])
                content_ti = j["content"]
                content_ti = content_ti.strip("&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;")
                content_ti = content_ti.strip("&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;")
                content_ti = content_ti.strip("&amp;2526lt;/span&amp;2526gt;")
                content_ti = content_ti.strip("&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;")
                content_ti = content_ti.strip("&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;")
                content_ti = content_ti.strip("&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;")

                content_ti = content_ti.replace("（&amp;2526lt;/span&amp;2526gt; &nbsp;&nbsp;&amp;2526lt;span&amp;2526gt;）", "(    )")
                content_ti = content_ti.replace("（ &nbsp; &nbsp;）", "(    )")
                content_ti = content_ti.replace("(    )", "（）")
                content_ti = content_ti.replace("（    ）", "（）")
                content_ti = content_ti.replace("(", "（")
                content_ti = content_ti.replace(")", "）")

                content_ti = content_ti.replace("“", "\"")
                content_ti = content_ti.replace("”", "\"")
                content_ti = content_ti.replace("\n", "")



                print(content_ti)
                f = open("text.txt", 'a', encoding="utf-8")
                f.write(content_ti + "\n")
                f.close()
                if (j["choices"]) != None:
                    for l in j["choices"]:
                        content = str(l["content"])
                        content = content.strip(
                            "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;")
                        content = content.strip(
                            "&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;")
                        content = content.strip("&amp;2526lt;/span&amp;2526gt;")
                        content = content.strip("&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;")
                        content = content.strip(
                            "&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;span&amp;2526gt;&amp;2526lt;span&amp;2526gt;")
                        content = content.strip(
                            "&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/span&amp;2526gt;&amp;2526lt;/p&amp;2526gt;&amp;2526lt;p&amp;2526gt;&amp;2526lt;br /&amp;2526gt;&amp;2526lt;/p&amp;2526gt;")

                        code = (l["code"])
                        f = open("text.txt", 'a', encoding="utf-8")
                        f.write(code + ":" + content + "\n")
                        f.close()
                        print(code + ":" + content)
                print("*" * 100)
    def run(self):
        self.parse()
        json_temp =  self.parse2()
        self.json1(json_temp)



if __name__ == '__main__':
    renshe =  renshe()

    renshe.run()