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
import time
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
    displayImageColor()
    end = time.time()
    second = end - start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text") )

def addColor() :
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
    second = end-start
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text") )

def addColor_NP() :
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
    value = askinteger("밝게하기", "값")
    if value == None :
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
    status.configure(text="{0:.2f}".format(second) + "초  " + status.cget("text") )


def grayColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    if filename == '' or filename == None:
        return
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
    ########################
    displayImageColor()


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
def drawExcel() :
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

def earLeftDetect_CV() :
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
def earRightDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    face_cascade = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml')
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)
    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.1, 5)
    for x, y, w, h in fact_rects:
        cv2.rectangle(cvOutImage, (x, y), (x + h, y + w), (0, 255, 0), 3)

    cvOut2outImage()
    ########################
    displayImageColor()
def mouseDetect_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    if filename == None:
        return
    ##### OpenCV 용 영상처리 ###
    face_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
    grey = cv2.cvtColor(cvInImage[:], cv2.COLOR_BGR2GRAY)
    # 얼굴 찾기
    cvOutImage = cvInImage[:]
    fact_rects = face_cascade.detectMultiScale(grey, 1.1, 5)
    for x, y, w, h in fact_rects:
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
            # print('count',count,label)
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
        ret, frame = capture.read()
        if not ret:  # 동영상을 읽기 실패
            break
        frameCount += 1
        # print('frameCount:',frameCount)
        #영상 프레임 = 이미지
        frame = cv2.resize(frame, None, fx=s_factor, fy=s_factor, interpolation=cv2.INTER_AREA)

        ## 1장짜리 SSD 딥러닝 ##

        frameCount += 1
        if frameCount % 10 == 0:  # 숫자 조절 가능 (속도 문제)
            #   영상 프래임 원본 저장
            retImage = ssdNet(frame)

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
    ########################
import cv2 as cv
def lineDetected_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    global temp

    movieName =  askopenfilename(parent=window,
           filetypes=(('동영상 파일', '*.mp4;*.avi'), ('All File', '*.*')))
    s_factor = 0.5 # 화면 크기 비율(조절 가능)

    # cv2.VideoCapture("동영상 경로") : 프레임 단위로 저장
    video = cv2.VideoCapture(movieName)

    while (True):

        #   영상 읽기
        ret, videoSrc = video.read()

        #   영상 크기 설정
        image = cv2.resize(videoSrc, (640, 360))
        test = ssdNet(image)
        #   cv::Canny( src [입력 영상], dst [결과 영상이 저장될 Mat 형식], 30 [ 낮은 경곗값 1],
        #       127 [ 높은 경곗값 2], 3 [Sobel 커널 크기], false [정교하게 작동 여부] );
        dst = cv.Canny(test, 50, 200, None, 3)

        cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
        cdstP = np.copy(test)



        '''
        cv2.HoughLines(image, rho, theta, threshold[, lines[, srn[, stn[, min_theta[, max_theta]]]]]) → lines
        Parameters:	
        image – 8bit, single-channel binary image, canny edge를 선 적용.
        rho – r 값의 범위 (0 ~ 1 실수)
        theta – 𝜃 값의 범위(0 ~ 180 정수)
        threshold – 만나는 점의 기준, 숫자가 작으면 많은 선이 검출되지만 정확도가 떨어지고, 숫자가 크면 정확도가 올라감.
        '''

        #차선 그리기
        lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
        if lines is not None:
            for i in range(0, len(lines)):
                rho = lines[i][0][0]
                theta = lines[i][0][1]
                a = math.cos(theta)
                b = math.sin(theta)
                x0 = a * rho
                y0 = b * rho
                pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
                pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
                cv.line(cdst, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

        # 차선 그리기
        linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), 3, cv.LINE_AA)

        cv.imshow("Original video", image)
        #   표준 허프 라인 변환
        cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
        #   Probabilistic Line Transform
        cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
        cv.imshow("Detected Lines (in red) - test", test)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    ########################

def region_of_interest(img, vertices, color3=(255, 255, 255), color1=255):  # ROI 셋팅

    mask = np.zeros_like(img)  # mask = img와 같은 크기의 빈 이미지

    if len(img.shape) > 2:  # Color 이미지(3채널)라면 :
        color = color3
    else:  # 흑백 이미지(1채널)라면 :
        color = color1

    # vertices에 정한 점들로 이뤄진 다각형부분(ROI 설정부분)을 color로 채움
    cv2.fillPoly(mask, vertices, color)

    # 이미지와 color로 채워진 ROI를 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image


