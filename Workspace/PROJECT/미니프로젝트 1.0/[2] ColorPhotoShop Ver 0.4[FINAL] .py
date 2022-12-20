from builtins import print
from ctypes.wintypes import RGB
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
#cd2 외부 라이브러리 설치 필요
#cmd > pip install opencv-python
import cv2
import numpy
import numpy as np
## 함수선언부
from sympy import primenu


def malloc(h, w, value=0) :
    retMemory = [ [ value for _ in range(w)]  for _ in range(h) ]
    return retMemory

def openFile() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run openFile() Method ...')
    ## 파일 선택하기
    filename = askopenfilename(parent=window, filetypes=(('Color 파일', '*.jpg;*.png;*.bmp;*.tif'), ('All File', '*.*')))

    ## (중요!) 입력이미지의 높이와 폭 알아내기

    # fsize = os.path.getsize(filename)
    # inH = inW = int(math.sqrt(fsize))
    cvInImage = cv2.imread(filename)
    print('cvInImage.shape :',cvInImage.shape)
    inH = cvInImage.shape[0]
    inW = cvInImage.shape[1]

    ## 입력이미지용 메모리 할당
    inImage = []
    for _ in range(RGB): #칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        inImage.append(malloc(inH, inW))

    ## 파일 --> 메모리 로딩
    #cv는 한 픽셀값에 rgb값이 들어있어 3차원배열이 아닌 2차원배열로 만들어야한다.
    # with open(filename,'rb') as fp :
    # for rgb in range(RGB) :

    for i in range(inH):
        for k in range(inW):
            inImage[R][i][k] = cvInImage.item(i, k, B)
            inImage[G][i][k] = cvInImage.item(i, k, G)
            inImage[B][i][k] = cvInImage.item(i, k, R)
    equalColor()

def saveFile() :
    # global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    # global cvInImage, cvOutImage
    # if filename == None or filename == '' :
    #     return
    #
    # saveCvPhoto = np.zeros((outH, outW, 3), np.uint8)
    #
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tup = tuple(([outImage[B][i][k],outImage[G][i][k],outImage[R][i][k]]))
    #         saveCvPhoto[i,k] = tup
    #
    # saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='.', filetypes=(("그림 파일", "*.png;*.jpg;*.bmp;*.tif"), ("모든 파일", "*.*")))
    #
    # if saveFp == '' or saveFp == None:
    #     return
    # cv2.imwrite(saveFp.name, saveCvPhoto)

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

def roolback() : # 실행취소
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    global beforeImage, afterImage
    print('Run roolback() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH
    outW = inW

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = beforeImage[rgb][i][k]

    ########################
    displayImageColor()

def restart() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    global beforeImage, afterImage
    print('Run restart() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = afterImage[rgb][i][k]

    ########################
    displayImageColor()

def displayImageColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run displayImageColor() Method ...')

    # canvas의 크기에 따라 윈도우의 크기 변환 > 없어도 자동적으로 변환된다.
    window.geometry(str(outH) + 'x' + str(outW))
    if canvas != None:
        canvas.destroy()
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)

    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal')

    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름
    rgbString = ""
    for i in range(outH):
        tmpString = ""  # 각 줄
        for k in range(outW):
            r = outImage[R][i][k]
            g = outImage[G][i][k]
            b = outImage[B][i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack()

#영상처리 함수 영역
#============================================== [1]. 화소점 처리 ==============================================
def equalColor() :

    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()

def addColor() :
    print('Run addColor() Method ...')
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    global beforeImage, afterImage
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB) :
        outImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("밝게하기", "값")
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                out = inImage[rgb][i][k] + value
                if out > 255 :
                    outImage[rgb][i][k] = 255
                else :
                    outImage[rgb][i][k] = out

    ########################
    if beforeImage == []:
        beforeImage = inImage
        afterImage = outImage
        print('beforeImage == [] :')
    else:
        beforeImage = afterImage
        afterImage = outImage
        print('beforeImage != [] :', afterImage)
    displayImageColor()

def grayColor() :
    print('Run grayColor() Method ...')
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    global beforeImage, afterImage
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB) :
        outImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            c = inImage[R][i][k] + inImage[G][i][k] + inImage[B][i][k]
            c = int(c/3)
            outImage[R][i][k] = outImage[G][i][k] = outImage[B][i][k] = c
    ########################
    if beforeImage == [] :
        beforeImage = inImage
        afterImage = outImage
        print('beforeImage == [] :')
    else :
        beforeImage = afterImage
        afterImage = outImage
        print('beforeImage != [] :', afterImage)
    displayImageColor()

