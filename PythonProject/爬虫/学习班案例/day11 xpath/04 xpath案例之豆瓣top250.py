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
