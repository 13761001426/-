import requests
url = "https://item.jd.com/100000961842.html"
kv = {"user-agent":"Mozilla/5.0"} #隐藏
try:
    r = requests.get(url,headers=kv,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("异常访问")