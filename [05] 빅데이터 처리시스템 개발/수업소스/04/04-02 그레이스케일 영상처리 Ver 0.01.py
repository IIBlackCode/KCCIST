from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math

### 함수 선언부
#### 공통 함수 ####

def malloc(h, w, value=0) :
    retMemory = [ [ value for _ in range(w)]  for _ in range(h) ]
    return retMemory

def openFile() :
    global window, canvas, paper, inImage, outImage ,inH, inW, outH, outW ,filename

    ## 파일 선택하기
    filename = askopenfilename(parent=window,
        filetypes=( ('RAW 파일', '*.raw'),('All File', '*.*') ) )

    ## (중요!) 입력이미지의 높이와 폭 알아내기
    fsize = os.path.getsize(filename)
    inH = inW = int(math.sqrt(fsize))

    ## 입력이미지용 메모리 할당
    inImage = malloc(inH, inW)

    ## 파일 --> 메모리 로딩
    with open(filename,'rb') as fp :
        for i in range(inH) :
            for k in range(inW) :
                inImage[i][k] = int(ord(fp.read(1)))
    equalImage()

import struct

def saveFile() :
    global window, canvas, paper, inImage, outImage ,inH, inW, outH, outW ,filename

    if filename == '' or filename == None :
        return
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw',
                           filetypes=(('RAW 파일', '*.raw'), ('All File', '*.*')))

    for i in range(outH) :
        for k in range(outW) :
            saveFp.write(struct.pack('B', outImage[i][k]))
    saveFp.close()

def displayImage() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    window.geometry(str(outH)+'x'+str(outW))
    if canvas != None :
        canvas.destroy()
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)

    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal')

    # 볼펜으로 콕콕콕 찍기  --> 열라 느림
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put("#%02x%02x%02x" % (r, g, b), (k, i))

    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름
    rgbString =""
    for i in range(outH) :
        tmpString = "" # 각 줄
        for k in range(outW) :
            r = g = b = outImage[i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack()

##### 영상처리 함수 ######

def equalImage() :  # 동일영상 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW

    ## 출력이미지 메모리 할당
    outImage=malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
    ########################

    displayImage()

def addImage() :  # 밝게하기 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage=malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("밝게할 값", "값-->", minvalue=1, maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] + value > 255 :
                outImage[i][k] = 255
            else :
                outImage[i][k] = inImage[i][k] + value
    ########################
    displayImage()

### 전역 변수부

window, canvas, paper = None, None, None
inImage, outImage = [], []
inH, inW, outH, outW = [0] * 4
filename = ''



### 메인 코드부

if __name__ == '__main__' :
    window = Tk()
    window.title('그레이 영상처리 Ver 0.01')
    window.geometry('512x512')
    window.resizable(height=False, width=False)



    ### 메뉴 만들기 ###

    mainMenu = Menu(window)
    window.configure(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="열기(Open)", command=openFile)
    fileMenu.add_command(label="저장(Save)", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="닫기(Close)")
    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)
    pixelMenu.add_command(label="동일영상", command=equalImage)
    pixelMenu.add_command(label="밝게하기", command=addImage)

    ######################

    window.mainloop()