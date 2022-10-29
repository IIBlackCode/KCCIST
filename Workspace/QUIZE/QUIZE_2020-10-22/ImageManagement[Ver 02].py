'''

Ver0.1 OpenCV 추가
Ver0.2 Numpy 추가
기존 구현함수 추가 및 함수명 변경(구분 가능하게), 기능정리
기능별 단위로 분리


'''
import time
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math
import cv2
import numpy
import random
import numpy as np

##  Start of Method
## =============================== Default Method ===============================
from matplotlib.pyplot import axis


def malloc(h, w, value=0) :
    retMemory = [ [ value for _ in range(w)]  for _ in range(h) ]
    return retMemory

def mallocNumpy(inputRGB, inputinH, inputinW):
    ##  np.zeros() 괄호안에 쓴 숫자크기만큼의 배열 [생성,3차원 배열 생성]
    retMemory = np.zeros((inputRGB, inputinH, inputinW), dtype=np.int16)
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

    ## 파일경로 filename 변수 저장
    filename = askopenfilename(parent=window,
           filetypes=(('Color 파일', '*.jpg;*.png;*.bmp;*.tif'), ('All File', '*.*')))

    ## 선택한 파일의 크기 저장
    cvInImage = cv2.imread(filename)
    inH = cvInImage.shape[0]
    inW = cvInImage.shape[1]

    ## 실제이미지의 크기로 inImage 생성[mallocNumpy() 함수 사용]
    # inImage = []
    # for _ in range(RGB) :
    #     inImage.append(malloc(inH, inW))
    inImage = mallocNumpy(RGB, inH, inW)

    ## 파일 --> 메모리 로딩
    start = time.time()
    for i in range(inH):
        for k in range(inW):
            inImage[R][i][k] = cvInImage.item(i, k ,B)
            inImage[G][i][k] = cvInImage.item(i, k, G)
            inImage[B][i][k] = cvInImage.item(i, k, R)

    # equalColor()
    equalColor_NP()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초 " + status.cget("text"))

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

    #[1]. Create Window
    window.geometry(str(outW)+'x'+str(outH))
    if canvas != None :
        canvas.destroy()
    #[2]. Create Canvas, Paper on Window
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

