import requests

res = requests.get("https://www.baidu.com/",headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

with open("baidu.html", "w") as f:
    f.write(res.text)
