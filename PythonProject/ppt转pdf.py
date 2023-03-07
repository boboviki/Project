import comtypes.client  # 导入需要用到的库
import os  # 这里需要用到一个新的库中的对象，我们要需要获得操作系统（operating system）的对象

input_path = "E:\\01 物联网\\05 专业课\\企业专业课08-《物联网web应用技术》\\PPT"  # 输入的文件夹
output_path = "E:\\01 物联网\\05 专业课\\企业专业课08-《物联网web应用技术》\\PPT\\pdf"   # 输出的文件夹，这俩可以不一样哈

input_files = os.listdir(input_path)  # 获取输入的文件夹里所有的ppt，得到了一个ppt列表
print(input_files)
powerpoint = comtypes.client.CreateObject("Powerpoint.Application")  # 打开ppt应用程序

for input_file_name in input_files:  # 循环遍历列表里每一个ppt
    if not input_file_name.lower().endswith((".ppt", ".pptx")):  # 略过末尾的文件名不是ppt的文件
        continue  # 这里的continue是跳过下面的代码，进入下一次循环的意思
    input_file_path = os.path.join(input_path, input_file_name)  # 把输入的文件名组合一下
    print(input_file_path)

    myppt = powerpoint.Presentations.Open(input_file_path)  # 用ppt应用程序打开我们的ppt文件
    file_name = os.path.splitext(input_file_name)[0]  # 获取ppt的名称，用splitext函数切割input_file_name，并访问第0个元素，即去“my.pptx”，去掉保留“my”
    output_file_path = os.path.join(output_path, file_name + ".pdf")  # 把输出文件名组合一下
    myppt.ExportAsFixedFormat(output_file_path, FixedFormatType=2, OutputType=1)  # 转存我们的ppt文件到pdf
    myppt.close()  # 关闭当前ppt

powerpoint.Quit()  # 关掉ppt程序