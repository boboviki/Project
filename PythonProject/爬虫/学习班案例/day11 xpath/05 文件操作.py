# 一、读操作

# open("/Users/yuan/PycharmProjects/pythonProject/爬虫JS逆向SVIP01期/day11 xpath/豆瓣top250.html", mode="r")

# 文件句柄
# file = open("html文件/豆瓣top250.html", mode="r")

# 获取当前文件的所有数据
# print(file.read())
# print(file.read(3))
# print(file.read(4))
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# 循环高效获取数据
# for line in file:
#     print(line)

# file.close()

# 二、写文件

from lxml import etree

with open("html文件/豆瓣top250.html") as f:
    data = f.read()
# print(data)

selector = etree.HTML(data)
# rets = selector.xpath('//ol[@class="grid_view"]/li//div[@class="hd"]//span[@class="title"][1]/text()')
# print(rets)

rets = selector.xpath('//ol[@class="grid_view"]/li')
# print(rets)
infos = []
for item in rets:
    # print(item)
    name = item.xpath('./div//div[@class="hd"]//span[@class="title"][1]/text()')[0]
    rating_num = item.xpath('./div//div[@class="bd"]//span[@class="rating_num"][1]/text()')[0]
    comment_num = item.xpath('./div//div[@class="star"]//span[last()]/text()')[0]
    # print(name, rating_num, comment_num)
    info = (name, rating_num, comment_num)
    infos.append(info)

print(infos)

# w模式：覆盖写  a:追加写
import json

file = open("豆瓣优秀电影.json", mode="a")
infosStr = json.dumps(infos, ensure_ascii=False)
file.write("apple")
file.write("apple")
file.write("apple")
file.write("apple")
file.write("apple")

# file.flush()  # 把缓冲的数据更新到磁盘
# file.write(infosStr + "\n")
# file.close()

# import time
# time.sleep(1000)
