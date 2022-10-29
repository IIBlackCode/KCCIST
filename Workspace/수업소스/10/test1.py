import test2
from tkinter import *

def clickBtn() :
    login = edt.get()
    window.destroy()
    test2.main(login)

window = Tk()
window.geometry('200x200')

edt = Entry(window, width = 10)
btn = Button(window, text='로그인', command=clickBtn)

edt.pack()
btn.pack()
window.mainloop()
