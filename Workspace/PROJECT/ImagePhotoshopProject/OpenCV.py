from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
import cv2
import numpy


## 함수 선언부
def malloc(h, w, value=0):
    retMemory = [[value for _ in range(w)] for _ in range(h)]
    return retMemory


def mallocNumpy(t, h, w):
    retMemory = np.zeros((t, h, w), dtype=np.int16)
    return retMemory


def allocateOutMemory():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    # outImage = []
    # for _ in range(RGB) :
    #     outImage.append(malloc(outH, outW))
    outImage = mallocNumpy(RGB, outH, outW)


def openFile():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    ## 파일 선택하기
    filename = askopenfilename(parent=window,
                               filetypes=(('Color 파일', '*.jpg;*.png;*.bmp;*.tif'), ('All File', '*.*')))
    ## (중요!) 입력이미지의 높이와 폭 알아내기
    cvInImage = cv2.imread(filename)
    inH = cvInImage.shape[0]
    inW = cvInImage.shape[1]
    ## 입력이미지용 메모리 할당
    # inImage = []
    # for _ in range(RGB) :
    #     inImage.append(malloc(inH, inW))
    inImage = mallocNumpy(RGB, inH, inW)
    ## 파일 --> 메모리 로딩

    for i in range(inH):
        for k in range(inW):
            inImage[R][i][k] = cvInImage.item(i, k, B)
            inImage[G][i][k] = cvInImage.item(i, k, G)
            inImage[B][i][k] = cvInImage.item(i, k, R)

    equalColor()


import numpy as np