def gammaColor() :  # 감마
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):
        outImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###
    ### Out = I ** (1/r)

    r = askfloat("감마연산", "값[0.8~1.2]-->", )
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # outImage[rgb][i][k] = inImage[rgb][i][k]

                v = int(inImage[rgb][i][k] ** (1 / r));
                # print(rgb, i, k, v,'<<',inImage[rgb][i][k])
                if v > 255:
                    outImage[rgb][i][k] = 255;
                elif v < 0:
                    outImage[rgb][i][k] = 0;
                else:
                    outImage[rgb][i][k] = int(inImage[rgb][i][k] ** (1 / r));
    ########################
    displayImageColor()

def paraCapColor() :  # 파라볼라 캡
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):
        outImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2
    for rgb in range(RGB):
        for i in range(inH) :
            for k in range(inW) :
                v = 255.0*((inImage[rgb][i][k]/128.0-1.0) ** 2);
                if v > 255 :
                    outImage[rgb][i][k] = 255;
                elif v < 0 :
                    outImage[rgb][i][k] = 0;
                else :
                    outImage[rgb][i][k] = int(v);
    ########################
    displayImageColor()

def paraCupColor() :  # 파라볼라 컵 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):
        outImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2
    for rgb in range(RGB):
        for i in range(inH) :
            for k in range(inW) :
                v = 255-255.0*((inImage[rgb][i][k]/128.0-1.0) ** 2);
                if v > 255 :
                    outImage[rgb][i][k] = 255;
                elif v < 0 :
                    outImage[rgb][i][k] = 0;
                else :
                    outImage[rgb][i][k] = int(v);
    ########################
    displayImageColor()

def bw1Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run bw1Color() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] < 127:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = 255
    ########################
    displayImageColor()

def bw2Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run bw2Color() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 이진화(평균) 알고리즘 ###
    sum = 0;
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                sum += inImage[rgb][i][k];
    avg = sum/(rgb*inH*inW)

    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] < avg:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = 255
    ########################
    displayImageColor()

def bw3Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run bw3Color() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 이진화(중위수) 알고리즘 ###
    tmpArray = []
    sum = 0;
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                tmpArray.append(inImage[rgb][i][k])

    tmpArray.sort()
    mid = tmpArray[int((RGB*inH*inW)/2)]

    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] < mid:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = 255
    ########################
    displayImageColor()

def mixbrColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run bw3Color() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 이진화(중위수,평균) 알고리즘 ###
    tmpArray = []
    sum = 0;
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                tmpArray.append(inImage[rgb][i][k])
                sum += inImage[rgb][i][k];
    avg = sum / (rgb * inH * inW)

    tmpArray.sort()
    mid = tmpArray[int((RGB * inH * inW) / 2)]

    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):

                #이진화 중위수
                if k<= int(inW/2) and i < int(inH/2) :
                    if inImage[rgb][i][k] < mid:
                        outImage[rgb][i][k] = 0
                    else:
                        outImage[rgb][i][k] = 255
                elif k> int(inW/2) and i > int(inH/2):
                #이진화 평균
                    if inImage[rgb][i][k] < avg:
                        outImage[rgb][i][k] = 0
                    else:
                        outImage[rgb][i][k] = 255
                else :
                    if inImage[rgb][i][k] < 127:
                        outImage[rgb][i][k] = 0
                    else:
                        outImage[rgb][i][k] = 255
    ########################
    displayImageColor()


def pixelMenu_7() :#영상반전
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 영상반전() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                if inImage[rgb][i][k] - 255 < 0:
                    outImage[rgb][i][k] = (inImage[rgb][i][k] - 255) * (-1);
                else:
                    outImage[rgb][i][k] = (inImage[rgb][i][k] - 255);
                # outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()

def pixelMenu_8() :#포스터라이징
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 영상반전() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    inputNum = askinteger("포스터라이징", "Enter the resolution to be printed :", minvalue=1, maxvalue=30);
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                for bit in range(inputNum,1) :
                    if inImage[rgb][i][k] < int(255/bit):
                        outImage[rgb][i][k] = 0
                    else :
                        outImage[rgb][i][k] = int(255/bit)*2
                # outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()

def point2Color() : #범위강조변환
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run point2Color() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 범위강조변환 알고리즘 ###
    #p1,p2를 입력받아 범위를 조절
    p1 = askinteger("", "Value : ")
    p2 = askinteger("", "Value : ")

    if p1 > p2 : p1, p2 = p2, p1

    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                if p1 < inImage[rgb][i][k] < p2:
                    outImage[rgb][i][k] = 255
                else:
                    outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()

