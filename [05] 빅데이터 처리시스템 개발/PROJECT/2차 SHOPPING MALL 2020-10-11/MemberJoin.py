import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk
def memberManagement(conn,cur):

    ##====================================================================================
    ##  함수 선언부
    
    ##      Data삽입 함수
    def insertMemberData() :
        # global conn, cur
        print("insertMemberData(입력 버튼 클릭)")
    
        # conn, cur = None, None # 교량과 트럭
        data1, data2, data3, data4 = "", "", "", ""
        data5 = ""
        sql = ""
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,db=DB, charset="utf8")
        cur = conn.cursor()  # 빈 트럭 준비
    
        data1 = edt1.get();
        data2 = edt2.get();
        data3 = edt3.get();
        data4 = edt4.get();
        # data5 = edt5.get();
    
        '''
        m_email	VARCHAR(30) 	PRIMARY KEY,	#회원 이메일
        m_pw		VARCHAR(50)		NOT NULL,		#회원 비밀번호
        m_name	VARCHAR(25) 	NOT NULL,		#이름
        s_tel		INT				NULL,				#연락처
        order_num INT				NULL				#주문번호
        '''
        #   중복 체크
        sql = "SELECT m_email FROM member"
        cur.execute(sql)
        email_DB = ''
        while (True) :
            row = cur.fetchone()
            if row == None :
                break;
            email_DB = row[0];
            if email_DB == data1 :
                messagebox.showerror('Error', '중복된 아이디 입니다.')
                break;

        sql = "INSERT INTO member (m_email,m_pw,m_name,s_tel)"
        sql += "VALUES('"+data1+"','"+data2+"','"+data3 +"',"+data4+")"

        try :
            # sql = "INSERT INTO student VALUES("+data1+",'"+data2+"','"+data3+"','"+data4 +"')"
            print(sql)
            cur.execute(sql)
        except :
            if (email_DB != data1):
                messagebox.showerror('오류', '데이터 입력 오류 발생')
        else :
            messagebox.showinfo('성공' , '데이터 입력 성공')
    
        conn.commit()
        conn.close()
        window.destroy()
    ##====================================================================================
    ## 전역변수부
    HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "1234"
    DB = "shopping_mall"
    ##====================================================================================
    ##  MainCode
    window = tk.Tk()
    window.title('        입력 :         아이디,           비밀번호,              이름,              전화번호')
    window_with = 650
    window_height = 50
    monitor_width = window.winfo_screenwidth()
    monitor_height = window.winfo_screenheight()
    x = (monitor_width / 2) - (window_with / 2)
    y = (monitor_height / 2) - 100
    window.geometry('%dx%d+%d+%d' % (window_with, window_height, x, y))
    
    edtFrame = Frame(window);
    edtFrame.pack();
    listFrame = Frame(window)
    listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)
    
    edt1 = Entry(edtFrame, width=10);   edt1.pack(side=LEFT, padx=10, pady=10)
    edt2 = Entry(edtFrame, width=10);   edt2.pack(side=LEFT, padx=10, pady=10)
    edt3 = Entry(edtFrame, width=10);   edt3.pack(side=LEFT, padx=10, pady=10)
    edt4 = Entry(edtFrame, width=10);   edt4.pack(side=LEFT, padx=10, pady=10)
    # edt5 = Entry(edtFrame, width=10);   edt5.pack(side=LEFT, padx=10, pady=10)
    
    ## BUTTON
    btnInsert = Button(edtFrame, text="회원가입",command=insertMemberData)
    btnInsert.pack(side=LEFT,padx=10,pady=10)

    window.mainloop()
