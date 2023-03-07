import lxpy
import requests
import parsel
import io
import os
import re



#需解决登录问题
# 第一种、使用Session

# s=requests.Session()
# headers=lxpy.lxheader.get_ua()
# 登入URL
# login_url = 'https://center.iresearch.cn/loginbk.shtml'
# form_data = {
#     'ck': '',
#     'remember': 'true',
#     'name': '624376399@qq.com',
#     'password': 'ydm901030',
# }
# res=s.post(login_url,headers=headers,data=form_data)
# print(res.text)
# 目标URL

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Cookie':'Hm_lvt_c33e4c1e69eca76a2e522c20e59773f6=1677210716; iRsCookieId=55a52a48a50a52a49a50a53a49a49a52a50a50a48a51a50; nps-uuid=cpdNhWwTLarRhl3y6OKg8uLITWOH; iRsUserId=49a55a51a52a56a50a49; iRsUserGroup=48; iRsUserAccount=109a111a99a46a113a113a64a57a57a51a54a55a51a52a50a54; iRsUserPassword=48a51a48a49a48a57a109a100a121; iRsUserDate=51a48a48a50a48a50; iRsUserType=49; iRsUserName=; iRsUserNick=; iRsUserPhoto=103a112a106a46a120a116a47a115a101a103a97a109a105a47a101a100a117a108a99a110a105a47a110a99a46a104a99a114a97a101a115a101a114a105a46a110a109a117a108a111a99a47a47a58a112a116a116a104; Hm_lpvt_c33e4c1e69eca76a2e522c20e59773f6=1677224612',
}
# url="https://report.iresearch.cn/#"
# formurl_data = {
#     'work': 'csearch',
#     'vid': '0',
#     'sid': '2',
#     'yid': '2022',
# }
url2="https://report.iresearch.cn/common/page/rsprocess.ashx?work=csearch&vid=0&sid=2&yid=2022"
# respones=s.get(url,headers=headers)
respones=requests.get(url2,headers=headers)
# respones=s.post(url,headers=headers,data=formurl_data)
respones.encoding=("gb2312")#乱码，设置编码格式
# print(respones.text)
html=respones.text
selectors=parsel.Selector(html)
lis=selectors.xpath('//div[@class="txt"]//a')
# lis_name=selectors.xpath('//div[@class="txt"]//a/text()')
print(len(lis))
lis_name=lis.xpath('./text()').getall()
lis_url=lis.xpath('./@href').getall()
# print(lis_name)
for i in range(len(lis)):
    name=lis_name[i]
    name=re.sub(r'[:/\\?*“”<>|+"]', '_', name)
    resurl=lis_url[i]
    num=str(resurl)[-10:-6]
    url2=resurl.replace('://','3A')
    url3=url2.replace('/','2F')
    urlDown="https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid="+num+"&work=rdown&url="+url3
    # print(name,urlDown)
    fileData=requests.get(urlDown,headers=headers)
    if os.path.exists('调研报告\\'+"%s.PDF" % name):
        print(str(i)+"、"+name+"已存在")
    else:
       bytes_io = io.BytesIO(fileData.content)
       with open('调研报告\\'+"%s.PDF" % name.replace('/',''),mode='wb') as f:
            f.write(bytes_io.getvalue())
            print(str(i)+'、'+'%s.PDF,下载成功！' % name)


# lis=selectors.xpath('//ul[@id="ulroot3"]//li')
# print(len(lis))
# print(selectors)
#
# print(res)
#
# downurl="https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid="+num+"&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F"
# https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid=4125&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F202212%2F4125.shtml
# https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid=4126&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F202301%2F4126.shtml
# https://report.iresearch.cn/include/ajax/user_ajax.ashx?reportid=4131&work=rdown&url=https%3A%2F%2Freport.iresearch.cn%2Freport%2F202301%2F4131.shtml