import urllib3
import requests
import io
from lxml import html
etree=html.etree
#爬取2022年职业大赛文档

# 带下载的文档链接
url = "http://jyt.jiangxi.gov.cn/art/2022/9/5/art_56952_4132818.html"
# 构造 header
send_headers = {
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
# # 首先访问文库官网，获取cookies，骗过防爬机制
res = requests.get(url)
res.encoding="utf-8" #编码方式
b=res.text  #获取源码文档
# print(b)
# links=re.findall('<a.*?>(.*?)</a>',b)
# print(links)
html=etree.HTML(b)#获取html源代码
href=html.xpath('//div[@class="slgk_zw"]//div[@id="zoom"]//p//a//@href')#通过正则，取出下载链接
name=html.xpath('//div[@class="slgk_zw"]//div[@id="zoom"]//p//a//text()')#过正则，取出文本值
print(href)
print(name)
save_path = 'C:/Users/Administrator/Desktop/'#设置保存路径
i=0
for i in range(len(name)-1):#开始遍历下载
    filename=name[i]#设置文件名
    print(filename)
    downurl="http://jyt.jiangxi.gov.cn/"+href[i]#设获取下载链接
    print(downurl)
    download_pdf=requests.get(downurl,headers=send_headers)#根据下载链接下载数据
    bytes_io=io.BytesIO(download_pdf.content)
    #数据抓取回来之后调用io模块将它转为二进制字节流形式保存起来，
    # 之后将文件名和文件的保存路径设置好就调用文件的写入方法将二进制字节流转码后写入到新的pdf文件中并保存。
    # 这样就完成了一个pdf文件的下载
    with open(save_path+"%s.PDF" % filename,mode='wb') as f:
        f.write(bytes_io.getvalue())
        print('%s.PDF,下载成功！' % (filename))
    i+=1


