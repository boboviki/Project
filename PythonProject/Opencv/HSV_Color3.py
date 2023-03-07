# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

def nothing(x):
    pass


# 创建一副黑色图像
img = np.zeros((300, 512, 3), np.uint8)

# 设置滑动条组件
cv2.namedWindow('HSV_Window')
cv2.createTrackbar('H_L', 'HSV_Window', 0, 255, nothing)
cv2.createTrackbar('H_H', 'HSV_Window', 0, 255, nothing)
cv2.createTrackbar('S_L', 'HSV_Window', 0, 255, nothing)
cv2.createTrackbar('S_H', 'HSV_Window', 0, 255, nothing)
cv2.createTrackbar('V_L', 'HSV_Window', 0, 255, nothing)
cv2.createTrackbar('V_H', 'HSV_Window', 0, 255, nothing)

while (1):

    success, frame = camera.read()
    cv2.imshow("HSV_Window", frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 将读取的BGR转换为HSV

    H_L = cv2.getTrackbarPos('H_L', 'HSV_Window')
    H_H = cv2.getTrackbarPos('H_H', 'HSV_Window')
    S_L = cv2.getTrackbarPos('S_L', 'HSV_Window')
    S_H = cv2.getTrackbarPos('S_H', 'HSV_Window')
    V_L = cv2.getTrackbarPos('V_L', 'HSV_Window')
    V_H = cv2.getTrackbarPos('V_H', 'HSV_Window')


    lower = np.array([H_L, S_L, V_L])  # 所要检测的像素范围
    upper = np.array([H_H, S_H, V_H])  # 此处检测绿色区域

    mask = cv2.inRange(hsv, lowerb=lower, upperb=upper)
    cv2.imshow("mask", mask)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # sw = cv2.getTrackbarPos(switch, 'HSV_Window')

    # if s == 0:
    #     img[:] = 0
    # else:
    #     img[:] = [b, g, r]

# 销毁窗口
cv2.destroyAllWindows()
