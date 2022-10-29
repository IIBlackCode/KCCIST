import cv2

# face_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


frame = cv2.imread('c:/images/Solar.png')
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
##얼굴이 여러개면 여러개 찾기.
## 얼굴위치 사각형[[x1,y1,w,h],[x2,y2,w,h]...]
face_rects = face_cascade.detectMultiScale(grey,1.1,5)
print(face_rects)

for x,y,w,h,in face_rects :
    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('',frame)
c=cv2.waitKey()
cv2.destroyWindow()