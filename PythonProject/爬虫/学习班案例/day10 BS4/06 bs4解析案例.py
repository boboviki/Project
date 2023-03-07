from bs4 import BeautifulSoup

# 方式1
# with open("豆瓣top250.html") as f:
#     data = f.read()
#
# print(data)
#
# BeautifulSoup(data, "html.parser")

# 方式2：
soup = BeautifulSoup(open("豆瓣top250.html"), "html.parser")

items = soup.find_all(class_="item")
# print(len(items))

for item in items:
    title = item.find(class_="title").text
    rating_num_tag = item.find(class_="rating_num")
    rating_num = rating_num_tag.text
    comment_num = rating_num_tag.find_next_sibling().find_next_sibling().text
    print(title, rating_num, comment_num)
