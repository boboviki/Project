#----------------爬取百度标题操作-----------------------------------------------#
from bs4 import BeautifulSoup
import requests
# req = requests.get('https://www.baidu.com')
# req.encoding ='utf-8'
# print(req.status_code)
# print(req.encoding)
# print(req.text)
# print(req.content)
#
# soup = BeautifulSoup(req.text,'lxml')
# #方式一：直接使用需要查找的标签名
# print(soup.title.string)
# #方式二：使用select方法选择需要查找的标签路径，路径可以通过后台复制
# print(soup.select('head > title')[0].text)

#----------------数据库操作-----------------------------------------------#
import pymysql
#返回一个conn对象，connect方法中包含了数据库连接的基本信息
# conn = pymysql.connect(host='localhost',user='root',password='ydm901030',port=3306)
# #使用conn对象的cursor方法建立对mysql的操作游标
# cursor = conn.cursor()
# #使用execute方法执行mysql指令
# cursor.execute('select version()')
# #使用fetchone()方法获取上一步获取数据的第一行
# data = cursor.fetchone()
# print('Database version：',data)
# # cursor.execute("create database testpc default character set utf8mb4")
# #关闭数据库，释放资源
# conn.close()

#----------------操作csv-----------------------------------------------#
import csv
# #读取数据
# filetouse = '一年级6班名单.csv'# 指定需要输出的csv名
# with open(filetouse,'r',encoding='utf-8-sig') as f: #使用with open()方法打开文件,filetouse为文件名，‘r’表示只读
#     # 如果产生非法字符\ufeff，可使用 utf-8-sig
#     r=csv.reader(f) #创建数据读取对象
#     file_header=next(r) #读取第一行的头部数据，并将焦点转到下一行
#     print(file_header)
#     for id,file_header_col in enumerate(file_header):
#         print(id,file_header_col)
#
#     for row in r:
#         if row[1]=='吴宇轩':
#             print(row)
#
# #写入数据
# with open(file_header,'a',encoding='utf-8-sig')as f:
#     wr=csv.writer(f)
#     wr.writerow(['写入的数据','第二列数据'])
#     wr.writerows(['多行写入','看一看'],['多行写入','看一看'])

# #----------------操作json-----------------------------------------------#
import json
# dict_content={"name":"jack"}
# with open('json文件写入.json','w')as f:
#     json.dump(dict_content,f)
# with open('json文件写入.json','r',encoding='utf-8-sig')as f:
#     str=f.read()
#     data=json.loads(str)
#     print(data)

db= pymysql.connect(host='localhost',user='root',password='ydm901030',port=3306,db='testpc')
cur=db.cursor()
cur.execute("drop table if exists employee")
sql="""create table 'employee'(
    'id' int(10) not null auto_increment,
    'first_name' char(20) not null,
    'last_name ' char(20) default null,
    'age' int(11) default null,
    'sex' char(1) default null,
    'income' float default null,
    primary key('id')
    ) ENGINE=InnoDB default charset = utf8mb4;"""
cur.execute(sql)
print("create tableSuccessfull.")
db.close()