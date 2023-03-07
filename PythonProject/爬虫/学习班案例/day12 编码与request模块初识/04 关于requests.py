import requests

res = requests.get("https://www.taobao.com/")
# print(type(res)) # <class 'requests.models.Response'>
print(res.status_code)  # 200
print(res.headers)
print(res.text)  # 字符串
# 写字符
# with open("taobao.html", "w") as f:
#     f.write(res.text)



