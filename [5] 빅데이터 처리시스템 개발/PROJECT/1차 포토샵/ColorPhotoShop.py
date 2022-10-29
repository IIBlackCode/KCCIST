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

    inImage = []

    for _ in range(RGB) :

        inImage.append(malloc(inH, inW))

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

    window.geometry(str(outW)+'x'+str(outH))

    if canvas != None :

        canvas.destroy()

    canvas = Canvas(window, height=outH, width=outW)

    paper = PhotoImage(height=outH, width=outW)

    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름

    rgbString =""

    for i in range(outH) :

        tmpString = "" # 각 줄

        for k in range(outW) :

            r = outImage[R][i][k]

            g = outImage[G][i][k]

            b = outImage[B][i][k]

            tmpString += "#%02x%02x%02x " % (r, g, b)

        rgbString += '{' + tmpString + '} '

    paper.put(rgbString)

    canvas.pack()

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

    outImage = []

    for _ in range(RGB) :

        outImage.append(malloc(outH, outW))

    ### 진짜 영상처리 알고리즘 ###

    for rgb in range(RGB):

        for i in range(inH):

            for k in range(inW):

                outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################

    displayImageColor()

def addColor() :

    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename

    global cvInImage, cvOutImage

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

    displayImageColor()

def grayColor() :

    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename

    global cvInImage, cvOutImage

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

    displayImageColor()

## 전역 변수부
window, canvas, paper = None, None, None
inImage, outImage = [], [];  inH, inW, outH, outW = [0] * 4
cvInImage, cvOutImage = None, None
filename = ''
RGB,R, G, B= 3, 0, 1, 2

## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('칼라 영상처리 Ver 0.1')
    window.geometry('512x512')
    window.resizable(height=False, width=False)
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


    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)

    pixelMenu.add_command(label="동일영상", command=equalColor)
    pixelMenu.add_command(label="밝게하기", command=addColor)
    pixelMenu.add_command(label="그레이스케일", command=grayColor)


    ######################

    window.mainloop()