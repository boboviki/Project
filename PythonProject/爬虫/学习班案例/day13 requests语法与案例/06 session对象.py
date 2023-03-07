import requests

session = requests.session()

session.post("http://127.0.0.1:5000/auth", data={
    "user": "yuan",
    "pwd": "123"
})

# (2) 携带cookie爬取数据
res2 = session.get("http://127.0.0.1:5000/books")
print(res2.text)
