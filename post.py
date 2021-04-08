import urllib.request
import urllib.parse
posturl  = "https://www.iqianyue.com/mypost"
postdate  = urllib.parse.urlencode({"name":"adminn",
                                    "pass":"administrator"}).encode("utf-8")
req = urllib.request.Request(posturl,postdate)
rst = urllib.request.urlopen(req).read().decode("utf-8")
fh = open("C:\\Users\\Administrator\\Desktop\\1\\post.html","w")
fh.write(rst)
fh.close()

print(rst)