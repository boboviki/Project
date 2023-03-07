import requests
from bs4 import BeautifulSoup

# 爬取小说资源的 URL
url = "https://fanqienovel.com/reader/7103120136252424708"

# 发送请求获取网页内容
response = requests.get(url)
html = response.text

# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(html, "html.parser")

# 获取小说的章节内容
chapters = soup.select(".content p")

# 将章节内容存储到列表中
text = []
for chapter in chapters:
    text.append(chapter.text)

# 将小说的章节内容拼接起来
novel = "\n".join(text)

# 将小说内容存储到文本文件中
with open("C:/Users/Administrator/Desktop/novel.txt", "w", encoding="utf-8") as f:
    f.write(novel)
