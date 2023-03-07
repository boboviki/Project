import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://movie.douban.com/explore",
}

url = 'https://m.douban.com/rexxar/api/v2/movie/recommend?'

res = requests.get(
    url,
    headers=headers,
    params={  # 查询
        "count": "20",
        "tags": "悬疑"
    }
)
# print(res.text)
# 方式1：不推荐
# import json
# data = json.loads(res.text)
# print(data)
# print(type(data))
# 方式2：推荐
# print(res.json())
# print(type(res.json()))

# 解析数据

for item in res.json()["items"]:
    if item.get("title"):
        print(item.get("title"))
