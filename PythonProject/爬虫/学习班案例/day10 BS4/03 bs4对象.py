from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<b>BBB</b>
<p class="title"><b>The Dormouse's story01</b><b>The Dormouse's story02</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>


"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.find_all("a"))


# (1) 查找标签
# print(soup.body)
# print(type(soup.body))
# print(soup.b)
# print(type(soup.b))
# print(soup.p.b)
# print(soup.p.a)
# 如果查到，一定是一个Tag对象

# (2) 获取标签信息
# print(soup.p.b.name)  # "b"
# print(soup.a.name)  # "a"
# print(soup.a["href"])  # http://example.com/elsie
# print(soup.a.attrs)  # {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
# print(soup.a.string)
# print(soup.a.text)

# print(soup.p.string)  # The Dormouse's story
# print(soup.p.text)  # The Dormouse's story


# 获取 文档的标签信息，构建 {a标签的文本:a的href作为值}


# ret = soup.find_all("a")
# d = {}
# for tag in ret:
#     val = tag.text
#     # h = tag["href"]
#     h = tag.attrs.get("href")
#     print(val, h)
#     d[val] = h
# print(d)

# 方式2
# print({tag.text: tag["href"] for tag in soup.find_all("a")})
