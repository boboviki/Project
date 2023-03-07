from lxml import etree

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>AAA</b></p>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
selector = etree.HTML(html_doc)
print(type(selector))  # <class 'lxml.etree._Element'>
ret = selector.xpath("//a")
print(ret)  # v [<Element a at 0x7fc6e80d7f80>, <Element a at 0x7fc6e80d7fc0>, <Element a at 0x7fc6e80df040>]

for linkE in ret:
    name = linkE.xpath("./text()")[0]
    href = linkE.xpath("./@href")[0]
    print(name, href)
