from PIL import Image, ImageFilter, ImageOps
import torch
img = Image.open('C:\\Users\\Administrator\\Desktop\\pp.png')
out = img.resize((1000,500),Image.ANTIALIAS)
#Image.NEAREST低质量；Image.BILINEAR双线性；Image.BICUBIC 三次样条插值；Image.ANTIALIAS高质量

def dodge(a, b, alpha):
    return min(int(a*255/(256-b*alpha)),255)

def draw(img,blur=26,alpha=1.0):
    img1 = img.convert('L') #图片转换成灰色
    img2 = img1.copy() #复制图片
    img2 = ImageOps.invert(img2) #实现二值图像的黑白翻转
    for i in range(blur): # blur模糊度
        img2 = img2.filter(ImageFilter.BLUR) #ImageFilter.BLUR为模糊滤波，处理之后的图像会整体变得模糊。
                                               #ImageFilter.CONTOUR为轮廓滤波，将图像中的轮廓信息全部提取出来。
    width, height = img1.size
    for x in range(width):
        for y in range( height) :
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), dodge(a, b, alpha)) #在指定位置上放一像素
    img1.show()
    img1.save( 'C:\\Users\\Administrator\\Desktop\\pp2.png')
draw(img)
