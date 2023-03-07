import requests
import lxpy
import parsel

url="https://wangxiao.xisaiwang.com/rk/xxzl/n132.html"
user_agent=lxpy.get_ua()

headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.1430.136 Safari/537.36',
    "cookie":"_sid_=98bfc88327bd94bf1f3ad8069f8fa69e; remark=%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99%E4%B8%8B%E8%BD%BD%E9%A1%B5; fcode1=203699; JESONG_USER_ID=01000000013264807456838572109451; enterPage=https%3A%2F%2Fwangxiao.xisaiwang.com%2Frk%2Fxxzl%2Fn101.html; mddcid=1678074568978rQP9sz; mddsync=1; mddldyurl=https%3A%2F%2Fwangxiao.xisaiwang.com%2Frk%2Fxxzl%2Fn101.html; Hm_lvt_4b9f46d3a269fb3925580a1827143bfb=1678074570; JESONG_VISITOR_ID=01000000013264807456838572109451; ListClassifyId=132; _subjectCode_=100110011004; fromUrl=https%3A%2F%2Fwangxiao.xisaiwang.com%2Frk%2Fxxzl%2Fn132.html; _rme=T; cstk=b7cf36196557bd31e63ea52cba915207; Hm_lpvt_4b9f46d3a269fb3925580a1827143bfb=1678074742; JESONG_AUTO_MON_TIMES=0",

}

res=requests.get(url,headers=headers)
html=res.text
selectors=parsel.Selector(html)
lis=selectors.xpath('//li[@class=" clearfix"]//a')
print(lis)
lisName=lis.xpath('./@contextparam').getall()
for i in range(len(lisName)):
    name=lisName[i]
    print(name)