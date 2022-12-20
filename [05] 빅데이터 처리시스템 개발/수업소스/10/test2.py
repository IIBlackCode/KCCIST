from tkinter import *
## 함수 선언부
def selectMemberData() :
    global inputEmail
    print(str(inputEmail.get()))
## 전역 변수부
inputEmail=""

## 메인코드부
def main(login) :
    window = Tk()

    window.geometry('400x400')

    text1 = Label(window, text=login)
    text1.pack()

    edtFrame = Frame(window);
    edtFrame.pack();

    inputEmail = Entry(edtFrame, width = 10);  inputEmail.pack(padx=10, pady=10)
    btnInsert = Button(edtFrame, text="Login",command=selectMemberData)
    btnInsert.pack(padx=10,pady=10)

    window.mainloop()
