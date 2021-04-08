import urllib.parse
import execjs

# 找到rsa.js文件里最下方的公钥参数，把这个参数修改成自己的公钥
js_file = './rsa.js'
with open(js_file, 'r', encoding='utf-8') as f:
    js_code = f.read()

js = execjs.compile(js_code)
password = urllib.parse.quote(js.call('getRsaResult', '尤正兴'))
print('password:', password)