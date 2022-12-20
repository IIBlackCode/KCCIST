#퀴즈1. 엔드-인 탐색 구현

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
#cd2 외부 라이브러리 설치 필요
#cmd > pip install opencv-python
import cv2
import numpy

## 함수선언부
def malloc(h, w, value=0) :
    global count
    count +=1;
    print('Run malloc() Method ...',h,w,value,count)

    if count >= 3 :
        count = 0;

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
    print(cvInImage.shape)
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
############### 영상처리 함수 ###############
def equalColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run equalColor() Method ...')

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

#퀴즈2. 칼라 --> GrayScale
def GrayScale() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run equalColor() Method ...')
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
                outImage[rgb][i][k] = int((inImage[0][i][k]+inImage[0][i][k]+inImage[0][i][k])/3)

    ########################
    displayImageColor()



## 전역 변수부
from tkinter import Tk
window, canvas, paper = None, None, None
inImage, outImage = [], []
inH, inW, outH, outW = [0] * 4
filename = '',
cvInImage, cvOutImage = None,None
RGB, R, G, B = 3,0,1,2
count = 0
## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('복습퀴즈 2020-09-24')
    window.geometry('512x512')
    window.resizable(height=False, width=False)

    ##Loading 상태바 구현
    status = Label(window, text='이미지정보 : ',bd=1, relief=SUNKEN, anchor=W);
    status.pack(side=BOTTOM, fill=X);

    ### 메뉴 만들기 ###

    #   메인메뉴 생성
    mainMenu = Menu(window)
    window.configure(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="열기(Open)", command=openFile)
    # fileMenu.add_command(label="저장(Save)", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="닫기(Close)")

    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)

    pixelMenu.add_command(label="GrayScale", command=GrayScale)
    # pixelMenu.add_command(label="밝게하기", command=addImage)
    # pixelMenu.add_command(label="감마연산", command=gammaImage)
    # pixelMenu.add_command(label="파라볼라(캡)", command=paraCapImage)
    # pixelMenu.add_command(label="파라볼라(캡)", command=paraCupImage)
    # pixelMenu.add_command(label="이진화(기본)", command=bw1Image)
    # pixelMenu.add_command(label="이진화(평균)", command=bw2Image)
    # pixelMenu.add_command(label="이진화(중위수)", command=bw3Image)
    # pixelMenu.add_command(label="범위강조 변환", command=point2Image)

    ######################

    window.mainloop()