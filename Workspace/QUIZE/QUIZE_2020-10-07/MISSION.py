'''

#미션1. [자바빅데이터] 학생 테이블 및 출석 테이블을 생성하고, 학생3명 및 각 출석 7건을 입력한다.
CREATE DATABASE javabigdata
USE javabigdata

##학생 테이블
DROP TABLE student;
CREATE TABLE student (
	s_num		SMALLINT 	PRIMARY KEY AUTO_INCREMENT,	#학번
	s_name	CHAR(25)		NOT NULL,		#이름
	s_mail	VARCHAR(25) NOT NULL,		#메일
	s_addr	VARCHAR(25)		NOT NULL,	#주소
	s_tel		INT			NULL				#연락처
);

SELECT * FROM student;
##출석 테이블


#미션2. p655를 참조해서, 위 학생 테이블을 입력/조회하는 프로그램을 작성
#미션3(선택). 위 미션1을 SQL Server에서 수행되도록 한다.
#미션4<심화>. 미션2에 변경/삭제 기능도 추가한다.
#미션5(선택). 위 미션4를 SQL Server에서 수행되도록 한다.

﻿

'''

import pymysql
from tkinter import *
from tkinter import messagebox
##====================================================================================
##  함수 선언부

##      Data삽입 함수
def insertData() :
    print("insertData(입력 버튼 클릭)")

    conn, cur = None, None # 교량과 트럭
    data1, data2, data3, data4 = "", "", "", ""
    data5 = ""
    sql = ""
    conn = pymysql.connect(host="127.0.0.1", user = "root", password = "1234", db = "javabigdata", charset = "utf8")
    cur = conn.cursor() # 빈 트럭 준비

    # data1 = edt1.get();
    data2 = edt2.get();
    data3 = edt3.get();
    data4 = edt4.get();
    data5 = edt5.get();

    '''
        s_num	SMALLINT 	PRIMARY KEY,    #학번
        s_name	CHAR(5)		NOT NULL,	    #이름
        s_mail	VARCHAR(25) NOT NULL,	    #메일
        s_addr	VARCHAR(25)	NOT NULL,		#주소
        s_tel	INT			NULL		    #연락처
    '''

    try :
        sql = "INSERT INTO student (s_name,s_mail,s_addr,s_tel)"
        sql += "VALUES('"+data2+"','"+data3+"','"+data4 +"',"+data5+")"
        # sql = "INSERT INTO student VALUES("+data1+",'"+data2+"','"+data3+"','"+data4 +"')"
        print(sql)
        cur.execute(sql)
    except :
        messagebox.showerror('오류', '데이터 입력 오류 발생')
    else :
        messagebox.showinfo('성공' , '데이터 입력 성공')

    conn.commit()
    conn.close()
    selectData()

def selectData() :
    print("selectData(조회 버튼 클릭)")
    strData1, strData2, strData3, strData4, strData5 = [], [], [], [], []
    conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", db="javabigdata", charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    strData1.append("학번"); strData2.append("이름"); strData3.append("메일");
    strData4.append("주소"); strData5.append("연락처");

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



##====================================================================================
##  MainCode
window = Tk()
window.title('GUI 데이터 입력')
window.geometry('800x300')

edtFrame = Frame(window);
edtFrame.pack();
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

# edt1 = Entry(edtFrame, width=10);   edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10);   edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10);   edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10);   edt4.pack(side=LEFT, padx=10, pady=10)
edt5 = Entry(edtFrame, width=10);   edt5.pack(side=LEFT, padx=10, pady=10)

## BUTTON
btnInsert = Button(edtFrame, text="입력",command=insertData)
btnInsert.pack(side=LEFT,padx=10,pady=10)
btnSelect = Button(edtFrame, text="조회",command=selectData)
btnSelect.pack(side=LEFT,padx=10,pady=10)

listData1 = Listbox(listFrame, bg = 'white')
listData1.pack(side=LEFT, fill=BOTH, expand=1)

listData2 = Listbox(listFrame, bg = 'white')
listData2.pack(side=LEFT, fill=BOTH, expand=1)

listData3 = Listbox(listFrame, bg = 'white')
listData3.pack(side=LEFT, fill=BOTH, expand=1)

listData4 = Listbox(listFrame, bg = 'white')
listData4.pack(side=LEFT, fill=BOTH, expand=1)

listData5 = Listbox(listFrame, bg = 'white')
listData5.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