#============================================== [2]. 기하학 처리 ==============================================
def geometryMenu_1() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 미러링(좌우) Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 미러링(좌우) 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][inW-k-1];
    ########################
    displayImageColor()

def geometryMenu_2() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 미러링(상하) Method ...')
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 미러링(상하) 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][inH-i-1][k];
    ########################
    displayImageColor()

def moveImage() : #영상이동
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run moveImage() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 영상이동 알고리즘 ###
    dx = askinteger("", "x Value : ")
    dy = askinteger("", "y Value : ")
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                if 0 <= i + dy < outH and 0 <= k + dx < outW:
                    outImage[rgb][i + dy][k + dx] = inImage[rgb][i][k]


    ########################
    displayImageColor()

def zoomoutImage() : # 영상축소 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run zoomoutImage() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("축소", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH / scale)
    outW = int(inW / scale)

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][int(i / scale)][int(k / scale)] = inImage[rgb][i][k]
                # outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()

def zoomout2Image() : #영상축소(백워딩) 알고리즘
    # 1. 블러 알고리즘 구현
    blurrColor2()
    # 2. 축소
    zoomoutImage()

def zoominColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 영상 확대_COLOR() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("확대", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH * scale)
    outW = int(inW * scale)

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(outH, outW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(rgb,i,k,':',inImage[rgb][i][k])
                outImage[rgb][int(i*scale)][int(k*scale)] = inImage[rgb][(i)][(k)]
                # outImage[int(i*scale)][int(k*scale)] = inImage[int(i)][int(k)]

    ########################
    displayImageColor()

def zoomin2Color() : #영상 확대(백워딩)_COLOR
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 영상 확대(백워딩)_COLOR Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("축소", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH * scale)
    outW = int(inW * scale)

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(outH, outW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                # print(rgb, i, k, ':', inImage[rgb][i][k])
                outImage[rgb][(i)][(k)] = inImage[rgb][int(i / scale)][int(k / scale)]

    ########################
    displayImageColor()

def zoomin3Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('영상 확대(양선형)_COLOR')
    if filename == '' or filename == None:
        return
    scale = askinteger("확대", "배율 : ")
    tmp = inImage
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = int(scale * inH);
    outW = int(scale * inW)
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)
    print('[outH,outW]:',outH,outW)
    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                print('[i][k]',i,k,'\t int(i/scale):',int(i / scale),' int(k/scale)',int(k / scale))
                outImage[rgb][i][k] = inImage[rgb][int(i/scale)][int(k/scale)]
    # for j in range(scale):
    #     for i in range(0, outH, scale):
    #         for k in range(j, outW - 1, scale):
    #             print('j,i,k:',j,i,k,' [k-1]:',(k-1))
    #             # outImage[rgb][i][k] = int((outImage[rgb][i][k - 1] + outImage[rgb][i][k + 1]) / 2)
    #     for i in range(j, outH - 1, scale):
    #         for k in range(outW):
    #             print('j,i,k:',j,i,k,' [i-1]:',(i-1))
    #             # outImage[rgb][i][k] = int((out
    #             Image[rgb][i - 1][k] + outImage[rgb][i + 1][k]) / 2)

    ########################
    displayImageColor()

def rotateColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('영상 회전_COLOR')
    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    angle = askinteger("회전", "각도 :", minvalue=1, maxvalue=255)
    radian = angle * math.pi / 180

    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                # 공식 : xd = cos * xs - sin * ys
                # 공식 : xy = sin * xs - cos * ys
                xs = i;
                ys = k
                xd = int(math.cos(radian) * xs - math.sin(radian) * ys)
                yd = int(math.sin(radian) * xs + math.cos(radian) * ys)

                if 0 <= xd < outH and 0 <= yd < outH:
                    outImage[rgb][xd][yd] = inImage[rgb][xs][ys];
                # outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()

def rotate2Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('영상 회전(중심, 백워딩)_COLOR')
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run equalColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    # 공식 : xd = cos * xs - sin * ys
    # 공식 : xy = sin * xs - cos * ys

    angle = askinteger("회전", "각도 :", minvalue=1, maxvalue=255)
    radian = angle * math.pi / 180

    cx = inH // 2
    cy = inW // 2
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                xs = i;
                ys = k
                xd = int(math.cos(radian) * (xs - cx) - math.sin(radian) * (ys - cy) + cx)
                yd = int(math.sin(radian) * (xs - cx) + math.cos(radian) * (ys - cy) + cy)

                # print(rgb,'[',i,k,']',xd, yd,cx,cy)
                # print((math.cos(radian),' * ',(xs - cx),' - ',math.sin(radian),' * ',(ys - cy),' + ',cx,' = ',xd))

                if 0 <= xd < outH and 0 <= yd < outH:
                    outImage[rgb][xs][ys] = inImage[rgb][xd][yd];
                
            # print()

    ########################
    displayImageColor()

def rotateTestColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('영상 회전(중심, 백워딩)_COLOR')


    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    # 공식 : xd = cos * xs - sin * ys
    # 공식 : xy = sin * xs - cos * ys

    angle = askinteger("회전", "각도 :", minvalue=1, maxvalue=255)
    radian = angle * math.pi / 180

    cx = inH // 2
    cy = inW // 2
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):

                # outImage[rgb][i][k] = inImage[rgb][i][k]

                xs = i;
                ys = k
                xd = int(math.cos(radian) * (xs - cx) - math.sin(radian) * (ys - cy) + cx)
                yd = int(math.sin(radian) * (xs - cx) + math.cos(radian) * (ys - cy) + cy)

                if ys < int(inW/2):
                    if 0 <= xd < outH and 0 <= yd < int(outH):
                        outImage[rgb][xs][ys] = inImage[rgb][xd][yd];
                if ys > int(inW/2) :
                    if 0 <= xd < outH and 0 <= yd < int(outH):
                        outImage[rgb][xs][ys] = inImage[rgb][yd][xd];
    ########################
    displayImageColor()

