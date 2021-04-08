import urllib.request
import urllib.parse
import urllib.parse
import execjs

# 找到rsa.js文件里最下方的公钥参数，把这个参数修改成自己的公钥
js_file = './rsa.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_code = f.read()

js = execjs.compile(js_code)
userName = urllib.parse.quote(js.call('getRsaResult', '尤正兴'))
password = urllib.parse.quote(js.call('getRsaResult', 'wl123456@'))

posturl  = "http://172.26.254.53:8080/xzsp/core/themes/theme1/jsp/login.jsp"
postdate  = urllib.parse.urlencode({"userName":userName,
                                    "password":"password@",
                                    "deptunid":"aaaaaaaaaaaaaaaaa001008010004012"}).encode("utf-8")
req = urllib.request.Request(posturl,postdate)
rst = urllib.request.urlopen(req).read().decode("utf-8")
fh = open("C:\\Users\\Administrator\\Desktop\\1\\post.html","w")
fh.write(rst)
fh.close()

print(rst)