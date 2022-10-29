import cv2
import random
import numpy as np

image_path = 'C:\\images\\Etc_JPG(rectangle)\\'
imgList = ['airplane.jpg','flower01.jpg','flower02.jpg',
           'garden01.jpg','garden02.jpg','garden03.jpg',
           'garden04.jpg','garden05.jpg','garden06.jpg',
           'garden07.jpg','lake01.jpg','lake02.jpg',
           'lake03.jpg','lake04.jpg','night_flower01.jpg',
           'night_flower02.jpg','night_flower03.jpg','night_flower04.jpg',
           'night_flower05.jpg','night_flower06.jpg','night_flower07.jpg',
           'ocean01.jpg','ocean02.jpg','ocean03.jpg',
           'ocean04.jpg','ocean05.jpg','ocean06.jpg','sky01.jpg','tank.jpg']

filename = image_path + random.choice(imgList)


##OpenCV 함수 사용법
cvInPhoto = cv2.imread(filename)

#(1) GrayScale
# cvOutPhoto = cv2.cvtColor(cvInPhoto, cv2.COLOR_BGR2GRAY)

#(2) Embossing
# mask = np.zeros((3,3), np.float32)
# mask[0][0]  = -1.0;
# mask[2][2]  = 1.0;
# cvOutPhoto = cv2.filter2D(cvInPhoto, -1, mask)

#(3) Catoon
cvOutPhoto = cv2.cvtColor(cvInPhoto, cv2.COLOR_BGR2GRAY)
cvOutPhoto = cv2.medianBlur(cvOutPhoto, 7)
edigs = cv2.Laplacian(cvOutPhoto, cv2.CV_8U, ksize=5)
ret, mask = cv2.threshold(edigs, 100, 255, cv2.THRESH_BINARY_INV)
cvOutPhoto = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

cv2.imshow("Out",cvOutPhoto)
cv2.imshow("In",cvInPhoto)
cv2.waitKey()