#============================================== [3]. 화소영역 처리 ==============================================

def embossColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run embossColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 3
    mask = [
        [
            [-1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ],
        [
            [-1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ],
        [
            [-1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
    ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))
    # inImage --> 임시input
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = S
    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):

                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def blurrColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run blurrColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    mask = [
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ]
    ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))

    # inImage --> 임시input
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = S
    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):

                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def blurrColor2() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run blurrColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    mask = [
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ]
    ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))

    # inImage --> 임시input
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = S
    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):

                if tmpOutImage[rgb][i][k] > 255:
                    inImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    inImage[rgb][i][k] = 0
                else:
                    inImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def sharpColor() : #샤프닝
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run sharpColor() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 3
    mask = [
                [
                    [0.0, -1.0, 0.0],
                    [-1.0, 5.0, -1.0],
                    [0.0, -1.0, 0.0]
                ],
                [
                    [0.0, -1.0, 0.0],
                    [-1.0, 5.0, -1.0],
                    [0.0, -1.0, 0.0]
                ],
                [
                    [0.0, -1.0, 0.0],
                    [-1.0, 5.0, -1.0],
                    [0.0, -1.0, 0.0]
                ]
            ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))
    # inImage --> 임시input
    # for rgb in range(RGB) :
    #     for i in range(inH):
    #         for k in range(inW):
    #             outImage[rgb][i][k] = inImage[rgb][i][k]
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = S

    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])

    ########################
    displayImageColor()

def sharp2Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run sharpColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 3
    mask = [
        [
            [-1 / 9.0, -1 / 9.0, -1 / 9.0],
            [-1 / 9.0, 8 / 9.0, -1 / 9.0],
            [-1 / 9.0, -1 / 9.0, -1 / 9.0]
        ],
        [
            [-1 / 9.0, -1 / 9.0, -1 / 9.0],
            [-1 / 9.0, 8 / 9.0, -1 / 9.0],
            [-1 / 9.0, -1 / 9.0, -1 / 9.0]
        ],
        [
            [-1 / 9.0, -1 / 9.0, -1 / 9.0],
            [-1 / 9.0, 8 / 9.0, -1 / 9.0],
            [-1 / 9.0, -1 / 9.0, -1 / 9.0]
        ]
    ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))
    # inImage --> 임시input
    # for rgb in range(RGB) :
    #     for i in range(inH):
    #         for k in range(inW):
    #             outImage[rgb][i][k] = inImage[rgb][i][k]
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = S

    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])

    ########################
    displayImageColor()

