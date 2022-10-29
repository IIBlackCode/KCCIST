'''
** 12일차 (빅데이터 처리 시스템 개발)**
# 복습퀴즈
## 미니 프로젝트 Vol 1.5 ##
- 기존 PPT에 [MySQL] 메뉴의 기능을 추가하기.
- 표지에 [Vol 1.5] 표시하기
- 제목을 포토샵, 그림판 등을 지양하기
- 제출은 10/11일(일) 20시까지 메일로 (dangtang@paran.com)

  [자바 빅데이터] 미니프로젝트 (Vol 1.5) , 홍길동
  - 보고서 PPT, 1page 요약, 동영상 파일(너무 크면 생략), 소스파일 및 사용데이터를 한번에 압축
   ** PPT 파일명 : 미니프로젝트1.5(홍길동).pptx
   ** 1page 요약 파일명 : 미니프로젝트1.5(홍길동)_요약본.pptx 또는 hwp 또는 docx
   ** 프로그램 이름 및 사용 데이터 : 관계없음
   ** 최종 압축파일명 :  미니프로젝트1.5(홍길동).zip

[영상처리 소프트웨어]를 데이터베이스 환경으로 구현하기.
권장기능

(1) 회원 관련
 - 로그인 기능
 - 관리자의 회원 관리 기능 : 회원입력/회원수정/회원삭제/회원조회
 - 회원 가입 기능

(2) 영상처리 관련
 - 데이터베이스에서 파일을 불러오기 및 저장 기능
 - 이미지 파일을 선택해서 데이터베이스에 업로드 기능
 - 폴더를 선택해서, 폴더의 모든 이미지를 한꺼번에 데이터베이스에 업로드 기능
 - 회원별 영상처리 작업 기록을 데이터베이스에 남겨 놓기 (작업기록테이블 필요)
'''

import MemberLogin
import MemberJoin
import tkinter as tk
import pymysql
from tkinter import *



##==============    Function   =============
##  Login

def memberLoginBTN():
    # global cur
    window.destroy()
    MemberLogin.memberLogin(conn,cur)

##  Member Management
# def memerManagementBTN() :
#     global cur
#     window.destroy()
#     MemberManagement.memberManagement()

##  Member Join
def memerJoinBTN() :
    # global cur
    MemberJoin.memberManagement(conn,cur)

##=============  Global variable   ==========
# conn, cur = None, None
HOST = "127.0.0.1"
USER ="root"
PASSWORD ="1234"
DB = "shopping_mall"
conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,db=DB, charset="utf8")
cur = conn.cursor()
email,password = '',''
##==============    MAIN CODE   =============

# if __name__ == '__main__' :
window = tk.Tk()
window.title('SHOPPING MALL PROJECT')
window_with     = 200
window_height   = 100
monitor_width = window.winfo_screenwidth()
monitor_height= window.winfo_screenheight()
x = (monitor_width/2) - (window_with/2)
y = (monitor_height/2) - (window_height/2)
window.geometry('%dx%d+%d+%d' %(window_with,window_height,x,y))

edtFrame = Frame(window);
edtFrame.pack();
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)
# #   Input Email
# inputEmail = Entry(edtFrame, width = 10);  inputEmail.pack(padx=10, pady=10)
# #   Input Password
# inputPassword = Entry(edtFrame, width = 10);  inputPassword.pack(padx=10, pady=10)

#Login Button
edt = Entry(window, width = 10)
loginbtn = Button(window, text='로그인', width=10, command=memberLoginBTN)
loginbtn.pack(padx=10, pady=10)
memerManagement = Button(window, text='회원가입', width=10, command=memerJoinBTN)
memerManagement.pack(padx=10, pady=10)

window.mainloop()
def backMain() :
    window = tk.Tk()
    window.title('SHOPPING MALL PROJECT')
    window_with = 200
    window_height = 100
    monitor_width = window.winfo_screenwidth()
    monitor_height = window.winfo_screenheight()
    x = (monitor_width / 2) - (window_with / 2)
    y = (monitor_height / 2) - (window_height / 2)
    window.geometry('%dx%d+%d+%d' % (window_with, window_height, x, y))

    edtFrame = Frame(window);
    edtFrame.pack();
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
    # #   Input Email
    # inputEmail = Entry(edtFrame, width = 10);  inputEmail.pack(padx=10, pady=10)
    # #   Input Password
    # inputPassword = Entry(edtFrame, width = 10);  inputPassword.pack(padx=10, pady=10)

    # Login Button
    edt = Entry(window, width=10)
    loginbtn = Button(window, text='로그인', width=10, command=memberLoginBTN)
    loginbtn.pack(padx=10, pady=10)
    memerManagement = Button(window, text='회원가입', width=10, command=memerJoinBTN)
    memerManagement.pack(padx=10, pady=10)

    window.mainloop()
