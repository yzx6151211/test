from fake_useragent import UserAgent
ua = UserAgent()
a = {"user_agent" : ua.random}
print(a)
print(ua.chrome)
print(ua.opera)
print(ua.firefox)
print(ua.safari)
print(ua.random)
print(ua.random)
print(ua.random)