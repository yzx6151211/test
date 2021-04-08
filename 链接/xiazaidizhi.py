import re
def ip():
    date = open("C:\\Users\\Administrator\\Desktop\\新建文本文档 (7).txt",encoding='gbk')
    txt = ""
    for line in date:
        txt=txt+line
    return txt


pat = 'https{0,1}://www\.[^\x{4e00}-\x{9fa5}\n\r\s]+\.((com)|(cn)|(info)|(com\.cn)|(top))[^\x{4e00}-\x{9fa5}\n\r\s]*'
res1 = re.compile(pat, re.S).findall(ip())
print(res1)