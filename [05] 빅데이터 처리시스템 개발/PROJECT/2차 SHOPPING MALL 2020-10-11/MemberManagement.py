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

def memberManagement(conn,cur,email,name):
    print('memberManagement 회원관리 페이지[',email,name,']')

    ##====================================================================================
    ##  함수 선언부
    
    ##      INSERT
    def insertMemberData() :

        print("insertMemberData(입력 버튼 클릭)["+email,name+']')
        # conn, cur = conn, cur # 교량과 트럭
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,db=DB, charset="utf8")
        cur = conn.cursor()  # 빈 트럭 준비
    
        '''
        m_email	VARCHAR(30) 	PRIMARY KEY,	#회원 이메일
        m_pw		VARCHAR(50)		NOT NULL,		#회원 비밀번호
        m_name	VARCHAR(25) 	NOT NULL,		#이름
        s_tel		INT				NULL,				#연락처
        order_num INT				NULL				#주문번호
        '''

        sql = "INSERT INTO member (m_email,m_pw,m_name,s_tel)"
        sql += "VALUES('"+m_email.get()+"','"+m_pw.get()+"','"+m_name.get() +"',"+s_tel.get()+")"

        sql2 = "INSERT INTO member (m_email,m_pw,m_name,s_tel)"
        sql2 += "VALUES(" + m_email.get() + "," + m_pw.get() + "," + m_name.get() + "," + s_tel.get() + ")"

        log = "INSERT INTO memberLog (m_email,m_name,querry,method)"
        log += "VALUES('"+email+"','"+name+"','"+sql2+"','insertMemberData()')"

        print('SQL : ',sql)
        print('LOG : ',log)

        ##  Execute Querry
        if m_email.get == None or m_email.get() == '' or m_pw.get() == None or m_pw.get() == '':
            messagebox.showerror('오류', '데이터 입력 오류 발생')

        else :
            try :
                cur.execute(log)
                cur.execute(sql)
            except :
                messagebox.showerror('오류', '데이터 입력 오류 발생')
            else :
                messagebox.showinfo('성공' , '데이터 입력 성공')
                
        ##  Querry End  After Execute and Commit
        conn.commit()
        conn.close()
        selectMemberData()
    ## ====== The end of Method ====== ##

    ##      SELECT
    def selectMemberData() :

        print("selectMemberData(조회 버튼 클릭)["+email,name+']')
        strData1, strData2, strData3, strData4, strData5 = [], [], [], [], []
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,db=DB, charset="utf8")
        cur = conn.cursor()  # 빈 트럭 준비

        ##  Execute Querry
        sql = "SELECT * FROM member"
        log = "INSERT INTO memberLog (m_email,m_name,querry,method)"
        log += "VALUES('" + email + "','" + name + "','[" + sql + "]','selectMemberData()')"
        print('SQL : ', sql)
        print('LOG : ',log)
        cur.execute(log)
        cur.execute(sql)

        strData1.append("회원 이메일"); strData2.append("회원 비밀번호[추후 삭제]"); strData3.append("회원명");
        strData4.append("연락처");
    
        strData1.append("----------"); strData2.append("----------"); strData3.append("----------");
        strData4.append("----------");
    
        while (True) :
            row = cur.fetchone()
            if row == None :
                break;
            strData1.append(row[0]); strData2.append(row[1]); strData3.append(row[2]);
            strData4.append(row[3]);
    
        listData1.delete(0, listData1.size() - 1);
        listData2.delete(0, listData2.size() - 1);
        listData3.delete(0, listData3.size() - 1);
        listData4.delete(0, listData4.size() - 1);
    
        for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4) :
            listData1.insert(END, item1); listData2.insert(END, item2);
            listData3.insert(END, item3); listData4.insert(END, item4);
    
        conn.close()
    ## ====== The end of Method ====== ##

    ##      DELETE
    def deleteMemberData():

        print("deleteMemberData(삭제 버튼 클릭)["+email,name+']')
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset="utf8")
        cur = conn.cursor()  # 빈 트럭 준비

        ##  Execute Querry
        sql = "DELETE FROM member WHERE m_email LIKE '"+(m_email2.get())+"'"
        sql2 = "DELETE FROM member WHERE m_email LIKE " + (m_email2.get()) + ""
        log = "INSERT INTO memberLog (m_email,m_name,querry,method)"
        log += "VALUES('"+email+"','"+name+"','["+sql2+"]','deleteMemberData()')"

        print('SQL : ', sql)
        print('LOG : ', log)


        try:
            cur.execute(log)
            cur.execute(sql)
        except:
            messagebox.showerror('오류', '데이터 입력 오류 발생')
        else:
            messagebox.showinfo('성공', '데이터 입력 성공')

        ##  Querry End  After Execute and Commit
        conn.commit()
        conn.close()
        selectMemberData()
    ## ====== The end of Method ====== ##

    ##      UPDATE
    def updateMemberData():

        print("updateMemberData(수정 버튼 클릭)["+m_name.get(),name+']')
        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset="utf8")
        cur = conn.cursor()  # 빈 트럭 준비

        sql = "UPDATE member SET"
        sql += " m_pw = '" + m_pw.get() + "',"
        sql += " m_name = '" + m_name.get() + "',"
        sql += " s_tel = " + s_tel.get()
        sql += " WHERE m_email = '" + m_email.get() + "'"

        sql2 = "UPDATE member SET"
        sql2 += " m_pw = " + m_pw.get() + ","
        sql2 += " m_name = " + m_name.get() + ","
        sql2 += " s_tel = " + s_tel.get()
        sql2 += " WHERE m_email = " + m_email.get()

        log = "INSERT INTO memberLog (m_email,m_name,querry,method)"
        log += "VALUES('"+m_email.get()+"','"+ m_name.get()+"','["+sql2+"]','updateMemberData()')"

        print('SQL : ', sql)
        print('LOG : ', log)

        ##  Execute Querry
        try:
            cur.execute(log)
            cur.execute(sql)
        except:
            messagebox.showerror('오류', '데이터 입력 오류 발생')
        else:
            messagebox.showinfo('성공', '데이터 입력 성공')
        ##  Querry End  After Execute and Commit
        conn.commit()
        conn.close()
        selectMemberData()
    ## ====== The end of Method ====== ##

    ##      Go to Main
    def goMain():

        conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, db=DB, charset="utf8")
        cur = conn.cursor()

        print('메인 버튼 클릭[' + email,name + ']')
        window.destroy()
        SubMain.mainPage(conn,cur,email,name)
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
    
    m_email = Entry(edtFrame, width=10);   m_email.pack(side=LEFT, padx=10, pady=10)
    m_pw = Entry(edtFrame, width=10);   m_pw.pack(side=LEFT, padx=10, pady=10)
    m_name = Entry(edtFrame, width=10);   m_name.pack(side=LEFT, padx=10, pady=10)
    s_tel = Entry(edtFrame, width=10);   s_tel.pack(side=LEFT, padx=10, pady=10)

    ## BUTTON
    btnInsert = Button(edtFrame, text="회원입력",command=insertMemberData)
    btnInsert.pack(side=LEFT,padx=10,pady=10)
    btnSelect = Button(edtFrame, text="회원조회",command=selectMemberData)
    btnSelect.pack(side=LEFT,padx=10,pady=10)
    btnUpdate = Button(edtFrame, text="회원수정", command=updateMemberData)
    btnUpdate.pack(side=LEFT, padx=10, pady=10)

    m_email2 = Entry(edtFrame, width=10);    m_email2.pack(side=LEFT, padx=10, pady=10)
    btnSelect = Button(edtFrame, text="회원삭제", command=deleteMemberData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

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
    
    # listData5 = Listbox(listFrame, bg = 'white')
    # listData5.pack(side=LEFT, fill=BOTH, expand=1)
    
    window.mainloop()
