import pymysql
from tkinter import *
from tkinter import messagebox
from datetime import datetime # 시간받아오기

## 함수 선언부
def insertStudentData():
    global conn,cur
    global s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time
    global edt1,edt2,edt3,edt4,edt5
    global listData1,listData2,listData3,listData4,listData5
    sql = ""

    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,
                           db=DB, charset="utf8")
    cur = conn.cursor()  # 빈 트럭 준비

    s_id = edt1.get()        #id
    s_name = edt2.get()      #이름
    s_age = edt3.get()       #나이
    s_adress = edt4.get()       #주소
    s_phone = edt5.get()       #폰

    try:
        sql = "INSERT INTO studentTbl(s_id, s_name, s_age, s_adress, s_phone) "
        sql += "VALUES ('"+ s_id + "', '" + s_name + "', '"+ s_age +"', '"
        sql += s_adress +"', '" + s_phone + "' )"
        cur.execute(sql)
    except :
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
    else :
        messagebox.showinfo("성공", "데이터 입력 성공")

    conn.commit()
    # 끝. 정리하기
    cur.close()
    conn.close()
def insertChulseokData():
    global conn,cur
    global s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time
    global edt1,edt2,edt3,edt4,edt5
    global listData1,listData2,listData3,listData4,listData5
    sql = ""

    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,
                           db=DB, charset="utf8")
    cur = conn.cursor()  # 빈 트럭 준비

    s_id = edt1.get()        #id
    s_chulseok = edt2.get()  #출석

    if s_chulseok == "Y" :
        now = datetime.now()   #시간
        s_time = "" + str(now.year) +"-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) \
                 + ":" + str(now.minute) + ":" + str(now.second) + ""
    elif s_chulseok == "N":
        s_time = "NULL"
    else:
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")

    try:
        # 2020-10-06 08:40:00
        sql = ""
        sql = "INSERT INTO chulseokTbl(num, s_id, s_chulseok, s_time) "
        sql += "VALUES  (NULL, '" + s_id + "', '"+ s_chulseok +"', '" + s_time + "' )"
        cur.execute(sql)
    except :
        messagebox.showerror("오류", "데이터 입력 오류가 발생함")
    else :
        messagebox.showinfo("성공", "데이터 입력 성공")

    conn.commit()
    # 끝. 정리하기
    cur.close()
    conn.close()
def selectStudentData():
    global conn,cur
    global s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time
    global edt1,edt2,edt3,edt4,edt5
    global listData1,listData2,listData3,listData4,listData5
    strData1, strData2, strData3, strData4, strData5 = [], [], [], [], []
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,
                           db=DB, charset="utf8")
    cur = conn.cursor()  # 빈 트럭 준비
    # 2. 물건(SQL) 준비 + 트럭에 실어서 부어 넣기
    sql = "SELECT * FROM studentTbl"
    cur.execute(sql)

    # # 3. 돌아온 트럭(cur)에서 하나씩 꺼내기
    # while True:
    #     row = cur.fetchone()  # 한칸 꺼내
    #     if row == None:
    #         break
    #     uid = row[0]
    #     uname = row[1]
    #     uemail = row[2]
    #     byear = row[3]
    #     print(uid, uname, uemail, byear)

    strData1.append("학생 ID")
    strData2.append("학생 이름")
    strData3.append("학생 나이")
    strData4.append("학생 주소")
    strData5.append("학생 연락처")
    strData1.append("----------")
    strData2.append("----------")
    strData3.append("----------")
    strData4.append("----------")
    strData5.append("----------")

    while (True):
        row = cur.fetchone()  # 한줄씩 출력
        if row == None:
            break
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(str(row[2]))
        strData4.append(row[3])
        strData5.append(row[4])

    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)
    listData4.delete(0, listData4.size() - 1)
    listData5.delete(0, listData5.size() - 1)

    for item1, item2, item3, item4, item5 in zip(strData1, strData2, strData3, strData4, strData5):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
        listData5.insert(END, item5)

    cur.close()
    conn.close()

def selectChulseokData():
    global conn,cur
    global s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time
    global edt1,edt2,edt3,edt4,edt5
    global listData1,listData2,listData3,listData4,listData5
    strData1, strData2, strData3 = [], [], []
    conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD,
                           db=DB, charset="utf8")
    cur = conn.cursor()  # 빈 트럭 준비
    # 2. 물건(SQL) 준비 + 트럭에 실어서 부어 넣기

    sql = "SELECT  s_name, s_chulseok, s_time FROM studentTbl "
    sql += "JOIN chulseokTbl ON studentTbl.s_id = chulseokTbl.s_id"
    cur.execute(sql)

    # # 3. 돌아온 트럭(cur)에서 하나씩 꺼내기
    # while True:
    #     row = cur.fetchone()  # 한칸 꺼내
    #     if row == None:
    #         break
    #     uid = row[0]
    #     uname = row[1]
    #     uemail = row[2]
    #     byear = row[3]
    #     print(uid, uname, uemail, byear)

    strData1.append("학생 이름")
    strData2.append("학생 출석")
    strData3.append("학생 시간")
    strData1.append("----------")
    strData2.append("----------")
    strData3.append("----------")


    while (True):
        row = cur.fetchone()  # 한줄씩 출력
        if row == None:
            break
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])


    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)


    for item1, item2, item3 in zip(strData1, strData2, strData3):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)

    cur.close()
    conn.close()

