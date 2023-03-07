import requests
import parsel #parsel是一个python的第三方库，相当于css选择器+xpath+re，相比于BeautifulSoup，xpath，parsel效率更高，使用更简单
import lxml

for page in range(1,11):
    print(f'===正在爬取第{page}页数据===') #f表示占位符,可以向{}中传数据
    url = f'https://ibaotu.com/tupian/{page}/'

    # 1、找到数据对应链接
    # url = 'https://ibaotu.com/tupian/3/'
    #准备一个请求的伪装 user-agent代表浏览器的身份标识
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

    #2.python发送指定地址的请求 requests
    response=requests.get(url=url,headers=headers)
    # print(response) 返回的是<Response [200]>，对象
    html =response.text #text 取对象的文本数据  字符串--》正则表达式
    # print(html)#获取到了返回的源代码数据，下一步需要解析
    #数据解析工具 parsel
    #3.解析出来（想要的数据） 请求到的是html数据，xpath css选择器专门提取html数据
    selector = parsel.Selector(html) #转化数据类型，论是使用css选择器，还是xpath，re，都需要先创建一个parsel.Selector对象
    lis = selector.xpath('//div[@class="term-list"]/div') #得到了该页面所有标签，可通过浏览器插件xpath helper
    #获取了该页面所有标签，下面可通过循环获取
    for li in lis:
        pic_title = li.xpath('string(.)').get()
        pic_url = li.xpath('.//img/@src').get()
        # print( pic_title)  #//可以获取到所有图片名
        # print( pic_title,pic_url)#如摊位门头图片 //pic.ibaotu.com/01/83/81/534888piCyMH.jpg-0.jpg!w280
        pic_url='https:'+pic_url
        # pic_url=pic_url.split('_')[0]#split为分割符，按指定字符分割
        #请求图片数据,视频图片音频都属于二进制数据，需要用content属性提取二进制数据
        pic_data=requests.get(url=pic_url,headers=headers).content

    # 4.数据的保存
    #with open是对文件操作的方法
        with open('Picture\\'+pic_title+'.jpg',mode='wb') as f:
            f.write(pic_data)
            print('保存完成',pic_title)

    #os 目录操作模块
    #爬取慢的话可以采取多任务并发编程（多进程，多线程）