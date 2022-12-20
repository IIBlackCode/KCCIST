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

import MemberLogin
import MemberManagement
import MemberJoin

import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk
##==============    Function   =============
##  Login
def memberLogin(conn,cur) :
    print('memberLogin 로그인 화면')
    def loginBTN():

        global email,password
        sql = "SELECT * FROM member WHERE m_email LIKE '"+inputEmail.get()+"'"
        print(sql)
        cur.execute(sql)
        temp =''
        while (True) :
            row = cur.fetchone()
            if row == None :
                break;
            email     = row[0]
            password  = row[1]
            name      = row[2]
            # print('입력ID:',inputEmail.get(), ' 입력PW',inputPassword.get() , email, password)

            if inputEmail.get() == email and inputPassword.get() == password :
                print('Success')
                goTomemberManagement(conn,cur,email,name)
                window.destroy()

                break
            elif inputEmail.get() == email and inputPassword.get() != password :
                # print('Error')
                temp = 'Password Error'
                break
            else :
                # print('Error')
                temp = TRUE

        if temp == 'Password Error' :
            messagebox.showerror('Error','비밀번호가 맞지 않습니다.')
            print('Error')
        if temp == TRUE :
            messagebox.showerror('Error','없는 아이디 입니다.')
            print('Error')

    ##  Member Management
    def goTomemberManagement(conn,cur,email,name) :
        print('회원관리 페이지 이동[',email,name,']')
        window.destroy()
        MemberManagement.memberManagement(conn,cur,email,name)

    ##=============  Global variable   ==========
    # conn, cur = None, None
    # HOST = "127.0.0.1"
    # USER ="root"
    # PASSWORD ="1234"
    # DB = "shopping_mall"

    email,password = '',''
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
    #   Input Email
    inputEmail = Entry(edtFrame, width = 10);  inputEmail.pack(padx=10, pady=10)
    #   Input Password
    inputPassword = Entry(edtFrame, width = 10);  inputPassword.pack(padx=10, pady=10)

    #Login Button
    edt = Entry(window, width = 10)
    loginbtn = Button(window, text='로그인', width=10, command=loginBTN)
    loginbtn.pack(padx=10, pady=10)

