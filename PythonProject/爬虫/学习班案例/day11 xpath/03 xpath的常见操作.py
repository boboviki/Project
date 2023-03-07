from lxml import etree

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>AAA</b></p>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister c1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="c2 sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

selector = etree.HTML(html_doc)
# ret = selector.xpath("//a/text()")
# ret = selector.xpath("//a[1]/text()")
# ret = selector.xpath("//a[1]/@href")
# ret = selector.xpath("//a/@href")
# ret = selector.xpath("//a/@class")
# ret = selector.xpath("//a/@id")
# ret = selector.xpath('//a[@class="sister"]')
# ret = selector.xpath('//a[contains(@class,"sister")]')
# ret = selector.xpath('//a[starts-with(@class,"sister")]')
# print(ret)
