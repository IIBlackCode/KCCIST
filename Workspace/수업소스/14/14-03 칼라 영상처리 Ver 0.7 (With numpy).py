'''

19일 미션 (OpenCV 기능)을 [GUI기반 영상처리 소프트웨어]에 적용
메뉴를 [openCV]로 추가한 후 적용시킨다.
--> 수업에서 함께 진행함. 미리 직접 해볼 것

'''
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
import cv2
import numpy
import random
'''
퀴즈4. 시트(COLOR) 추가하고, 칼라색상으로...
'''
## 함수 선언부
def malloc(h, w, value=0) :
    retMemory = [ [ value for _ in range(w)]  for _ in range(h) ]
    return retMemory

def mallocNumpy(t,h,w) :
    retMemory = np.zeros((t,h,w), dtype=np.int16)
    return retMemory
def allocateOutMomory() :
    return mallocNumpy(RGB, outH, outW)

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
            inImage[R][i][k] = cvInImage.item(i, k ,R)
            inImage[G][i][k] = cvInImage.item(i, k, G)
            inImage[B][i][k] = cvInImage.item(i, k, B)

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
    outImage = allocateOutMomory()

    # outImage = []
    # for _ in range(RGB) :
    #     outImage.append(malloc(outH, outW))
    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB):
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]
    ########################
    displayImageColor()