def displayImageColorNew() :
    print("displayImageColorNew()")
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if canvas != None :
        canvas.destroy()
    #윈도우 고정크기
    windowX, windowY = 512, 512 # 최대 화면 크기

    ## 이미지 크기가 512보다 클 경우 윈도우 크기 512최대 고정
    step = 1
    #이미지의 높이와 폭 둘중 하나가 512보다 클 경우
    if (outH>windowY and outW<windowX) or (outW>windowX and outH<windowY) :
        print('#이미지의 높이와 폭 둘중 하나가 512보다 클 경우 :outH:',outH,' outW:',outW)
        if outW<windowX :
            print("세로가 긴 직사각형",'Y', ':', windowX, '=', outH, ':', outW)
            print(windowY, ':X = ', outH, ':', outW)
            print(outH, "X = ", windowY, '*', outW)
            print('X = (', windowY, '*', outW, ')/', outH)
            print('X = ', int((windowY * outW) / outH))
            windowX = int((windowY * outW) / outH)

            step = outH / windowX
            print('step:',step)

        elif outH<windowY :
            print("가로가 긴 직사각형", windowY, ':','X', '=', outH, ':', outW)
            print('Y:', windowX, '=', outH, ':', outW)
            print(outW, "Y = ", windowX, '*', outH)
            print('Y = (', windowX, '*', outH, ')/', outW)
            print('Y = ', int((windowX * outH) / outW))
            windowY = int((windowY * outW) / outH)

            step = outH/windowX
            print('step:',step)

    #이미지 자체가 512 X 512 보다 큰 경우
    elif(outH>windowY and outW>windowX) :
        print('#이미지 자체가 512 X 512 보다 큰 경우 :')
        if outW > outH:
            print("가로가 긴 직사각형",windowY,':','X','=',outH,':',outW)

            print('Y:',windowX,'=', outH, ':', outW)
            print(outW, "Y = ", windowX, '*', outH)
            print('Y = (', windowX, '*', outH, ')/', outW)
            print('Y = ', int((windowX * outH) / outW))
            windowY = int((windowX * outH) / outW)

            step = outW/windowY
            print('step:',step)
        elif outW < outH:
            print("세로가 긴 직사각형",'Y',':',windowX,'=',outH,':',outW)

            print(windowY,':X = ',outH,':',outW)
            print(outH,"X = ",windowY,'*',outW)
            print('X = (',windowY,'*',outW,')/',outH)
            print('X = ',int((windowY*outW)/outH))
            windowX = int((windowY*outW)/outH)

            step = outH/windowX
            print('step:',step)

    if outW > outH:
        step = outW / windowX  # 1024/512 = 2
    elif outW < outH:
        step = outH / windowY  # 1024/512 = 2

    X = str(int(windowX*1.2))
    Y = str(int(windowY*1.2))
    #1. X,Y 크기의 윈도우창 생성
    window.geometry( X + 'x' + Y )
    canvas = Canvas(window, height=windowY, width=windowX)
    paper = PhotoImage(height=windowY, width=windowX)
    #Canvas Height width

    #x,y 위치에 이미지 생성
    x,y = windowX//2,windowY//2

    canvas.create_image(x, y, image=paper, state='normal')
    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름

    rgbString =""
    #numpy.arange(0, outW, step) : 0부터 outW까지 step반큼 건너뛴 1차원 배열
    for i in numpy.arange(0,outH,step) :
        tmpString = "" # 각 줄
        # print(i,end=' ')
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
'''
    [1].    영상 처리 함수
            1. 화소점 처리
            2. 기하학 처리
            3. 화소영역 처리
'''
## =============================== 영상 처리 함수 ===============================
'''
            1. 화소점 처리
                (1). 동일영상
                (2). 밝게하기
                (3). 그레이스케일
                (4). 감마연산
                (5). 파라볼라(캡)
                (6). 파라볼라(컵)
                (7). 이진화(기본)
                (8). 이진화(평균)
                (9). 이진화(중위수)
                (10). 범위강조 변환
'''
##  (1) 동일영상 [구버젼]
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
def reverseColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW
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
    second = end-start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text") )

## =============================== NUMPY ===============================
'''
    기존 영상처리 함수에 NUMPY를 사용하여 성능이 향상된 버젼
'''

##  (1) 동일영상
def equalColor_NP() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    print("성능 개선")
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = inImage.copy()
    ########################
    displayImageColorNew()

## (2) 밝게하기
def addColor_NP() :
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
    displayImageColorNew()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text"))

def reverseColor_NP() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW
    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    # value = askinteger("밝게하기", "값")
    # if value == None :
    #     return
    outImage = 255 - inImage
    ########################
    displayImageColorNew()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text") )