def sharp3Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run sharpColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 3
    mask = [
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ]
    ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))
    # inImage --> 임시input
    # for rgb in range(RGB) :
    #     for i in range(inH):
    #         for k in range(inW):
    #             outImage[rgb][i][k] = inImage[rgb][i][k]
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = inImage[rgb][i - 1][k - 1] - S

    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def sharp4Color() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run sharpColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 3
    mask = [
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ],
        [
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]
        ]
    ]

    tmpInImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
    tmpOutImage = []
    for _ in range(RGB):
        tmpOutImage.append(malloc(outH, outW))
    # inImage --> 임시input
    # for rgb in range(RGB) :
    #     for i in range(inH):
    #         for k in range(inW):
    #             outImage[rgb][i][k] = inImage[rgb][i][k]
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = float(inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    α = 0.1 * askinteger("축소할 값", "Enter the resolution to be printed :", minvalue=1, maxvalue=30);
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m + i - 1][n + k - 1]
                tmpOutImage[rgb][i - 1][k - 1] = α * (inImage[rgb][i - 1][k - 1]) - S
    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def OnHomogenOperatorColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run OnHomogenOperatorColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    tmpInImage = []
    tmpOutImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
        tmpOutImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###
    #inImage >>> tmpInImage
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = (inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    # tmpInImage >>> tmpOutImage
    for rgb in range(RGB):
        for i in range(1,outH):
            for k in range(1,outW):
                #1. i행 k열과 인접한 주변 요소와의 절대값을 temp에 저장
                temp = []
                for m in range(-1, 2):
                    for n in range(-1, 2):
                        # 3x3행렬 내에서 max값을 구하는 알고리즘
                        # print('[',rgb,i,k,']',tmpInImage[rgb][i][k], '\t', '[',m + i,n + k,']',tmpInImage[rgb][m + i][n + k],'=',tmpInImage[rgb][i][k] - tmpInImage[rgb][m][n])
                        temp.append(abs(tmpInImage[rgb][i][k] - tmpInImage[rgb][m][n]))
                        # if tmpInImage[rgb][i][k] - tmpInImage[rgb][m][n] < 0:
                        #
                        #     temp.append((tmpInImage[rgb][i][k] - tmpInImage[rgb][m + i][n + k]) * (-1))
                        # else:
                        #     temp.append(tmpInImage[rgb][i][k] - tmpInImage[rgb][m + i][n + k])
                #2. 구한 절대값을 tmpOutImage배열의 시작점부터 넣어준다.
                tmpOutImage[rgb][i - 1][k - 1] = max(temp)
                # print()
    ## 임시Output --> outImage .... 오버플로 체크
    # tmpOutImage >>> outImage
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()


def differenceOperatorColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run equalColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    tmpInImage = []
    tmpOutImage = []
    newPixel = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));
        tmpInImage.append(malloc(inH + 2, inW + 2, 127))
        tmpOutImage.append(malloc(outH, outW))
        newPixel.append(malloc(inH + 2, inW + 2, 127))

    ### 진짜 영상처리 알고리즘 ###
    #InImage >>> tmpInImage
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = (inImage[rgb][i][k])
    # tmpInImage >>> newPixel

    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                newPixel[rgb][i][k]=(
                    max(
                        abs(tmpInImage[rgb][i-1][k-1]-tmpInImage[rgb][i+1][k+1]),
                        abs(tmpInImage[rgb][i-1][k+2]-tmpInImage[rgb][i+1][k-1]),
                        abs(tmpInImage[rgb][i-1][k]-tmpInImage[rgb][i+1][k]),
                        abs(tmpInImage[rgb][i][k+1]-tmpInImage[rgb][i][k-1])
                    )
                )

                # print('newPixel[',cnt,']:',newPixel[cnt])
                # print('newPixel[',rgb,i,k,']:',newPixel[rgb][i][k])

    # newPixel >>> tmpOutImage
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                tmpOutImage[rgb][i][k]=newPixel[rgb][i][k]
                # tmpOutImage[rgb][i][k]=newPixel[cnt]
                # print('[',rgb,i,k,']:',newPixel[cnt])


    # tmpOutImage >>> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def logOperatorColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run logOperatorColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 5
    mask = [
        [
            [ 0.0, 0.0,-1.0, 0.0, 0.0],
            [ 0.0,-1.0,-2.0,-1.0, 0.0],
            [-1.0,-2.0,16.0,-2.0,-1.0],
            [ 0.0,-1.0,-2.0,-1.0, 0.0],
            [ 0.0, 0.0,-1.0, 0.0, 0.0]
        ],
        [
            [ 0.0, 0.0,-1.0, 0.0, 0.0],
            [ 0.0,-1.0,-2.0,-1.0, 0.0],
            [-1.0,-2.0,16.0,-2.0,-1.0],
            [ 0.0,-1.0,-2.0,-1.0, 0.0],
            [ 0.0, 0.0,-1.0, 0.0, 0.0]
        ],
        [

            [ 0.0, 0.0,-1.0, 0.0, 0.0],
            [ 0.0,-1.0,-2.0,-1.0, 0.0],
            [-1.0,-2.0,16.0,-2.0,-1.0],
            [ 0.0,-1.0,-2.0,-1.0, 0.0],
            [ 0.0, 0.0,-1.0, 0.0, 0.0]
        ]
    ]

    tmpInImage = []
    tmpOutImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 4, inW + 4, 128))
        tmpOutImage.append(malloc(outH, outW))

    # inImage >>> tmpInImage
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = (inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m+i-2][n+k-2]
                # tmpOutImage[rgb][i - 2][k - 2] = α * (inImage[rgb][i - 2][k - 2]) - S
                tmpOutImage[rgb][i-2][k-2] = S
    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

def dogOperatorColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run logOperatorColor() Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    mSize = 5
    mask = [
                [
                    [ 0.0, 0.0,-1.0,-1.0,-1.0, 0.0, 0.0],
                    [ 0.0,-2.0,-3.0,-3.0,-3.0,-2.0, 0.0],
                    [-1.0,-3.0, 5.0, 5.0, 5.0,-3.0,-1.0],
                    [-1.0,-3.0, 5.0,16.0, 5.0,-3.0,-1.0],
                    [-1.0,-3.0, 5.0, 5.0, 5.0,-3.0,-1.0],
                    [ 0.0,-2.0,-3.0,-3.0,-3.0,-2.0, 0.0],
                    [ 0.0, 0.0,-1.0,-1.0,-1.0, 0.0, 0.0]
                ],
                [
                    [ 0.0, 0.0,-1.0,-1.0,-1.0, 0.0, 0.0],
                    [ 0.0,-2.0,-3.0,-3.0,-3.0,-2.0, 0.0],
                    [-1.0,-3.0, 5.0, 5.0, 5.0,-3.0,-1.0],
                    [-1.0,-3.0, 5.0,16.0, 5.0,-3.0,-1.0],
                    [-1.0,-3.0, 5.0, 5.0, 5.0,-3.0,-1.0],
                    [ 0.0,-2.0,-3.0,-3.0,-3.0,-2.0, 0.0],
                    [ 0.0, 0.0,-1.0,-1.0,-1.0, 0.0, 0.0]
                ],
                [
                    [ 0.0, 0.0,-1.0,-1.0,-1.0, 0.0, 0.0],
                    [ 0.0,-2.0,-3.0,-3.0,-3.0,-2.0, 0.0],
                    [-1.0,-3.0, 5.0, 5.0, 5.0,-3.0,-1.0],
                    [-1.0,-3.0, 5.0,16.0, 5.0,-3.0,-1.0],
                    [-1.0,-3.0, 5.0, 5.0, 5.0,-3.0,-1.0],
                    [ 0.0,-2.0,-3.0,-3.0,-3.0,-2.0, 0.0],
                    [ 0.0, 0.0,-1.0,-1.0,-1.0, 0.0, 0.0]
                ]
            ]

    tmpInImage = []
    tmpOutImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        tmpInImage.append(malloc(inH + 6, inW + 6, 128))
        tmpOutImage.append(malloc(outH, outW))

    # inImage >>> tmpInImage
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):

                # print(inImage[rgb][i][k],'>>>',float(inImage[rgb][i][k]))
                tmpInImage[rgb][i + 1][k + 1] = (inImage[rgb][i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for rgb in range(RGB):
        for i in range(1, inH + 1):
            for k in range(1, inW + 1):
                # 각 점을 처리
                S = 0.0
                for m in range(mSize):
                    for n in range(mSize):
                        S += mask[rgb][m][n] * tmpInImage[rgb][m+i-3][n+k-3]
                # tmpOutImage[rgb][i - 2][k - 2] = α * (inImage[rgb][i - 2][k - 2]) - S
                tmpOutImage[rgb][i - 3][k - 3] = S
    ## 임시Output --> outImage .... 오버플로 체크
    for rgb in range(RGB):
        for i in range(outH):
            for k in range(outW):
                if tmpOutImage[rgb][i][k] > 255:
                    outImage[rgb][i][k] = 255
                elif tmpOutImage[rgb][i][k] < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(tmpOutImage[rgb][i][k])
    ########################
    displayImageColor()

#============================================== [3]. 히스토그램 처리 ==============================================
def stretchColor() :    #히스토그램 스트래칭
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 히스토그램 스트래칭 Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 히스토그램 스트래칭처리 알고리즘 ###
    # 공식 : Out = (in - low)/(hight - low) * 255.0
    # low = hight = 0
    low = hight = inImage[0][0][0];
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                if low > inImage[rgb][i][k]:
                    low = inImage[rgb][i][k]
                elif hight < inImage[rgb][i][k]:
                    hight = inImage[rgb][i][k]

    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                out = (inImage[rgb][i][k] - low) / (hight - low) * 255.0
                if out > 255:
                    outImage[rgb][i][k] = 255
                elif out < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(out)  # 마지막 대입전에 정수화 시키는것이 정확한값을 출력한다.

    ########################
    displayImageColor()

#앤드 인 탐색 알고리즘
# : 이미 스트레칭된 이미지인 경우 히소토그램이 효과없을 수 있다.
#   그런경우 의도적으로 최소값 최대값 범위를 줄여 스트레칭을 하면 히스토그램 효과를 얻을 수 있다.
def endInColor():       #앤드 - 인 탐색
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 앤드 - 인 탐색 Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 히스토그램 스트래칭처리 알고리즘 ###
    # 공식 : Out = (in - low)/(hight - low) * 255.0
    # low = hight = 0
    low = hight = inImage[0][0][0];
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                if low > inImage[rgb][i][k]:
                    low = inImage[rgb][i][k]
                elif hight < inImage[rgb][i][k]:
                    hight = inImage[rgb][i][k]
    # askinteger("title","Content", minvalue=최소값, maxvalue=최대값)
    value = askinteger("스트래칭 범위 계수", "Enter Value", minvalue=0, maxvalue=255)
    low += value
    hight -= value

    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                out = (inImage[rgb][i][k] - low) / (hight - low) * 255.0
                if out > 255:
                    outImage[rgb][i][k] = 255
                elif out < 0:
                    outImage[rgb][i][k] = 0
                else:
                    outImage[rgb][i][k] = int(out)  # 마지막 대입전에 정수화 시키는것이 정확한값을 출력한다.

    ########################
    displayImageColor()

#히스토그램 평활화 - 많이 뭉쳐있는 명암 위주로 스트레칭 해주는 알고리즘
#그래프상에서 명암이 뭉쳐있으면 인접픽셀간 셀값이 비슷하여 영상을 구분하기 힘들다.
#그렇게 뭉쳐있는 픽셀값 위주로 스트레칭 해주면서 명확성을 올리는 알고리즘
def equalizedColor():   #히스토그램 평활화
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run 히스토그램 평활화 Method ...')

    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###

    # 1. 히스토그램 생성
    histo = [0 for _ in range(256)]
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                histo[inImage[rgb][i][k]] += 1
    # 2. 누적합(누적 히스토그램)
    sumHisto = [0 for _ in range(256)]
    sumHisto[0] = histo[0]
    for i in range(1, 255):
        sumHisto[i] = histo[i] + sumHisto[i - 1];
    # 3. 정규화 : n = 누적합 * (1/픽셀 수:512*512)*최대 Value(255)
    histo.sort()
    nomalHisto = [0 for _ in range(256)]
    for i in range(256):
        nomalHisto[i] = sumHisto[i] * (1 / (RGB * inH * inW)) * 255.0

    # 공식 : Out = (in - low)/(hight - low) * 255.0
    low = hight = inImage[0][0][0];
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = int(nomalHisto[inImage[rgb][i][k]]);

    ########################
    displayImageColor()

## 전역 변수부
from tkinter import Tk
window, canvas, paper = None, None, None
inImage, outImage, beforeImage, afterImage = [], [], [], []
inH, inW, outH, outW = [0] * 4
filename = '',
cvInImage, cvOutImage = None,None
RGB, R, G, B = 3,0,1,2


## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('COLOR PHOTOSHOP Ver 0.02')
    window.geometry('512x512')
    window.resizable(height=False, width=False)

    ##Loading 상태바 구현
    status = Label(window, text='이미지정보 : ',bd=1, relief=SUNKEN, anchor=W);
    status.pack(side=BOTTOM, fill=X);

    ### 메뉴 만들기 ###
    mainMenu = Menu(window)
    window.configure(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="열기(Open)", command=openFile)
    fileMenu.add_command(label="저장(Save)", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="닫기(Close)")

    editMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="편집", menu=editMenu)
    editMenu.add_command(label="실행취소", command=roolback)
    editMenu.add_command(label="다시실행", command=restart)

    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)
    pixelMenu.add_command(label="동일영상", command=equalColor)
    pixelMenu.add_command(label="1. 밝게하기", command=addColor)
    pixelMenu.add_command(label="2. 그레이스케일", command=grayColor)
    pixelMenu.add_command(label="3. 감마연산", command=gammaColor)
    pixelMenu.add_separator()
    pixelMenu.add_command(label="4. 파라볼라(캡)_COLOR", command=paraCapColor)
    pixelMenu.add_command(label="5. 파라볼라(컵)_COLOR", command=paraCupColor)
    pixelMenu.add_separator()
    pixelMenu.add_command(label="6. 이진화(기본)_COLOR", command=bw1Color)
    pixelMenu.add_command(label="7. 이진화(평균)_COLOR", command=bw2Color)
    pixelMenu.add_command(label="8. 이진화(중위수)_COLOR", command=bw3Color)
    pixelMenu.add_separator()
    pixelMenu.add_command(label="9. 영상반전", command=pixelMenu_7)
    # pixelMenu.add_command(label="포스터라이징", command=pixelMenu_8)
    pixelMenu.add_command(label="10. 범위강조 변환_COLOR", command=point2Color)
    pixelMenu.add_separator()
    # pixelMenu.add_command(label="감마연산", command=gammaImage)
    # pixelMenu.add_command(label="파라볼라(캡)_COLOR", command=paraCapImage)
    # pixelMenu.add_command(label="파라볼라(컵)_COLOR", command=paraCupImage)
    # pixelMenu.add_command(label="이진화(기본)", command=bw1Image)
    # pixelMenu.add_command(label="이진화(평균)", command=bw2Image)
    # pixelMenu.add_command(label="이진화(중위수)", command=bw3Image)
    # pixelMenu.add_command(label="감마", command=pixelMenu_9)
    # pixelMenu.add_command(label="파라볼라(캡)", command=pixelMenu_10)
    # pixelMenu.add_command(label="파라볼라(컵)", command=pixelMenu_11)
    # pixelMenu.add_command(label="범위강조 변환", command=point2Image)

    geometryMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="기하학 처리", menu=geometryMenu)
    geometryMenu.add_command(label="1. 미러링(좌우)", command=geometryMenu_1)
    geometryMenu.add_command(label="2. 미러링(상하)", command=geometryMenu_2)
    geometryMenu.add_command(label="3. 영상 이동", command=moveImage)
    geometryMenu.add_separator()
    geometryMenu.add_command(label="4. 영상 축소", command=zoomoutImage)
    geometryMenu.add_command(label="5. 영상 축소(백워딩)", command=zoomout2Image)
    geometryMenu.add_command(label="6. 영상 확대_COLOR", command=zoominColor)
    geometryMenu.add_command(label="7. 영상 확대(백워딩)", command=zoomin2Color)
    geometryMenu.add_command(label="8. 영상 확대(양선형)수정중", command=zoomin3Color)
    geometryMenu.add_separator()
    geometryMenu.add_command(label="9. 영상 회전_COLOR", command=rotateColor)
    geometryMenu.add_command(label="10. 영상 회전(중심, 백워딩)_COLOR", command=rotate2Color)

    areaMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소영역 처리", menu=areaMenu)
    areaMenu.add_command(label="1. 엠보싱_COLOR", command=embossColor)
    areaMenu.add_command(label="2. 블러링_COLOR", command=blurrColor)
    areaMenu.add_command(label="3. 샤프닝_COLOR", command=sharpColor)
    areaMenu.add_command(label="4. 고주파 필터 통과 샤프닝", command=sharp2Color)
    areaMenu.add_command(label="5. Unsharp Masking", command=sharp3Color)
    areaMenu.add_command(label="6. High-Boost", command=sharp4Color)
    areaMenu.add_command(label="7. 유사 연산자", command=OnHomogenOperatorColor)
    areaMenu.add_command(label="8. 차 연산자", command=differenceOperatorColor)
    areaMenu.add_command(label="9. LOG", command=(logOperatorColor))
    areaMenu.add_command(label="10. DOG", command=(dogOperatorColor))

    histoMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="히스토그램 처리", menu=histoMenu)
    histoMenu.add_command(label="1. 히스토그램 스트래칭", command=stretchColor)
    histoMenu.add_command(label="2. 앤드 - 인 탐색", command=endInColor)
    histoMenu.add_command(label="3. 히스토그램 평활화", command=equalizedColor)

    mixMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="응용", menu=mixMenu)
    mixMenu.add_command(label="1. 이진화(중위수,평균)_COLOR", command=mixbrColor)
    mixMenu.add_command(label="2. 영상 회전(좌우 상반 회전)_COLOR", command=rotateTestColor)
    ######################

    window.mainloop()