import requests

url = "https://api.qinor.cn/soup/?charset=utf-8"

res = requests.get(url)
print(res.text)