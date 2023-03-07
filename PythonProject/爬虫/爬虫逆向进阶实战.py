import lxpy
#lxpy 爬虫工具包,包含
# 时间处理，xml检查，html去除标签，jsonp格式化
# 正则xpath，生成随机ua，请求头字符串转字典等处理方法
#DateGo  时间类，包含 获取当前时间、获取当前 年，月，日
#       把时间戳 转换为 年月日时分 格式、负数时间戳转换/转换1970年之前的时间戳
#        把 年月日时分 转换为 时间戳格式、# 获取昨天开始的时间戳
#       两个时间的差 -> 秒，# 微博时间处理方法，转换为时间格式
#      优酷时间处理方法、当前时间和指定时间的差/-> 秒、   两个时间的差/-> 秒
#       分钟/小时/天 前/后 的时间


lxpy.DateGo.java_date()#java时间格式转pyth时间格式
lxpy.lxheader.get_ua() #user-agent转换?
lxpy.lxheader.copy_headers_dict()#随机生成user-agent?
lxpy.lxml_check.create_root_node()#对html数据进行检查，解决有时候在etree.HTML解析后html数据会丢失的问题,调用 create_root_node 方法，传入response.text即可
lxpy.lxtools.html_format()#工具方法，如字符串去除html标签，jsonp快速转json，在xpath中使用正则表达式，从url中快速提取params等
lxpy.cipher().morse_enc() #解密, 如凯撒密码莫斯密码等