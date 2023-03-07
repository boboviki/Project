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

# 查询儿子tag
# print(soup.p.contents)
# print(soup.p.children)
# print(list(soup.p.children))

# print(soup.body.contents)
# print(list(soup.p.descendants))

# print(soup.a.parent)
# print(soup.a.next_sibling.next_sibling.next_sibling)
# print(soup.a.next_sibling)
# print(type(soup.a.next_sibling))  # NavigableString
print(soup.a.previous_sibling)  # NavigableString
print(soup.a.previous_sibling.previous_sibling)  # NavigableString
