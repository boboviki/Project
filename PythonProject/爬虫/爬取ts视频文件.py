import requests
import re
import os

url_prifix = "https://xxx.sdhdbd1.com/52av/20210629/A%e5%9b%bd%e4%ba%a7%e8%87%aa%e6%8b%8d/%e8%ba%ab%e6%9d%90%e5%be%88%e6%98%af%e8%8b%97%e6%9d%a1%e9%98%b4%e6%af%9b%e5%a4%9a%e5%a4%9a%e6%8f%89%e5%a5%b6%e6%8e%b0%e7%a9%b4/SD/"

url = "https://xxx.sdhdbd1.com/52av/20210629/A%e5%9b%bd%e4%ba%a7%e8%87%aa%e6%8b%8d/%e8%ba%ab%e6%9d%90%e5%be%88%e6%98%af%e8%8b%97%e6%9d%a1%e9%98%b4%e6%af%9b%e5%a4%9a%e5%a4%9a%e6%8f%89%e5%a5%b6%e6%8e%b0%e7%a9%b4/SD/playlist.m3u8"
# 获取m3u8文件
res = requests.get(url).text
print(res)
# 正则提取内容
ts = re.findall(r"(\d+).ts", res, flags=re.S)
print(ts)
# 从网页上复制下来的请求头
headers = {
    'authority': 'xxx.sdhdbd1.com',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
}
for i in ts:
    # 拼接完整的ts文件下载链接
    u = url_prifix + i + ".ts"
    r = requests.get(url=u, headers=headers).content
    print(i, u)
    # 二进制写入到本地
    with open('./ts/' + i + '.ts', mode="wb") as file:
        file.write(r)
# 利用cmd命令将.ts文件合成为mp4格式
os.system("copy /b /ts/*.ts heel.mp4")
print("转换成功")


# import re
# import time
# import requests
# from bs4 import BeautifulSoup
# import os
#
# # m = 'https://tse2-mm.cn.bing.net/th/id/OIP-C.uihwmxDdgfK4FlCIXx-3jgHaPc?w=115&amp;h=183&amp;c=7&amp;r=0&amp;o=5&amp;pid=1.7'
# '''
# resp = requests.get(m)
# byte = resp.content
# print(os.getcwd())
# img_path = os.path.join(m)
# '''
#
#
# def main():
#     baseurl = 'https://cn.bing.com/images/search?q=%E6%83%85%E7%BB%AA%E5%9B%BE%E7%89%87&qpvt=%e6%83%85%e7%bb%aa%e5%9b%be%e7%89%87&form=IGRE&first=1&cw=418&ch=652&tsc=ImageBasicHover'
#     datalist = getdata(baseurl)
#
#
# def getdata(baseurl):
#     Img = re.compile(r'img.*src="(.*?)"')  # 正则表达式匹配图片
#     datalist = []
#     head = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"}
#     response = requests.get(baseurl, headers=head)  # 获取网页信息
#     html = response.text  # 将网页信息转化为text形式
#     soup = BeautifulSoup(html, "html.parser")  # BeautifulSoup解析html
#     # i = 0  # 计数器初始值
#     data = []  # 存储图片超链接的列表
#     for item in soup.find_all('img', src=""):  # soup.find_all对网页中的img—src进行迭代
#         item = str(item)  # 转换为str类型
#         Picture = re.findall(Img, item)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接
#         for b in Picture:  # 遍历列表，取最后一次结果
#             data.append(b)
#             # i = i + 1
#             datalist.append(data[-1])
#     return datalist  # 返回一个包含超链接的新列表
#     # print(i)
#
#
# '''
# with open("img_path.jpg","wb") as f:
#     f.write(byte)
# '''
#
# if __name__ == '__main__':
#     os.chdir("D://情绪图片测试")
#
#     main()
#     i = 0  # 图片名递增
#     for m in getdata(
#             baseurl='https://cn.bing.com/images/search?q=%E6%83%85%E7%BB%AA%E5%9B%BE%E7%89%87&qpvt=%e6%83%85%e7%bb%aa%e5%9b%be%e7%89%87&form=IGRE&first=1&cw=418&ch=652&tsc=ImageBasicHover'):
#         resp = requests.get(m)  # 获取网页信息
#         byte = resp.content  # 转化为content二进制
#         print(os.getcwd())  # os库中输出当前的路径
#         i = i + 1  # 递增
#         # img_path = os.path.join(m)
#         with open("path{}.jpg".format(i), "wb") as f:  # 文件写入
#             f.write(byte)
#             time.sleep(0.5)  # 每隔0.5秒下载一张图片放入D://情绪图片测试
#         print("第{}张图片爬取成功!".format(i))




# #encoding:utf-8
# import urllib
# import re
#
# def getHtml(url):
#     response=urllib.urlopen(url)
#     html=response.read()
#     return html
#
# html=getHtml("https://test.mingrisoft.com/uploads/ebook/538/1.jpg")
#
# def getImg(html):
#     reg=r'src="(.+?.jpg)"width'
#     imgre=re.compile(reg)
#     imglist=re.findall(imgre.html)
#     x=0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl,'%s.jpg'%x)
#         x+=1
#
# getImg(html)

#
# 请求网址: https://test.mingrisoft.com/uploads/ebook/538/6.jpg
# 请求方法: GET
# 状态代码: 200 OK （来自内存缓存）
# 远程地址: 182.92.215.212:443
# 引荐来源网址政策: strict-origin-when-cross-origin
# Accept-Ranges: bytes
# Connection: Keep-Alive
# Content-Length: 543536
# Content-Type: image/jpeg
# Date: Tue, 31 May 2022 05:29:58 GMT
# ETag: "84b30-5a1e7b97c4640"
# Keep-Alive: timeout=5, max=100
# Last-Modified: Sat, 28 Mar 2020 10:31:45 GMT
# Server: Apache/2.4.37 (Unix) OpenSSL/1.0.2q mod_fcgid/2.3.9 PHP/5.6.40 mod_perl/2.0.8-dev Perl/v5.16.3
# 显示的是预配标头。停用缓存即可查看完整标头。
# 了解详情
# Referer: https://www.mingrisoft.com/
# sec-ch-ua: "Chromium";v="21", " Not;A Brand";v="99"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36