def saveImage():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == None or filename == '':
        return

    saveCvPhoto = np.zeros((outH, outW, 3), np.uint8)
    for i in range(outH):
        for k in range(outW):
            tup = tuple(([outImage[B][i][k], outImage[G][i][k], outImage[R][i][k]]))
            saveCvPhoto[i, k] = tup

    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='.',
                           filetypes=(("그림 파일", "*.png;*.jpg;*.bmp;*.tif"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    cv2.imwrite(saveFp.name, saveCvPhoto)


def displayImageColor():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if canvas != None:
        canvas.destroy()

    VX, VY = 512, 512  # 최대 화면 크기
    ## 크기가 512보다 크면, 최대 512로 보이기....
    if outH <= VY or outW <= VX:
        VX = outW
        VY = outH
        step = 1
    else:
        if outH > outW:
            step = outH / VY
            VX = int(VY * outW / outH)
        else:
            step = outW / VX
            VY = int(VX * outH / outW)

    window.geometry(str(int(VX * 1.2)) + 'x' + str(int(VY * 1.2)))
    canvas = Canvas(window, height=VY, width=VX)
    paper = PhotoImage(height=VY, width=VX)
    canvas.create_image((VX // 2, VY // 2), image=paper, state='normal')
    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름
    import numpy
    rgbString = ""
    for i in numpy.arange(0, outH, step):
        tmpString = ""  # 각 줄
        for k in numpy.arange(0, outW, step):
            i = int(i);
            k = int(k)
            r = outImage[R][i][k]
            g = outImage[G][i][k]
            b = outImage[B][i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack(expand=1, anchor=CENTER)
    status.configure(text='이미지정보:' + str(outH) + 'x' + str(outW) + '      ' + filename)


###### 영상 처리 함수 ##########
def equalColor():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당

    # outImage = []
    # for _ in range(RGB) :
    #     outImage.append(malloc(outH, outW))
    # outImage = allocateOutMemory()
    ### 진짜 영상처리 알고리즘 ###
    # for rgb in range(RGB):
    #     for i in range(inH):
    #         for k in range(inW):
    #             outImage[rgb][i][k] = inImage[rgb][i][k]
    outImage = inImage.copy()
    ########################
    displayImageColor()


import time


def reverseColor():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    # value = askinteger("밝게하기", "값")
    # if value == None :
    #     return
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = 255 - inImage[rgb][i][k]
    ########################
    displayImageColor()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text"))


def reverseColor_NP():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    # value = askinteger("밝게하기", "값")
    # if value == None :
    #     return
    outImage = 255 - inImage
    ########################
    displayImageColor()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text"))


def addColor():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("밝게하기", "값")
    if value == None:
        return
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                out = inImage[rgb][i][k] + value
                if out > 255:
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = out
    ########################
    displayImageColor()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text"))


def addColor_NP():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("밝게하기", "값")
    if value == None:
        return
    inImage = inImage.astype(np.int16)
    outImage = inImage + value

    # 조건으로 범위 지정
    outImage = np.where(outImage > 255, 255, outImage)
    outImage = np.where(outImage < 0, 0, outImage)
    ########################
    displayImageColor()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text"))


def grayColor():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            c = inImage[R][i][k] + inImage[G][i][k] + inImage[B][i][k]
            c = int(c / 3)
            outImage[R][i][k] = outImage[G][i][k] = outImage[B][i][k] = c
    ########################
    displayImageColor()


### OpenCV 용 함수 모음 ###
def cvOut2outImage():  # OpenCV의 결과 --> OutImage 메모리에 넣기
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    ## 결과 메모리의 크기
    outH = cvOutImage.shape[0]
    outW = cvOutImage.shape[1]
    ## 입력이미지용 메모리 할당
    outImage = []
    for _ in range(RGB):
        outImage.append(malloc(outH, outW))
    ## cvOut --> 메모리
    for i in range(outH):
        for k in range(outW):
            if (cvOutImage.ndim == 2):  # 그레이, 흑백
                outImage[R][i][k] = cvOutImage.item(i, k)
                outImage[G][i][k] = cvOutImage.item(i, k)
                outImage[B][i][k] = cvOutImage.item(i, k)
            else:
                outImage[R][i][k] = cvOutImage.item(i, k, B)
                outImage[G][i][k] = cvOutImage.item(i, k, G)
                outImage[B][i][k] = cvOutImage.item(i, k, R)


def grayscale_CV():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    cvOutImage = cv2.cvtColor(cvInImage, cv2.COLOR_BGR2GRAY)
    cvOut2outImage()
    ########################
    displayImageColor()


def cartoon_CV():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    cvOutImage = cv2.cvtColor(cvInImage, cv2.COLOR_RGB2GRAY)
    cvOutImage = cv2.medianBlur(cvOutImage, 7)
    edges = cv2.Laplacian(cvOutImage, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
    cvOutImage = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    cvOut2outImage()
    ########################
    displayImageColor()


def faceDetect_CV():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)
    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.1, 5)
    for x, y, w, h in fact_rects:
        cv2.rectangle(cvOutImage, (x, y), (x + h, y + w), (0, 255, 0), 3)

    cvOut2outImage()
    ########################
    displayImageColor()


def catFaceDetect_CV():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)
    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.1, 5)
    for x, y, w, h in fact_rects:
        cv2.rectangle(cvOutImage, (x, y), (x + h, y + w), (0, 255, 0), 3)

    cvOut2outImage()
    ########################
    displayImageColor()


def ssdNet(image):
    CONF_VALUE = 0.8  # 20% 인정
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
    net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
    (h, w) = image.shape[:2]

    print('image.shape[:2]:', image.shape[:])

    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > CONF_VALUE:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            cv2.rectangle(image, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    return image


def deepStopImage_CV():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    cvOutImage = ssdNet(cvInImage)

    cvOut2outImage()
    ########################
    displayImageColor()


# 영상
def deepMoveImage_CV():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList

    movieName = askopenfilename(parent=window,
                                filetypes=(('동영상 파일', '*.mp4;*.avi'), ('All File', '*.*')))
    s_factor = 0.5  # 화면 크기 비율(조절 가능)

    # cv2.VideoCapture("동영상 경로") : 프레임 단위로 저장
    capture = cv2.VideoCapture(movieName)

    frameCount = 0  # 처리할 프레임의 숫자 (자동증가)
    ##### OpenCV 용 영상처리 ###
    while True:
        ret, frame = capture.read()
        if not ret:  # 동영상을 읽기 실패
            break
        frameCount += 1
        if frameCount % 10 == 0:  # 숫자 조절 가능 (속도 문제)
            frame = cv2.resize(frame, None, fx=s_factor, fy=s_factor, interpolation=cv2.INTER_AREA)
            ## 1장짜리 SSD 딥러닝 ##
            retImage = ssdNet(frame)
            ####################
            cv2.imshow('Video', retImage)

        # 입력한숫자ms마다 프레임을 재생합니다.
        key = cv2.waitKey(1)  # 화면 속도 조절

        if key == 27:  # esc 키
            break
        elif key == ord('c') or key == ord('C'):
            # 키보드가 아닌, 조건에 의해서 처리도 가능함...
            # 예로 사람이 3명이상 등장하면......  강아지가 나타나면...
            cvInImage = cvOutImage = retImage
            filename = movieName
            cvOut2outImage()
            displayImageColor()

    capture.release()
    # cv2.destroyAllWindows()
    ########################
    # displayImageColor()


# 영상

def deepMoveImage_CV2():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList

    movieName = askopenfilename(parent=window,
                                filetypes=(('동영상 파일', '*.mp4;*.avi'), ('All File', '*.*')))
    s_factor = 0.5  # 화면 크기 비율(조절 가능)

    # cv2.VideoCapture("동영상 경로") : 프레임 단위로 저장
    capture = cv2.VideoCapture(movieName)

    frameCount = 0  # 처리할 프레임의 숫자 (자동증가)
    ##### OpenCV 용 영상처리 ###
    while True:
        ret, frame = capture.read()
        if not ret:  # 동영상을 읽기 실패
            break
        frameCount += 1
        # print('frameCount:',frameCount)
        # 영상 프레임 = 이미지
        frame = cv2.resize(frame, None, fx=s_factor, fy=s_factor, interpolation=cv2.INTER_AREA)

        ## 1장짜리 SSD 딥러닝 ##
        retImage = ssdNet(frame)
        cvInImage = retImage
        ####################
        cvOutImage = cv2.cvtColor(cvInImage, cv2.COLOR_RGB2GRAY)
        cvOutImage = cv2.medianBlur(cvOutImage, 7)
        edges = cv2.Laplacian(cvOutImage, cv2.CV_8U, ksize=5)
        ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
        cvOutImage = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

        retImage2 = cvOutImage
        cv2.imshow('VideoOriginal', retImage)
        cv2.imshow('Video', retImage2)
        # print('frame:',frame,'retImage:',retImage)
        # if frameCount % 10 == 0 : # 숫자 조절 가능 (속도 문제)

        # 입력한숫자ms마다 프레임을 재생합니다.
        key = cv2.waitKey(1)  # 화면 속도 조절

        if key == 27:  # esc 키
            break
        elif key == ord('c') or key == ord('C'):
            # 키보드가 아닌, 조건에 의해서 처리도 가능함...
            # 예로 사람이 3명이상 등장하면......  강아지가 나타나면...
            cvInImage = cvOutImage = retImage
            filename = movieName
            cvOut2outImage()
            displayImageColor()

    capture.release()
    # cv2.destroyAllWindows()
    ########################
    # displayImageColor()


## 전역 변수부
window, canvas, paper = None, None, None
inImage, outImage = [], [];
inH, inW, outH, outW = [0] * 4
cvInImage, cvOutImage = None, None
filename = ''
RGB, R, G, B = 3, 0, 1, 2
# DB 관련
conn, cur = None, None
IP = '192.168.56.105'
USER = 'winUser'
PASSWORD = '4321'
DB = 'photo_db'
fileList = None

## 메인 코드부
if __name__ == '__main__':
    window = Tk()
    window.title('칼라 영상처리 Ver 0.8(include 하르케스케이드)')
    window.geometry('512x512')
    # window.resizable(height=False, width=False)
    status = Label(window, text='이미지정보:', bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    ### 메뉴 만들기 ###
    mainMenu = Menu(window)
    window.configure(menu=mainMenu)

    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="열기(Open)", command=openFile)
    fileMenu.add_command(label="저장(Save)", command=saveImage)
    fileMenu.add_separator()
    fileMenu.add_command(label="닫기(Close)")

    openCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="OpenCV", menu=openCVMenu)
    openCVMenu.add_command(label="그레이 스케일", command=grayscale_CV)
    openCVMenu.add_command(label="카툰 이미지", command=cartoon_CV)

    harrCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="머신러닝", menu=harrCVMenu)
    harrCVMenu.add_command(label="하르케스케이드(얼굴)", command=faceDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(고영희씨)", command=catFaceDetect_CV)

    deepCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="딥러닝", menu=deepCVMenu)
    deepCVMenu.add_command(label="사물 인식(정지영상)", command=deepStopImage_CV)
    deepCVMenu.add_command(label="사물 인식(동영상)", command=deepMoveImage_CV)
    deepCVMenu.add_command(label="사물 인식(연습)", command=deepMoveImage_CV2)
    ######################

    window.mainloop()
