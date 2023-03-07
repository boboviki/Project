# 序列化：  将某种编程语言支持的数据类型对象做一个格式化字符串，从而能够进行存储或网络传输
# 反序列化: 将能够进行存储或网络传输的某种格式字符串转换成本编程语言能够识别的数据类型对象

# json: 标准的数据交换格式 "" 1 true false   []  {}  null
import json

# json.dumps()
# json.loads()

# data = {
#     1001: {"name": 'yuan'},
#     1002: {"name": "rain"}
# }
#
# dataJson = json.dumps(data)
# # print(dataJson,type(dataJson))
# print(repr(dataJson))


data = '{"name":"eric","age":22,"isMarried":false}'

ret = json.loads(data)
print(ret, type(ret))
print(ret["name"])

















