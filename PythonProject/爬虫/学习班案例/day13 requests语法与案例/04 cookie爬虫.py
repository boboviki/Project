import requests

# (1) 模拟登录，获取动态cookie
res1 = requests.post("http://127.0.0.1:5000/auth", data={
    "user": "yuan",
    "pwd": "123"
})
# 响应cookie
print(dict(res1.cookies))

# (2) 携带cookie爬取数据
res2 = requests.get("http://127.0.0.1:5000/books", cookies=dict(res1.cookies))
print(res2.text)
