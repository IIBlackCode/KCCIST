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
import SubMain
import pymysql
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def memberLog(email,name):
    print('memberManagement 회원관리 페이지[',email,name,']')

    ##====================================================================================
    ##  함수 선언부
    ##      SELECT
    def selectMemberLog() :

        print("selectMemberData(조회 버튼 클릭)["+email,name+']')
        strData1, strData2, strData3, strData4, strData5 = [], [], [], [], []
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,db=DB, charset="utf8")
        cur = conn.cursor()  # 빈 트럭 준비

        ##  Execute Querry
        sql = "SELECT * FROM memberLog WHERE m_email LIKE '"+m_email.get()+"'"
        print(sql)
        try:
            cur.execute(sql)
        except:
            messagebox.showerror('오류', '데이터 입력 오류 발생')
        else:
            messagebox.showinfo('성공', '데이터 입력 성공')
        
        strData1.append("회원 이메일"); strData2.append("회원명"); strData3.append("실행쿼리|형상처리 내역");
        strData4.append("실행메소드");  strData5.append("실행시간");
    
        strData1.append("----------"); strData2.append("----------"); strData3.append("----------");
        strData4.append("----------"); strData5.append("----------");
    
        while (True) :
            row = cur.fetchone()
            if row == None :
                break;
            strData1.append(row[0]); strData2.append(row[1]); strData3.append(row[2]);
            strData4.append(row[3]); strData5.append(row[4]);
    
        listData1.delete(0, listData1.size() - 1);
        listData2.delete(0, listData2.size() - 1);
        listData3.delete(0, listData3.size() - 1);
        listData4.delete(0, listData4.size() - 1);
        listData5.delete(0, listData5.size() - 1);

        for item1, item2, item3, item4, item5 in zip(strData1, strData2, strData3, strData4, strData5) :
            listData1.insert(END, item1); listData2.insert(END, item2);
            listData3.insert(END, item3); listData4.insert(END, item4);
            listData5.insert(END, item5);
    
        conn.close()
    ## ====== The end of Method ====== ##

    ##      Go to Main
    def goMain():

        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset="utf8")
        cur = conn.cursor()

        print('메인 버튼 클릭[' + email, name + ']')
        window.destroy()
        SubMain.mainPage(conn, cur, email, name)
    ## ====== The end of Method ====== ##

    ##====================================================================================
    ## 전역변수부
    HOST = "127.0.0.1"
    USER ="root"
    PASSWORD ="1234"
    DB = "shopping_mall"

    ##====================================================================================
    ##  MainCode
    window = tk.Tk()
    window.title('SHOPPING MALL PROJECT')
    window_with = 1000
    window_height = 500
    monitor_width = window.winfo_screenwidth()
    monitor_height = window.winfo_screenheight()
    x = (monitor_width / 2) - (window_with / 2)
    y = (monitor_height / 2) - (window_height / 2)
    window.geometry('%dx%d+%d+%d' % (window_with, window_height, x, y))

    
    edtFrame = Frame(window);
    edtFrame.pack();
    listFrame = Frame(window)
    listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)
    
    m_email = Entry(edtFrame, width=20);  m_email.pack(side=LEFT, padx=10, pady=10)


    ## BUTTON

    btnSelect = Button(edtFrame, text="회원조회",command=selectMemberLog)
    btnSelect.pack(side=LEFT,padx=10,pady=10)


    mainBTN = Button(edtFrame, text="MAIN", command=goMain)
    mainBTN.pack(side=LEFT, padx=10, pady=10)

    listData1 = Listbox(listFrame, bg = 'white')
    listData1.pack(side=LEFT, fill=BOTH, expand=1)
    
    listData2 = Listbox(listFrame, bg = 'white')
    listData2.pack(side=LEFT, fill=BOTH, expand=1)
    
    listData3 = Listbox(listFrame, bg = 'white')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)
    
    listData4 = Listbox(listFrame, bg = 'white')
    listData4.pack(side=LEFT, fill=BOTH, expand=1)

    listData5 = Listbox(listFrame, bg='white')
    listData5.pack(side=LEFT, fill=BOTH, expand=1)
    
    # listData5 = Listbox(listFrame, bg = 'white')
    # listData5.pack(side=LEFT, fill=BOTH, expand=1)
    
    window.mainloop()
