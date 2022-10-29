import cv2

def snapshot(f) :
    cv2.imwrite('traffic.png',f)

capture = cv2.VideoCapture('C:/images/movie/traffic.mp4')
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
while True :
    # 동영상 끝날때까지 프레임을 읽어들인다.
    ret, frame = capture.read()

    #동영상 읽기 실패
    if not ret :
        cv2.imshow('Video', frame)

    #ESC키 입력시 종료
    key = cv2.waitKey(20)
    if key == 27:
        break
    #Capture 스탭샷
    if key == ord('c') or key == ord('C') :
        snapshot(frame)


capture.release()
cv2.destroyAllWindows()