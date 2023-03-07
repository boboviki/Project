# 编码
# 0000   0
# 0001   1
# 0010   2
# 0011   3
# 0100   4
# 0101   5
'''
B：byte：占8个比特为(8个b)
KB：1024B
MB：1024KB
GB：1024MB
TB：1024MB
'''

# 计算机的存储单位：字节 byte 8个比特为

# 01010101 01011010 100101010101010111111111011110101000000000101

# ASCII
# 00000000 @
# 00000001  #
# 00000010
# a
# ...
#
# 拉丁美洲：编码：扩展ASCII码
# 00000000 @
# 00000001  #
# 00000010
# a
# ...
# 10000000
# 拉丁
#
# 亚洲：
#
# 中国：常用汉子五千个：GBK
# GB232：两个字节代表一个符号
#
# 00000000
# 00000000 @
# 00000000
# 00000001  #
# 00000000
# 00000010
# a
# ...
# 00000000
# 10000000
# 拉丁
# 00000001
# 00000000
# 中
# 00000001
# 00000001
# 国
#
# 日本：几千个：编码
#
# 00000000
# 00000000 @
# 00000000
# 00000001  #
# 00000000
# 00000010
# a
# ...
# 00000000
# 10000000
# 拉丁
# 00000001
# 00000000
# 日文符号
#
# unicode
# 编码：世界统一：四个字节映射一个符号： 2
# 的32次方
#
# 00000000
# 00000000
# 00000000
# 00000000 @
# 00000000
# 00000000
# 00000000
# 00000001  #
# 00000000
# 00000000
# 00000000
# 00000010
# a
#
# # go的作者：rob：utf-8: 针对unicode动态伸缩
# # 针对ASCII符号用一个字节，其它单论，utf8一个汉字3个字节
# # i am 苑
#
# 我是苑老师 15
#          10
