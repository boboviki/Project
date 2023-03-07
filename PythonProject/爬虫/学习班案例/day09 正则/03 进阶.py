import re

# 案例1
# text = '<12> <xzy> <!@#$%> <1a!#e2> <>'
#
# # ret = re.findall("<\d+>", text)
# # ret = re.findall("<\w+>", text)
# ret = re.findall("<.+?>", text)
# ret = re.findall("<.*?>", text)
# print(ret)

# 案例2
text = """
<12
>

<x
 yz> 

 <!@#$%> 

 <1a!#
 e2> 

 <>
"""
# ret = re.findall("<.*?>", text)
ret = re.findall("<.*?>", text, re.S)

print(ret)
