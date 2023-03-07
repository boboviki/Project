import openpyxl
# 创建一个工作簿对象
wb = openpyxl.load_workbook('./工作簿1.xlsx')
print(wb)
print(wb.sheetnames)#获取工作表名称