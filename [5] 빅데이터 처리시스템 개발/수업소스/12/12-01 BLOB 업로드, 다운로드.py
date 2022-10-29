from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import pymysql
import random
import os
import cv2

## 함수 선언부
def upFileSelect() :
    ## 파일 선택하기
    filename = askopenfilename(parent=window,
                               filetypes=(('Color 파일', '*.jpg;*.png;*.bmp;*.tif'), ('All File', '*.*')))
    edtUpFile.delete(0, 'end')
    edtUpFile.insert(0,filename)

def uploadFile() :
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
    filename = edtUpFile.get()
    tmpName = os.path.basename(os.path.basename(filename))
    p_fname, p_ext = tmpName.split('.')
    p_size = os.path.getsize(filename)
    tmpImage = cv2.imread(filename)
    p_height = tmpImage.shape[0]
    p_width = tmpImage.shape[1]
    p_upDate = '20201008' # 구글링
    p_upUser = 'root' # 로그인한 사용자

    # 파일을 읽기
    fp = open(filename, 'rb')
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

def downFileList():
    global  fileList
    conn = pymysql.connect(host=IP, user=USER, password=PASSWORD, db=DB, charset='utf8')
    cur = conn.cursor()  # 빈 트럭 준비

    sql = "SELECT p_id, p_fname, p_ext, p_size FROM photo_table"
    cur.execute(sql)

    fileList = cur.fetchall()
    for fileTup in fileList :
        listData.insert(END, fileTup[1:])


    cur.close()
    conn.close()

import tempfile
def downLoadFile() :
    global fileList
    selectIndex = listData.curselection()[0]
    print(selectIndex)
    conn = pymysql.connect(host=IP, user=USER, password=PASSWORD, db=DB, charset='utf8')
    cur = conn.cursor()  # 빈 트럭 준비

    sql = "SELECT  p_fname, p_ext, p_photo FROM photo_table WHERE p_id= "
    sql += str(fileList[selectIndex][0])
    cur.execute(sql)
    p_fname, p_ext, p_photo = cur.fetchone()

    fullPath = tempfile.gettempdir() + '/' + p_fname + '.' + p_ext
    fp = open(fullPath, 'wb')
    fp.write(p_photo)
    fp.close()

    print(fullPath)
    cur.close()
    conn.close()



## 전역 변수부
window, canvas, paper = None, None, None
inImage, outImage = [], [];  inH, inW, outH, outW = [0] * 4
cvInImage, cvOutImage = None, None
filename = ''
RGB,R, G, B= 3, 0, 1, 2
# DB 관련
conn, cur = None, None
IP = '127.0.0.1'
USER = 'root'
PASSWORD = '1234'
DB = 'photo_db'
fileList = None

## 메인 코드부
if __name__ == '__main__' :
    window  = Tk()
    window.geometry('700x500')

    ## 업로드용 프레임
    upFrame = Frame(window); upFrame.pack()
    edtUpFile = Entry(upFrame, width=50); edtUpFile.pack(side=LEFT, padx=10, pady=10)
    btnUpSelect = Button(upFrame, text='파일선택', command=upFileSelect);btnUpSelect.pack(side=LEFT, padx=10, pady=10)
    btnUpload = Button(upFrame, text='!!업로드!!', command=uploadFile); btnUpload.pack(side=LEFT, padx=10, pady=10)

    ## 다운로드용 프레임
    downFrame = Frame(window); downFrame.pack()
    btnDownList = Button(downFrame, text='목록선택', command=downFileList); btnDownList.pack(side=LEFT, padx=10, pady=10)
    listData = Listbox(downFrame, bg='yellow'); listData.pack(side=LEFT, fill=BOTH, expand=1)
    btnDownLoad = Button(downFrame, text='!!다운로드!!', command=downLoadFile); btnDownLoad.pack(side=LEFT, padx=10, pady=10)

    window.mainloop()