def studentTable() :
    global conn,cur
    global s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time
    global edt1,edt2,edt3,edt4,edt5
    global listData1,listData2,listData3,listData4,listData5
    edtFrame = Frame(window)
    edtFrame.pack()
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    # 입력하는 창 생성
    edt1 = Entry(edtFrame, width=10);
    edt1.pack(side=LEFT, padx=10, pady=10)
    edt2 = Entry(edtFrame, width=10);
    edt2.pack(side=LEFT, padx=10, pady=10)
    edt3 = Entry(edtFrame, width=10);
    edt3.pack(side=LEFT, padx=10, pady=10)
    edt4 = Entry(edtFrame, width=10);
    edt4.pack(side=LEFT, padx=10, pady=10)
    edt5 = Entry(edtFrame, width=10);
    edt5.pack(side=LEFT, padx=10, pady=10)

    # 입력버튼 생성
    btnInsert = Button(edtFrame, text="입력", command=insertStudentData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    # 조회버튼 생성
    btnSelect = Button(edtFrame, text="조회", command=selectStudentData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    listData1 = Listbox(listFrame, bg='yellow')
    listData1.pack(side=LEFT, fill=BOTH, expand=1)
    listData2 = Listbox(listFrame, bg='yellow')
    listData2.pack(side=LEFT, fill=BOTH, expand=1)
    listData3 = Listbox(listFrame, bg='yellow')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)
    listData4 = Listbox(listFrame, bg='yellow')
    listData4.pack(side=LEFT, fill=BOTH, expand=1)
    listData5 = Listbox(listFrame, bg='yellow')
    listData5.pack(side=LEFT, fill=BOTH, expand=1)
def chulseokTable() :
    global conn,cur
    global s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time
    global edt1,edt2,edt3,edt4,edt5
    global listData1,listData2,listData3,listData4,listData5
    edtFrame = Frame(window)
    edtFrame.pack()
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    # 입력하는 창 생성
    edt1 = Entry(edtFrame, width=10);
    edt1.pack(side=LEFT, padx=10, pady=10)
    edt2 = Entry(edtFrame, width=10);
    edt2.pack(side=LEFT, padx=10, pady=10)

    # 입력버튼 생성
    btnInsert = Button(edtFrame, text="입력", command=insertChulseokData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    # 조회버튼 생성
    btnSelect = Button(edtFrame, text="조회", command=selectChulseokData)
    btnSelect.pack(side=LEFT, padx=10, pady=10)

    listData1 = Listbox(listFrame, bg='gray')
    listData1.pack(side=LEFT, fill=BOTH, expand=1)
    listData2 = Listbox(listFrame, bg='gray')
    listData2.pack(side=LEFT, fill=BOTH, expand=1)
    listData3 = Listbox(listFrame, bg='gray')
    listData3.pack(side=LEFT, fill=BOTH, expand=1)


    window.mainloop()

## 전역변수부
conn, cur = None, None
HOST = "127.0.0.1"
USER ="root"
PASSWORD ="1234"
DB = "javaBigDataStudentDB"
s_id, s_name, s_age, s_adress, s_phone, s_chulseok, s_time = "", "", "", "", "", "", ""


## 메인코드부

if __name__ == "__main__":
    window = Tk()
    window.geometry("900x300")
    window.title("출석 데이터 입력")

    edtFrame = Frame(window)
    edtFrame.pack()
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    # 입력하는 창 생성
    edt1 = Entry(edtFrame, width=10);
    edt2 = Entry(edtFrame, width=10);
    edt3 = Entry(edtFrame, width=10);
    edt4 = Entry(edtFrame, width=10);
    edt5 = Entry(edtFrame, width=10);


    ### 메뉴 만들기 ###
    mainMenu = Menu(window)
    window.configure(menu=mainMenu)

    studentMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="학생", menu=studentMenu)
    studentMenu.add_command(label="학생테이블", command=studentTable)

    chulseokMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="출석", menu=chulseokMenu)
    chulseokMenu.add_command(label="출석테이블", command=chulseokTable)

    listData1 = Listbox(listFrame, bg='yellow')
    listData2 = Listbox(listFrame, bg='yellow')
    listData3 = Listbox(listFrame, bg='yellow')
    listData4 = Listbox(listFrame, bg='yellow')
    listData5 = Listbox(listFrame, bg='yellow')

    window.mainloop()
