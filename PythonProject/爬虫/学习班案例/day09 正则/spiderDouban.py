with open("豆瓣top250.html") as f:
    s = f.read()
# print(s)

import re

ret = re.findall('<li>.*?class="item">.*?<div class="info">.*?<div class="hd">.*?<span class="title">(.*?)</span>.*?<span class="rating_num".*?>(.+?)</span>', s, re.S)
print(ret)
print(len(ret))