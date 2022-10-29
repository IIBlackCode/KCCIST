'''
** 12일차 (빅데이터 처리 시스템 개발)**
# 복습퀴즈
(1) 데이터베이스 및 테이블 설계
 - 쇼핑몰 중 한곳을 골라서 회원가입 양식을 확인하고 [회원 테이블]을 만든다.
 - 적당한 물건을 장바구니에 담은 후에, [구매] 버튼을 눌러서 확인하고 [구매 테이블]을 만든다.
 - 데이터를 회원 2명, 구매물건 각 3건씩 입력한다.


(2) 위 1번의 회원가입을 위한 TUI(Text User Interface) Python 코드를 작성한다.
(3) 위 1번의 회원가입을 위한 GUI Python 코드를 작성한다.
'''

import MemberLog
import MemberLogin
import MemberManagement
import MemberJoin
import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import ImageManagement

##==============    Function   =============
##  Login
def mainPage(conn,cur,email,name):
    print('mainPage['+email,name+']')


    ##  Member Management
    def memerManagementBTN() :
        print('회원관리 버튼 클릭 ['+email,name+']')
        window.destroy()
        MemberManagement.memberManagement(conn,cur,email,name)

    ##  Color Photoshop
    def imageBTN() :
        print('영상처리 버튼 클릭 ['+email,name+']')
        window.destroy()
        ImageManagement.mainMethod(email,name)

    ##  Select memberLog
    def memberLogBTN() :
        print('회원로그 버튼 클릭['+email,name+']')
        window.destroy()
        MemberLog.memberLog(email, name)

    ##=============  Global variable   ==========
    # conn, cur = None, None
    HOST = "127.0.0.1"
    USER ="root"
    PASSWORD ="1234"
    DB = "shopping_mall"
    ##==============    MAIN CODE   =============

    # if __name__ == '__main__' :
    window = tk.Tk()
    window.title('SHOPPING MALL PROJECT')
    window_with = 200
    window_height = 150

    monitor_width = window.winfo_screenwidth()
    monitor_height = window.winfo_screenheight()

    x = (monitor_width / 2) - (window_with / 2)
    y = (monitor_height / 2) - (window_height / 2)

    window.geometry('%dx%d+%d+%d' % (window_with, window_height, x, y))

    edtFrame = Frame(window);
    edtFrame.pack();
    listFrame = Frame(window)
    listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

    memerManagement = Button(window, text='회원관리', width=10, command=memerManagementBTN)
    memerManagement.pack(padx=10, pady=10)
    image = Button(window, text='영상처리', width=10, command=imageBTN)
    image.pack(padx=10, pady=10)
    image = Button(window, text='회원로그', width=10, command=memberLogBTN)
    image.pack(padx=10, pady=10)

    window.mainloop()
