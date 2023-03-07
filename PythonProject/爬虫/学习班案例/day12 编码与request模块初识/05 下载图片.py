import requests

res = requests.get("https://img0.baidu.com/it/u=3330672963,1063627283&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=281")

with open("美女.jpg", "wb") as f:
    f.write(res.content)
