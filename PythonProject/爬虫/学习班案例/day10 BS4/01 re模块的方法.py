import re

# (1) findall
# re.findall("", "")

# ret = re.findall(r"\d+", "apple 122 peach 34")
# # print(ret)


# (2) search
# ret = re.search(r"\d+", "apple 122 peach 34")
# print(ret)
# print(ret.span())  # (6, 9)
# print(ret.group())  # 122


# 有名分组
# ret = re.search("(?P<tel>1[3-9]\d{9}).*?(?P<email>\d+@qq\.com)", "我的手机号码是13928835900,我的邮箱是123@qq.com ...........  ")
# print(ret.group())
# print(ret.group("tel"))
# print(ret.group("email"))


# (3) match方法
# ret = re.match("1[3-9]\d{9}", "我的手机号码是13928835900,我女朋友的手机号 13122647238...........  ")
# print(ret)
#
# ret = re.match("1[3-9]\d{9}", "13928835900,我女朋友的手机号 13122647238...........  ")
# print(ret)
# print(ret.group())

# (4) split方法

# print("yuan rain alvin".split(" "))
# txt = "my  name        is    yuan"
# print(txt.split(" "))
# ret = re.split(r"\s+", txt)
# print(ret)
#
# # (5) sub/subn
# print("12 34 56 88".replace("88", "yuan"))
# s = "12 34 56 88"
# ret = re.sub(r"\d+", "yuan", s, 2)
# print(ret)

# (6) compile 编译
# s1 = "12 apple 34 peach 77 banana"
# ret = re.findall(r"\d+", s1)
# print(ret)
#
# s2 = "22 apple 33 peach 44 banana"
# ret = re.findall(r"\d+", s2)
# print(ret)

# s1 = "12 apple 34 peach 77 banana"
# s2 = "22 apple 33 peach 44 banana"
#
# reg = re.compile("\d+")
#
# print(reg.findall(s1))
# print(reg.findall(s2))


# 补充raw-string  : 原生字符串

# ret = re.findall(r"\a","")
# print(ret)








