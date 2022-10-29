
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
plt.style.use('dark_background')

# Read Input Image
img_ori = cv2.imread('/images/1.jpg')
#그래이 스케일 전환
gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)

# 이미지 사이즈 저장
height, width, channel = img_ori.shape

plt.figure(figsize=(12, 10))
plt.imshow(gray, cmap='gray')


# #   이미지 가우시안블러[노이즈 제거 효과]
# img_blurred = cv2.GaussianBlur(gray,ksize = (5,5), sigmaX=0)
#
# #   이미지 Threshold[검은색과 흰색으로 나눔]
# img_thresh = cv2.adaptiveThreshold(
#     img_blurred,
#     maxValue = 255.0,
#     adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#     thresholdType=cv2.THRESH_BINARY_INV,
#     blockSize=19,
#     c=19
# )
#
# #   이미지 윤곽선 찾기
# contours = cv2.findContours(
#     img_thresh,
#     mode=cv2.RETR_LIST,
#     method=cv2.CHAIN_APPROX_NONE
# )
#
# temp_resulot = np.zeros((height, width, channel), dtype = np.unit8)
#
# cv2.drawContours(temp_resulot, contours=contours, contourIdx=-1, color=(255,255,255))
#
# plt.figure(figsize = (12,10))
#
# plt.imshow(temp_resulot)