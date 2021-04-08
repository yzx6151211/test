import hashlib
import base64
import requests
import xlrd


def headers():
    headers = {
        'Connection': 'keep-alive',
        'Content-Length': '984',
        'Cache-Control': 'no-cache',
        'Content-Type': 'image/x-icon',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',

    }
    return headers


book = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\a.xls')
sheet = book.sheet_by_name('Sheet1')
for i in range(sheet.nrows):
    row_values = sheet.row_values(i)
    mobiles = str(int(row_values[0]))
    content = row_values[1]
    url = "http://112.35.1.155:1992/sms/norsubmit"  # 接口地址
    sign = "n82SHWTQb"
    apId = "wlsbzx"
    ecName = "温岭市社会保险事业管理中心"
    addSerial = ""
    secretKey = "bd5ham"
    #   mobiles="13600586831"

    m = hashlib.md5()
    a = (ecName + apId + secretKey + mobiles + content + sign).encode("utf-8")
    # a = "政企分公司测试demo0123qwe13800138000移动改变生活。DWItALe3A".encode("utf-8")
    m.update(a)
    mac = m.hexdigest()
    url2 = '{"content": "' + content + '", "sign": "' + sign + '", "apId": "' + apId + '", "mac": "' + mac + '", "ecName": "' + ecName + '", "addSerial": "", "secretKey": "' + secretKey + '", "mobiles": "' + mobiles + '"}'
    bytes_url2 = url2.encode("utf-8")
    str_url2 = base64.b64encode(bytes_url2)  # 被编码的参数必须是二进制数据
    payload = str_url2.decode("utf-8")
    r = requests.post(url, json=payload, headers=headers(), verify=False)
    print(r.json())
