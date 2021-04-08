import urllib.request
import re
response = urllib.request.urlopen("https://www.biedoul.com/t/54iG56yR5Zu%2B54mH_246.html")
html = response.read()
images = re.findall(r'src="(.*?\.(jpg|png))"',html.decode('utf-8'))
x=1

for ima in images:
    try:
        urllib.request.urlretrieve(ima[0], filename='C:/Users/Administrator/Desktop/1/%d.jpg' % x)
    except:
        pass
    print(ima[0])
    x+=1