def mark_img(image):  # 흰색 차선 찾기
    blue_threshold = 200; green_threshold = 200; red_threshold = 200
    #  BGR 제한 값
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (image[:, :, 0] < bgr_threshold[0]) \
                 | (image[:, :, 1] < bgr_threshold[1]) \
                 | (image[:, :, 2] < bgr_threshold[2])
    mark = np.copy(image)
    mark[thresholds] = [0, 0, 0]
    return image

def lineDetected2_CV() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage, fileList
    global temp

    movieName = askopenfilename(
        parent=window,
        filetypes=(('동영상 파일', '*.mp4;*.avi'), ('All File', '*.*'))
    )
    s_factor = 0.5  # 화면 크기 비율(조절 가능)

    # cv2.VideoCapture("동영상 경로") : 프레임 단위로 저장
    video = cv2.VideoCapture(movieName)

    while (True):

        #   영상 읽기
        ret, videoSrc = video.read()

        #   영상 크기 설정
        image = cv2.resize(videoSrc, (640, 360))
        height, width = image.shape[:2]
        # test = ssdNet(image)
        #   cv::Canny( src [입력 영상], dst [결과 영상이 저장될 Mat 형식], 30 [ 낮은 경곗값 1],
        #       127 [ 높은 경곗값 2], 3 [Sobel 커널 크기], false [정교하게 작동 여부] );
        dst = cv.Canny(image, 50, 200, None, 3)

        # 사다리꼴 모형의 Points
        vertices = np.array(
            [
                [
                    (80, height),
                    (width / 2 - 60, height / 2 + 30),
                    (width / 2 + 60, height / 2 + 30),
                    (width - 80, height)
                ]
            ],
            dtype=np.int32)

        # vertices에 정한 점들 기준으로 ROI 이미지 생성
        roi_img = region_of_interest(image, vertices, (0, 0, 255))
        mark = np.copy(roi_img)  # roi_img 복사
        mark = mark_img(roi_img)  # 흰색 차선 찾기

        # 흰색 차선 검출한 부분을 원본 image에 overlap 하기
        color_thresholds = (mark[:, :, 0] == 0) & (mark[:, :, 1] == 0) & (mark[:, :, 2] > 200)
        image[color_thresholds] = [0, 255, 0]

        cv2.imshow('roi_white', mark)  # 흰색 차선 추출 결과 출력
        cv2.imshow('result', image)  # 이미지 출력

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

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
count = 0
temp = 0

## 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('칼라 영상처리 Ver 0.8(include 하르케스케이드)')
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
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)
    pixelMenu.add_command(label="동일영상", command=equalColor)
    pixelMenu.add_command(label="반전영상", command=reverseColor)
    pixelMenu.add_command(label="반전영상(NumPy)", command=reverseColor_NP)
    pixelMenu.add_command(label="밝게하기", command=addColor)
    pixelMenu.add_command(label="밝게하기(NumPy)", command=addColor_NP)
    pixelMenu.add_command(label="그레이스케일", command=grayColor)

    MySQLMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="MySQL", menu=MySQLMenu)
    MySQLMenu.add_command(label="MySQL에 저장", command=upMySQL)
    MySQLMenu.add_command(label="MySQL에서 열기", command=downMySQL)

    excelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="Excel", menu=excelMenu)
    excelMenu.add_command(label="Excel에 저장", command=saveExcel)
    excelMenu.add_command(label="Excel에서 열기", command=openExcel)
    excelMenu.add_separator()
    excelMenu.add_command(label="Excel 아트", command=drawExcel)

    openCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="OpenCV", menu=openCVMenu)
    openCVMenu.add_command(label="그레이 스케일", command=grayscale_CV)
    openCVMenu.add_command(label="카툰 이미지", command=cartoon_CV)

    harrCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="머신러닝", menu=harrCVMenu)
    harrCVMenu.add_command(label="하르케스케이드(얼굴)", command=faceDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(귀-왼쪽)", command=earLeftDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(귀-오른쪽)", command=earRightDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(입)", command=mouseDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(코)", command=noseDetect_CV)
    harrCVMenu.add_command(label="하르케스케이드(고영희씨)", command=catFaceDetect_CV)

    deepCVMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="딥러닝", menu=deepCVMenu)
    deepCVMenu.add_command(label="사물 인식(정지영상)", command=deepStopImage_CV)
    deepCVMenu.add_command(label="사물 인식(동영상)", command=deepMoveImage_CV)
    deepCVMenu.add_command(label="사물 인식(연습)", command=deepMoveImage_CV2)
    deepCVMenu.add_command(label="차선, 차 인식(연습)", command=lineDetected_CV)
    deepCVMenu.add_command(label="차선, 차 인식(연습)", command=lineDetected2_CV)

    ######################

    window.mainloop()
