'''

영상처리 소프트웨어에 하르케스케이드(머신러닝)메뉴 추가
    --> 얼굴인식 메뉴 추가하고, 구현
    --> 코인식 메뉴 추가하고, 구현
    --> 귀인식 메뉴 추가하고, 구현
    --> 고양이 얼굴 인식 메뉴 추가

'''
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
import cv2
import numpy
## 함수 선언부
def malloc(h, w, value=0) :
    retMemory = [ [ value for _ in range(w)]  for _ in range(h) ]
    return retMemory

def mallocNumpy(t, h, w):
    retMemory = np.zeros((t, h, w), dtype=np.int16)
    return retMemory

def allocateOutMemory() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    # outImage = []
    # for _ in range(RGB) :
    #     outImage.append(malloc(outH, outW))
    outImage = mallocNumpy(RGB, outH, outW)

def openFile() :
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
            inImage[R][i][k] = cvInImage.item(i, k ,B)
            inImage[G][i][k] = cvInImage.item(i, k, G)
            inImage[B][i][k] = cvInImage.item(i, k, R)

    equalColor()

import numpy as np
def saveImage() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == None or filename == '' :
        return

    saveCvPhoto = np.zeros((outH, outW, 3), np.uint8)
    for i in range(outH) :
        for k in range(outW) :
            tup = tuple(([outImage[B][i][k],outImage[G][i][k],outImage[R][i][k]]))
            saveCvPhoto[i,k] = tup

    saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='.', filetypes=(("그림 파일", "*.png;*.jpg;*.bmp;*.tif"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    cv2.imwrite(saveFp.name, saveCvPhoto)


def displayImageColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if canvas != None :
        canvas.destroy()

    VX, VY = 512, 512 # 최대 화면 크기
    ## 크기가 512보다 크면, 최대 512로 보이기....
    if outH <= VY or outW <= VX :
        VX = outW
        VY = outH
        step = 1
    else :
        if outH > outW:
            step = outH / VY
            VX = int(VY * outW / outH)
        else:
            step = outW / VX
            VY = int(VX * outH / outW)

    window.geometry(str(int(VX*1.2)) + 'x' + str(int(VY*1.2)))
    canvas = Canvas(window, height=VY, width=VX)
    paper = PhotoImage(height=VY, width=VX)
    canvas.create_image((VX // 2, VY // 2), image=paper, state='normal')
    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름
    import numpy
    rgbString =""
    for i in numpy.arange(0,outH,step) :
        tmpString = "" # 각 줄
        for k in numpy.arange(0, outW, step) :
            i=int(i); k = int(k)
            r = outImage[R][i][k]
            g = outImage[G][i][k]
            b = outImage[B][i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack(expand=1, anchor=CENTER)
    status.configure(text='이미지정보:' + str(outH) + 'x' + str(outW)+'      '+filename)


###### 영상 처리 함수 ##########
def equalColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW
    ## 출력이미지 메모리 할당

    # outImage = []
    # for _ in range(RGB) :
    #     outImage.append(malloc(outH, outW))
    #outImage = allocateOutMemory()
    ### 진짜 영상처리 알고리즘 ###
    # for rgb in range(RGB):
    #     for i in range(inH):
    #         for k in range(inW):
    #             outImage[rgb][i][k] = inImage[rgb][i][k]
    outImage = inImage.copy()
    ########################
    displayImageColor()

### OpenCV 용 함수 모음 ###
def cvOut2outImage() : # OpenCV의 결과 --> OutImage 메모리에 넣기
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    ## 결과 메모리의 크기
    outH = cvOutImage.shape[0]
    outW = cvOutImage.shape[1]
    ## 입력이미지용 메모리 할당
    outImage = []
    for _ in range(RGB) :
        outImage.append(malloc(outH, outW))
    ## cvOut --> 메모리
    for i in range(outH):
        for k in range(outW):
            if (cvOutImage.ndim == 2) : # 그레이, 흑백
                outImage[R][i][k] = cvOutImage.item(i, k)
                outImage[G][i][k] = cvOutImage.item(i, k)
                outImage[B][i][k] = cvOutImage.item(i, k)
            else :
                outImage[R][i][k] = cvOutImage.item(i, k ,B)
                outImage[G][i][k] = cvOutImage.item(i, k, G)
                outImage[B][i][k] = cvOutImage.item(i, k, R)

def grayscale_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None :
        return
    ##### OpenCV 용 영상처리 ###
    cvOutImage = cv2.cvtColor(cvInImage, cv2.COLOR_BGR2GRAY)
    cvOut2outImage()
    ########################
    displayImageColor()

def cartoon_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None :
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

def faceDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None :
        return
    ##### OpenCV 용 영상처리 ###

    #   xml파일을 읽어 CascadeClassifier객체 생성
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    print('face_cascade : ',face_cascade)

    #cv2.cvtcolor(원본 이미지, 색상 변환 코드)
    # a[:]와 같이 시작 인덱스와 끝 인덱스를 둘다 생략하면 리스트 전체를 가져옵니다.
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)

    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.3, 5)
    print('fact_rects : ',fact_rects)
    for x, y, w, h in fact_rects:

        # cv2.rectangle(이미지 파일, 시작점(x, y),종료점(x + h, y + w), color(0, 255, 0, 선두께)
        cv2.rectangle(cvOutImage, (x, y), (x + h, y + w), (0, 255, 0), 3)

    cvOut2outImage()
    ########################
    displayImageColor()

def noseDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    face_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)
    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.1, 5)
    for x, y, w, h in fact_rects:
        cv2.rectangle(cvOutImage, (x, y), (x + h, y + w), (0, 255, 0), 3)

    cvOut2outImage()
    ########################
    displayImageColor()

def earDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    face_cascade = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml')
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)
    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.1, 5)
    for x, y, w, h in fact_rects:
        cv2.rectangle(cvOutImage, (x, y), (x + h, y + w), (0, 255, 0), 3)

    cvOut2outImage()
    ########################
    displayImageColor()

def catFaceDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None :
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


## 전역 변수부
window, canvas, paper = None, None, None
inImage, outImage = [], [];  inH, inW, outH, outW = [0] * 4
cvInImage, cvOutImage = None, None
filename = ''
RGB,R, G, B= 3, 0, 1, 2
# DB 관련
conn, cur = None, None
IP = '192.168.56.105'
USER = 'winUser'
PASSWORD = '4321'
DB = 'photo_db'
fileList = None


## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('QUIZE 2020-10-22')
    window.geometry('512x512')
    #window.resizable(height=False, width=False)
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

    '''
    영상처리 소프트웨어에 하르케스케이드(머신러닝)메뉴 추가
    --> 얼굴인식 메뉴 추가하고, 구현
    --> 코인식 메뉴 추가하고, 구현
    --> 귀인식 메뉴 추가하고, 구현
    --> 고양이 얼굴 인식 메뉴 추가
    '''

    harrCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="머신러닝", menu=harrCVMenu)
    harrCVMenu.add_command(label="하르케스케이드(얼굴)", command=faceDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(코)", command=noseDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(귀)", command=earDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(고영희씨)", command=catFaceDetect_CV)


    ######################

    window.mainloop()