## (5) 그레이스케일
def grayColor_NP() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    global beforeImage, afterImage
    if filename == '' or filename == None:
        return
    start = time.time()
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW

    ## 출력이미지 메모리 할당
    outImage = mallocNumpy(RGB, outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            c = inImage[R][i][k] + inImage[G][i][k] + inImage[B][i][k]
            c = int(c/3)
            outImage[R][i][k] = outImage[G][i][k] = outImage[B][i][k] = c

    # 영상처리 후 바뀐 이미지 저장
    ########################
    displayImageColorNew()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text"))

## =============================== MySQL 관련 함수 ===============================
### MySQL 관련 함수 ###
import tempfile
import os
import pymysql
import random
def upMySQL() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == None or filename == '':
        return

    saveCvPhoto = np.zeros((outH, outW, 3), np.uint8)
    for i in range(outH):
        for k in range(outW):
            tup = tuple(([outImage[B][i][k], outImage[G][i][k], outImage[R][i][k]]))
            saveCvPhoto[i, k] = tup

    saveFname = tempfile.gettempdir() + '/' + os.path.basename(filename)
    cv2.imwrite(saveFname, saveCvPhoto)
    ##############
    '''
    DROP DATABASE IF exists photo_db;
    CREATE DATABASE photo_db;
    USE photo_db;
    CREATE TABLE photo_table (
      p_id INT PRIMARY KEY,
      p_fname VARCHAR(255),
      p_ext   CHAR(5),
      p_size  BIGINT,
      p_height INT,
      p_width  INT,
      p_photo LONGBLOB,
      p_upDate DATE,
      p_upUser CHAR(10) -- Foreign Key
    )
    '''
    conn = pymysql.connect(host=IP, user=USER, password=PASSWORD, db=DB, charset='utf8')
    cur = conn.cursor()  # 빈 트럭 준비
    p_id = random.randint(-2100000000, 2100000000)
    tmpName = os.path.basename(os.path.basename(saveFname))
    p_fname, p_ext = tmpName.split('.')
    p_size = os.path.getsize(saveFname)
    tmpImage = cv2.imread(saveFname)
    p_height = tmpImage.shape[0]
    p_width = tmpImage.shape[1]
    p_upDate = '20201008' # 구글링
    p_upUser = 'root' # 로그인한 사용자

    # 파일을 읽기
    fp = open(saveFname, 'rb')
    blobData = fp.read()
    fp.close()

    # 파일 정보 입력
    sql = "INSERT INTO photo_table(p_id, p_fname, p_ext, p_size, p_height, p_width, "
    sql += "p_upDate, p_UpUser, p_photo) VALUES (" + str(p_id) + ", '" + p_fname + "', '" + p_ext
    sql += "', " + str(p_size) + "," + str(p_height) + "," + str(p_width) + ", '" + p_upDate
    sql += "', '" + p_upUser +  "', %s )"
    tupleData = (blobData,)
    cur.execute(sql,tupleData)

    conn.commit()
    cur.close()
    conn.close()
    messagebox.showinfo('성공', filename + ' 잘 입력됨.')

    #############


def downMySQL() : # 파일 열기 개념....
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    ###################
    conn = pymysql.connect(host=IP, user=USER, password=PASSWORD, db=DB, charset='utf8')
    cur = conn.cursor()  # 빈 트럭 준비
    sql = "SELECT p_id, p_fname, p_ext, p_size FROM photo_table"
    cur.execute(sql)
    fileList = cur.fetchall()
    cur.close()
    conn.close()
    ##################
     # 서브 윈도창 나오기.
    def downLoad() :
        global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
        global cvInImage, cvOutImage, fileList
        selectIndex = listData.curselection()[0]
        conn = pymysql.connect(host=IP, user=USER, password=PASSWORD, db=DB, charset='utf8')
        cur = conn.cursor()  # 빈 트럭 준비
        sql = "SELECT  p_fname, p_ext, p_photo FROM photo_table WHERE p_id= "
        sql += str(fileList[selectIndex][0])
        cur.execute(sql)
        p_fname, p_ext, p_photo = cur.fetchone()

        fullPath = tempfile.gettempdir() + '/' + p_fname + '.' + p_ext
        fp = open(fullPath, 'wb')
        fp.write(p_photo)
        print(fullPath)
        fp.close()
        cur.close()
        conn.close()

        filename = fullPath
        subWindow.destroy()
        ####
        cvInImage = cv2.imread(filename)
        inH = cvInImage.shape[0]
        inW = cvInImage.shape[1]
        ## 입력이미지용 메모리 할당
        inImage = []
        for _ in range(RGB):
            inImage.append(malloc(inH, inW))
        ## 파일 --> 메모리 로딩

        for i in range(inH):
            for k in range(inW):
                inImage[R][i][k] = cvInImage.item(i, k, B)
                inImage[G][i][k] = cvInImage.item(i, k, G)
                inImage[B][i][k] = cvInImage.item(i, k, R)

        equalColor()
        ####

    subWindow = Toplevel(window)
    subWindow.geometry('300x400')

    ## 스크롤바 나타내기
    frame = Frame(subWindow)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side='right', fill = 'y')
    listData = Listbox(frame, yscrollcommand=scrollbar.set); listData.pack()
    scrollbar['command']=listData.yview
    frame.pack()

    for fileTup in fileList:
        listData.insert(END, fileTup[1:])
    btnDownLoad = Button(subWindow, text='!!다운로드!!', command=downLoad)
    btnDownLoad.pack(padx=10, pady=10)
