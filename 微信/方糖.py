import requests
text = "123"
desp = "321"

data = {
    "text" : text,
    "desp": desp
}


from openpyxl.styles import Border
requests.get("https://sc.ftqq.com/SCU9774T276cf0c078302cc3c762ff794b27f6b95959bb9107466.send?",data = data)