import re

"""re.findall(正则模式, 文本)  基于正则模式查找所有匹配的文本内容"""
# part1: 通配符->.  字符集-> []
# ret1 = re.findall("a", "a,b,c,d,e,a")
# ret1 = re.findall(".", "a,b,c,d,e")
# ret1 = re.findall("a.b", "a,b,c,d,e,acb,abb,a\tb")
# ret1 = re.findall("[ace]", "a,b,c,d,e")
# ret1 = re.findall("a[bce]f", "af,abf,abbf,acef,aef,")
# ret1 = re.findall("[abcde]", "a,b,c,d,e")
# ret1 = re.findall("[a-zA-Z]", "a,b,c,d,e,A,B,C")
# ret1 = re.findall("[0-9]", "a,b,2,d,6,8,B,C")
# ret1 = re.findall("[^0-9]", "a,b,2,d,6,8,B,C")
# ret1 = re.findall("\d", "a,b,2,d,6,8,B,C")
# ret1 = re.findall("[a-zA-Z0-9]", "a,b,2,d,6,8,B,C")
# ret1 = re.findall("\w", "a,b,2,d,6,8,B,C")
#
# print(ret1)

# part2: 重复  + 1-多次   *  0-多次  ? [0 1]     {m,n}
# ret2 = re.findall("\d+", "a,b,2435676,d,6,888888888888888")  # 默认贪婪匹配
# print(ret2)
# 取消贪婪匹配  重复元字符加一个?，即取消贪婪匹配
# ret2 = re.findall("\d+?", "a,b,2435676,d,6,888888888888888")  # 默认贪婪匹配
# print(ret2)

# ret2 = re.findall("[0-9a-zA-Z_]", "apple,banana,orange,melon")
# ret2 = re.findall("\w", "apple,banana,orange,melon")
# ret2 = re.findall("\w+", "apple,banana,orange,melon")
# ret2 = re.findall("\w+?", "apple,banana,orange,melon")  # 取消贪婪匹配
# ret2 = re.findall("", "apple,banana,orange,melon")
# ret2 = re.findall("abc*", "abc,abcc,abe,ab")
# ret2 = re.findall("abc+", "abc,abcc,abe,ab")

# "ab"    "abc"   "abcc"  "abccc"  "abcccc"   ....
# ret2 = re.findall("abc*?", "abc,abccc,abe,ab")
# ret2 = re.findall("\w{6}", "apple,banana,orange,melon")
# ret2 = re.findall("abc??", "abc,abcc,abe,ab")
# print(ret2)


# part3: 位置元字符-> ^ $
# ret3 = re.findall("^\w+", "peach,34,banana,255,orange,65536")
# ret3 = re.findall("\w+$", "peach,34,banana,255,orange,65536")
# ret3 = re.findall("/goods/food/\d+", "/goods/food/1006")
# ret3 = re.findall("/goods/food/\d+", "/server/app01/goods/food/1006")
# ret3 = re.findall("/goods/food/\d+", "/goods/food/1006/aaa/bbb")
# ret3 = re.findall("^/goods/food/\d+$", "/goods/food/1006/aaa/bbb")
# ret3 = re.findall("^/goods/food/\d+$", "/server/app01/goods/food/1006")
# ret3 = re.findall("^/goods/food/\d+$", "/goods/food/1006")
#
# print(ret3)

# part4:
# | 指定原子或正则模式进行二选一或多选一
# () 具备模式捕获的能力，也就是优先提取数据的能力，通过(?:) 可以取消模式捕获
# ret4 = re.findall("\w+", ",apple,banana,peach,orange,melon,")  # 筛选出5个字符的单词
# ret4 = re.findall(",\w{5},", ",apple,banana,peach,orange,melon,")  # 筛选出5个字符的单词
# ret4 = re.findall(",(\w{5}),", ",apple,banana,peach,orange,melon,")  # 筛选出5个字符的单词
# ret4 = re.findall(",(\w{5}),", ",apple,banana,peach,orange,melon,")  # 筛选出5个字符的单词
#
# ret4 = re.findall("\w+@163.com", "123abc@163.com,....234xyz@qq.com,....")
# ret4 = re.findall("\w+@qq.com", "123abc@163.com,....234xyz@qq.com,....")
# ret4 = re.findall("\w+@\w+.com", "123abc@163.com,....234xyz@qq.com,....")
# ret4 = re.findall("\w+@\w+.com", "123abc@163.com,....234xyz@qq.com,...666abc@123.com ,,,")
# ret4 = re.findall("\w+@(?:163|qq).com", "123abc@163.com,....234xyz@qq.com,...666abc@123.com ,,,")
# print(ret4)
#


# ret = re.findall("\(abc\)", "(abc)....")
# print(ret)
ret = re.findall("a[bc]d", "abcd acd")

#  part5: 转义符号\的两个功能：
#  (1) 将一些普通符号赋予特殊功能  \d  [0-9]    \D [^0-9]  \w  [0-9a-zA-Z]
#  (2) 将特殊符号(元字符)取消其特殊功能   \* \. \+ \?

ret = re.findall("\*", "*** ???  ___  ")
print(ret)
ret4 = re.findall("\w+@(?:163|qq)\.com", "123abc@163?com,....234xyz@qq.com,...666abc@123.com ,,,")
print(ret4)

#   转义符-> \d \D  \w \W      \n    \s \S  \b \B
""" \b 1个单词边界原子 """
txt = "my name is nana. nihao,nana"
# ret = re.findall(r"na", txt)
# ret = re.findall(r"\bna\w+", txt)
ret = re.findall(r"\bna", txt)
print(ret)


ret = re.findall("\\\\", "\\")
ret = re.findall(r"\\", "\\")
print(ret)
'''
 re ("\\", "\")

'''