## =============================== 엑셀 처리 함수 ===============================
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
## =============================== Haarcascade (머신러닝) ===============================
### Haarcascade 관련 함수 ###
import cv2
#   얼굴인식
def faceDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
    print("성능 개선")
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = inImage.copy()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    grey = cv2.cvtColor(cvInImage, cv2.COLOR_BGR2GRAY)
    face_rects = face_cascade.detectMultiScale(grey, 1.1, 5)

    for x, y, w, h, in face_rects:
        cv2.rectangle(cvInImage, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow('', cvInImage)
    c = cv2.waitKey()
    cv2.destroyWindow()
    ########################
    displayImageColorNew()
#   코 인식
def haarcascade_mcs_nose() :
    pass
#   귀 인식
def haarcascade_mcs_leftear() :
    pass
#   고양이 얼굴 인식
def catFaceDetect_CV() :
    pass
## =============================== DeepLearning (딥러닝) ===============================
### DeepLearning 관련 함수 ###
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
def ssdNet(image) :
    global count
    CONF_VALUE = 0.8 # 20% 인정
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]
    COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
    net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt", "MobileNetSSD_deploy.caffemodel")
    (h, w) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    count = 0
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > CONF_VALUE:
            count +=1
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            print('count',count,label)
            cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    return image


def deepStopImage_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    cvOutImage = ssdNet(cvInImage)

    cvOut2outImage()
    ########################
    displayImageColor()

#영상
def deepMoveImage_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList

    movieName =  askopenfilename(parent=window,
           filetypes=(('동영상 파일', '*.mp4;*.avi'), ('All File', '*.*')))
    s_factor = 0.5 # 화면 크기 비율(조절 가능)

    # cv2.VideoCapture("동영상 경로") : 프레임 단위로 저장
    capture = cv2.VideoCapture(movieName)


    frameCount = 0 # 처리할 프레임의 숫자 (자동증가)
    ##### OpenCV 용 영상처리 ###
    while True:
        ret, frame = capture.read()
        if not ret:  # 동영상을 읽기 실패
            break
        frameCount += 1
        if frameCount % 30 == 0 : # 숫자 조절 가능 (속도 문제)
            frame = cv2.resize(frame, None, fx=s_factor, fy=s_factor, interpolation=cv2.INTER_AREA)
            ## 1장짜리 SSD 딥러닝 ##
            retImage = ssdNet(frame)
            ####################
            cv2.imshow('Video', retImage)

        # 입력한숫자ms마다 프레임을 재생합니다.
        key = cv2.waitKey(1) # 화면 속도 조절

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
    #cv2.destroyAllWindows()
    ########################
    #displayImageColor()

