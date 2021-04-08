import re
text='a href="http://ok.renzuida.com/2001/DMF华-48.mp4"'
ret=re.match('href="\w+mp4"',text)
print(ret.group())