## 엑셀 처리 부분
import xlrd
import xlwt
def saveExcel() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='xls',
                           filetypes=(("엑셀 파일", "*.xls"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    xlsName = saveFp.name
    #sheetName = os.path.basename(filename) # cat01_256.png
    wb = xlwt.Workbook()
    ws_R = wb.add_sheet("RED")
    ws_G = wb.add_sheet("GREEN")
    ws_B = wb.add_sheet("BLUE")
    for i in range(outH) :
        for k in range(outW) :
            ws_R.write(i,k, outImage[R][i][k])
            ws_G.write(i, k, outImage[G][i][k])
            ws_B.write(i, k, outImage[B][i][k])

    wb.save(xlsName)
    print('Excel. save ok...')


def openExcel() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList

    filename = askopenfilename(parent=window,
           filetypes=(('엑셀 파일', '*.xls'), ('All File', '*.*')))

    workbook = xlrd.open_workbook(filename)
    wsList = workbook.sheets() # 3장 워크시트
    inH = wsList[0].nrows
    inW = wsList[0].ncols
    ## 입력이미지용 메모리 할당
    inImage = []
    for _ in range(RGB):
        inImage.append(malloc(inH, inW))
    ## 파일 --> 메모리 로딩
    for i in range(inH):
        for k in range(inW):
            inImage[R][i][k] = int(wsList[R].cell_value(i, k))
            inImage[G][i][k] = int(wsList[G].cell_value(i, k))
            inImage[B][i][k] = int(wsList[B].cell_value(i, k))

    equalColor()

import xlsxwriter
def drawExcel_R() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='xls',
                           filetypes=(("엑셀 파일", "*.xls"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    xlsName = saveFp.name
    #sheetName = os.path.basename(filename) # cat01_256.png
    wb = xlsxwriter.Workbook(xlsName)
    ws_R = wb.add_worksheet("RED")
    ws_G = wb.add_worksheet("GREEN")
    ws_B = wb.add_worksheet("BLUE")

    # 셀 크기를 조절
    ws_R.set_column(0, outW-1, 1.0) # 엑셀에서 0.34
    for i in range(outH) :
        ws_R.set_row(i, 9.5) # 엑셀에서 약 0.35
    ws_G.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_G.set_row(i, 9.5)  # 엑셀에서 약 0.35
    ws_B.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_B.set_row(i, 9.5)  # 엑셀에서 약 0.35
    # 메모리 --> 엑셀 파일
    for i in range(outH) :
        for k in range(outW) :
            ## Red 시트
            data = outImage[R][i][k]
            if data <= 15 :
                hexStr = '#' + ('0' + hex(data)[2:]) + '0000'
            else :
                hexStr = '#' + hex(data)[2:] + '0000'
            # 셀 속성 변경
            cell_format = wb.add_format()
            cell_format.set_bg_color(hexStr)
            ws_R.write(i,k,'', cell_format)

    wb.close()
    print('Excel Art. save ok...')

def drawExcel_G() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='xls',
                           filetypes=(("엑셀 파일", "*.xls"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    xlsName = saveFp.name
    #sheetName = os.path.basename(filename) # cat01_256.png
    wb = xlsxwriter.Workbook(xlsName)
    ws_R = wb.add_worksheet("RED")
    ws_G = wb.add_worksheet("GREEN")
    ws_B = wb.add_worksheet("BLUE")

    # 셀 크기를 조절
    ws_R.set_column(0, outW-1, 1.0) # 엑셀에서 0.34
    for i in range(outH) :
        ws_R.set_row(i, 9.5) # 엑셀에서 약 0.35
    ws_G.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_G.set_row(i, 9.5)  # 엑셀에서 약 0.35
    ws_B.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_B.set_row(i, 9.5)  # 엑셀에서 약 0.35
    # 메모리 --> 엑셀 파일
    for i in range(outH) :
        for k in range(outW) :
            ## Green 시트
            data = outImage[G][i][k]
            if data <= 15 :
                hexStr = '#00' + ('0' + hex(data)[2:]) + '00'
                print(hexStr)
            else :
                hexStr = '#00' + hex(data)[2:] + '00'
                print(hexStr)
            # 셀 속성 변경
            cell_format = wb.add_format()
            cell_format.set_bg_color(hexStr)
            ws_G.write(i,k,'', cell_format)

    wb.close()
    print('Excel Art. save ok...')

def drawExcel_B() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='xls',
                           filetypes=(("엑셀 파일", "*.xls"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    xlsName = saveFp.name
    #sheetName = os.path.basename(filename) # cat01_256.png
    wb = xlsxwriter.Workbook(xlsName)
    ws_R = wb.add_worksheet("RED")
    ws_G = wb.add_worksheet("GREEN")
    ws_B = wb.add_worksheet("BLUE")

    # 셀 크기를 조절
    ws_R.set_column(0, outW-1, 1.0) # 엑셀에서 0.34
    for i in range(outH) :
        ws_R.set_row(i, 9.5) # 엑셀에서 약 0.35
    ws_G.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_G.set_row(i, 9.5)  # 엑셀에서 약 0.35
    ws_B.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_B.set_row(i, 9.5)  # 엑셀에서 약 0.35
    # 메모리 --> 엑셀 파일
    for i in range(outH) :
        for k in range(outW) :
            ## Red 시트
            data = outImage[B][i][k]
            if data <= 15 :
                hexStr = '#0000' + ('0' + hex(data)[2:])
            else :
                hexStr = '#0000' + hex(data)[2:]
            # 셀 속성 변경
            cell_format = wb.add_format()
            cell_format.set_bg_color(hexStr)
            ws_B.write(i,k,'', cell_format)

    wb.close()
    print('Excel Art. save ok...')

def drawExcel_RGB() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    saveFp = asksaveasfile(parent=window, mode='wb',defaultextension='xls',
                           filetypes=(("엑셀 파일", "*.xls"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    xlsName = saveFp.name
    #sheetName = os.path.basename(filename) # cat01_256.png
    wb = xlsxwriter.Workbook(xlsName)
    ws_R = wb.add_worksheet("RED")
    ws_G = wb.add_worksheet("GREEN")
    ws_B = wb.add_worksheet("BLUE")
    ws_RGB = wb.add_worksheet("COLOR")

    # 셀 크기를 조절
    ws_R.set_column(0, outW-1, 1.0) # 엑셀에서 0.34
    for i in range(outH) :
        ws_R.set_row(i, 9.5) # 엑셀에서 약 0.35
    ws_G.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_G.set_row(i, 9.5)  # 엑셀에서 약 0.35
    ws_B.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_B.set_row(i, 9.5)  # 엑셀에서 약 0.35
    ws_RGB.set_column(0, outW - 1, 1.0)  # 엑셀에서 0.34
    for i in range(outH):
        ws_RGB.set_row(i, 9.5)  # 엑셀에서 약 0.35

    # 메모리 --> 엑셀 파일
    for i in range(outH) :
        for k in range(outW) :
            for rgb in range(RGB) :
                ## Red 시트
                data = outImage[rgb][i][k]

                if rgb == R :
                    if data <= 15 :
                        hexStr = '#' + ('0' + hex(data)[2:])
                    else :
                        hexStr = '#' + hex(data)[2:]
                elif rgb == G :
                    if data <= 15 :
                        hexStr += ('0' + hex(data)[2:])
                    else :
                        hexStr += hex(data)[2:]
                elif rgb == B :
                    if data <= 15 :
                        hexStr += ('0' + hex(data)[2:])
                    else :
                        hexStr += hex(data)[2:]

                # 셀 속성 변경
                cell_format = wb.add_format()
                cell_format.set_bg_color(hexStr)
                ws_RGB.write(i,k,'', cell_format)

    wb.close()
    print('Excel Art. save ok...')

def grayScaleOpenCV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage

    ## 파일 선택하기
    fileRandomPath = image_path + random.choice(imgList)
    filename = fileRandomPath
    ## (중요!) 입력이미지의 높이와 폭 알아내기
    cvInImage = cv2.imread(filename)
    cvOutPhoto = cv2.cvtColor(cvInImage, cv2.COLOR_BGR2GRAY)
    inH = cvOutPhoto.shape[0]
    inW = (cvOutPhoto.shape[1]*2)+1
    ## 입력이미지용 메모리 할당
    inImage = []
    for _ in range(RGB):
        inImage.append(malloc(inH, inW))
    ## 파일 --> 메모리 로딩

    cvInImage = cv2.imread(filename)
    # print(cvInImage.item(0, 402, R))
    # print(cvInImage.item(1, 403, R))
    for i in range(inH):
        for k in range(inW):
            if k<=int(inW/2-1) :
                count1 =k
                # print("k<=inW :[i:",i,",k",k,"]")
                inImage[R][i][k] = cvInImage.item(i, k, R)
                inImage[G][i][k] = cvInImage.item(i, k, G)
                inImage[B][i][k] = cvInImage.item(i, k, B)

            if k>1+int(inW/2) :
                count2 =k
                # print("k>1+int(inW/2) :[i:",i,",k",k,"]")
                inImage[R][i][k] = cvOutPhoto.item(i, k-inW+1)
                inImage[G][i][k] = cvOutPhoto.item(i, k-inW+1)
                inImage[B][i][k] = cvOutPhoto.item(i, k-inW+1)

    print("inW :",inW,int(inW/2),"  count1",count1,count2)
    equalColor()


def embossingOpenCV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage

    ## 파일 선택하기
    fileRandomPath = image_path + random.choice(imgList)
    filename = fileRandomPath
    ## (중요!) 입력이미지의 높이와 폭 알아내기
    cvInImage = cv2.imread(filename)
    mask = np.zeros((3, 3), np.float32)
    mask[0][0] = -1.0;
    mask[2][2] = 1.0;
    cvOutPhoto = cv2.filter2D(cvInImage, -1, mask)

    inH = cvOutPhoto.shape[0]
    inW = cvOutPhoto.shape[1]*2 + 1
    ## 입력이미지용 메모리 할당
    inImage = []
    for _ in range(RGB):
        inImage.append(malloc(inH, inW))
    ## 파일 --> 메모리 로딩

    for i in range(inH):
        for k in range(inW):
            if k <= int(inW/2 -1):
                inImage[R][i][k] = cvInImage.item(i, k, R)
                inImage[G][i][k] = cvInImage.item(i, k, G)
                inImage[B][i][k] = cvInImage.item(i, k, B)
            if k > inW/2 :
                # print(k-int(inW/2)-1)
                inImage[R][i][k] = cvOutPhoto.item(i, k-int(inW/2)-1, R)
                inImage[G][i][k] = cvOutPhoto.item(i, k-int(inW/2)-1, G)
                inImage[B][i][k] = cvOutPhoto.item(i, k-int(inW/2)-1, B)

    equalColor()

def catoonOpenCV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage

    ## 파일 선택하기
    fileRandomPath = image_path + random.choice(imgList)
    filename = fileRandomPath
    ## (중요!) 입력이미지의 높이와 폭 알아내기
    cvInImage = cv2.imread(filename)
    cvOutPhoto = cv2.cvtColor(cvInImage, cv2.COLOR_BGR2GRAY)
    cvOutPhoto = cv2.medianBlur(cvOutPhoto, 7)
    edigs = cv2.Laplacian(cvOutPhoto, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edigs, 100, 255, cv2.THRESH_BINARY_INV)
    cvOutPhoto = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    inH = cvOutPhoto.shape[0]
    inW = cvOutPhoto.shape[1]*2 + 1
    ## 입력이미지용 메모리 할당
    inImage = []
    for _ in range(RGB):
        inImage.append(malloc(inH, inW))
    ## 파일 --> 메모리 로딩

    for i in range(inH):
        for k in range(inW):
            if k <= int(inW / 2 - 1):
                inImage[R][i][k] = cvInImage.item(i, k, R)
                inImage[G][i][k] = cvInImage.item(i, k, G)
                inImage[B][i][k] = cvInImage.item(i, k, B)
            if k > inW / 2:
                # print(k - int(inW / 2) - 1)
                inImage[R][i][k] = cvOutPhoto.item(i, k - int(inW / 2) - 1, R)
                inImage[G][i][k] = cvOutPhoto.item(i, k - int(inW / 2) - 1, G)
                inImage[B][i][k] = cvOutPhoto.item(i, k - int(inW / 2) - 1, B)

    equalColor()



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



## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('칼라 영상처리 Ver 0.3(with MySQL)')
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

    excelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Excel", menu=excelMenu)
    excelMenu.add_command(label="Excel에 저장", command=saveExcel)
    excelMenu.add_command(label="Excel에서 열기", command=openExcel)
    excelMenu.add_separator()
    excelMenu.add_command(label="Excel 아트 R", command=drawExcel_R)
    excelMenu.add_command(label="Excel 아트 G", command=drawExcel_G)
    excelMenu.add_command(label="Excel 아트 B", command=drawExcel_B)
    excelMenu.add_command(label="Excel 아트 RGB", command=drawExcel_RGB)

    opencvMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="OpenCV", menu=opencvMenu)
    opencvMenu.add_command(label="(1) GrayScale", command=grayScaleOpenCV)
    opencvMenu.add_command(label="(2) Embossing", command=embossingOpenCV)
    opencvMenu.add_command(label="(3) Catoon", command=catoonOpenCV)
    ######################

    window.mainloop()