#영상
def deepMoveImage_CV2() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    global temp

    movieName =  askopenfilename(parent=window,
           filetypes=(('동영상 파일', '*.mp4;*.avi'), ('All File', '*.*')))
    s_factor = 0.5 # 화면 크기 비율(조절 가능)

    # cv2.VideoCapture("동영상 경로") : 프레임 단위로 저장
    capture = cv2.VideoCapture(movieName)


    frameCount = 0 # 처리할 프레임의 숫자 (자동증가)
    ##### OpenCV 용 영상처리 ###
    while True:
        frameCount += 1
        # print('frameCount:',frameCount)
        #영상 프레임 = 이미지

        ## 1장짜리 SSD 딥러닝 ##

        frameCount += 1
        if frameCount % 10 == 0:  # 숫자 조절 가능 (속도 문제)
            #   영상 프래임 원본 저장
            ret, frame = capture.read()
            frame = cv2.resize(frame, None, fx=s_factor, fy=s_factor, interpolation=cv2.INTER_AREA)
            retImage = ssdNet(frame)
            if not ret:  # 동영상을 읽기 실패
                break

            # 이미지 처리작업
            cvInImage = retImage

            # cvOutImage = cv2.cvtColor(cvInImage, cv2.COLOR_RGB2GRAY)
            # cvOutImage = cv2.medianBlur(cvOutImage, 7)
            # edges = cv2.Laplacian(cvOutImage, cv2.CV_8U, ksize=5)
            # ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)
            # cvOutImage = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

            #그레이스케일 효과
            cvOutImage = cv2.cvtColor(cvInImage, cv2.COLOR_BGR2GRAY)
            cvOut2outImage()

            #   원본영상 출력
            cv2.imshow('VideoOriginal', retImage)

            #   이미지 처리영상 출력
            retImage2 = cvOutImage
            cv2.imshow('Video', retImage2)


        # 입력한숫자ms마다 프레임을 재생합니다.
        key = cv2.waitKey(60) # 화면 속도 조절

        if key == 27:  # esc 키
            break
        elif key == ord('c') or key == ord('C'):
            # 키보드가 아닌, 조건에 의해서 처리도 가능함...
            # 예로 사람이 3명이상 등장하면......  강아지가 나타나면...
            cvInImage = cvOutImage = retImage
            filename = movieName
            cvOut2outImage()
            displayImageColor()
        # elif count >=3 :
        #     cvInImage = cvOutImage = retImage
        #     filename = movieName
        #     cvOut2outImage()
        #     displayImageColor()
        #     print('count : ', count)

        if (count > temp) and (temp != None) :
            temp = count
            print('temp:',temp,' count:',count)
            cvInImage = cvOutImage = retImage
            filename = movieName
            cvOut2outImage()
            displayImageColor()


    capture.release()
    #cv2.destroyAllWindows()
    ########################
    #displayImageColor()

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
count = 0
temp = 0

## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('칼라 영상처리 Ver 0.7(2020-10-20)')
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

    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리[NUMPY]", menu=pixelMenu)
    pixelMenu.add_command(label="동일영상", command=equalColor_NP)
    pixelMenu.add_command(label="밝게하기", command=addColor_NP)
    pixelMenu.add_command(label="리버스", command=reverseColor_NP)
    pixelMenu.add_command(label="그레이스케일", command=grayColor_NP)
    # pixelMenu.add_command(label="감마연산", command=gammaColor)
    # pixelMenu.add_command(label="파라볼라(캡)_COLOR", command=paraCapColor)
    # pixelMenu.add_command(label="파라볼라(컵)_COLOR", command=paraCupColor)
    # pixelMenu.add_command(label="이진화(기본)_COLOR", command=bw1Color)
    # pixelMenu.add_command(label="이진화(평균)_COLOR", command=bw2Color)
    # pixelMenu.add_command(label="이진화(중위수)_COLOR", command=bw3Color)
    # pixelMenu.add_command(label="범위강조 변환_COLOR", command=point2Color)

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

    haarcascadeMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="haarcascade", menu=haarcascadeMenu)
    haarcascadeMenu.add_command(label="(1) 얼굴인식", command=faceDetect_CV)
    haarcascadeMenu.add_command(label="(2) 하르케스케이드(고영희씨)", command=catFaceDetect_CV)

    deepCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="딥러닝", menu=deepCVMenu)
    deepCVMenu.add_command(label="사물 인식(정지영상)", command=deepStopImage_CV)
    deepCVMenu.add_command(label="사물 인식(동영상)", command=deepMoveImage_CV)
    deepCVMenu.add_command(label="사물 인식(연습)", command=deepMoveImage_CV2)

    ######################

    window.mainloop()
