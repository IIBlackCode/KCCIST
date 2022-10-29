import cv2
def snapshot(f) :
    cv2.imwrite('traffic.png', f)

capture = cv2.VideoCapture('c:/images/movie/traffic.mp4')
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
while True :
    ret, frame = capture.read()
    if not ret : # 동영상을 읽기 실패
        break
    cv2.imshow('Video', frame)

    key = cv2.waitKey(20)
    if key == 27 : # esc 키
        break
    if key == ord('c')  or key == ord('C') :
        snapshot(frame)

capture.release()
cv2.destroyAllWindows()