from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *

def clickButton() :
    messagebox.showinfo("You click this button","context");
#gui관련 Action을 event라고 한다. 클릭, 시간이 흐르는것, 키보드입력
def leftMouseClick(event) : # 클릭시 마우스에 대한 정보가 들어온다.
    txt = '클릭좌표 :';
    x = event.x;
    y = event.y;
    txt += str(x) + ',' + str(y);
    lable1.configure(text=txt);
def keyEvent(event) : # 클릭시 마우스에 대한 정보가 들어온다.
    txt = '누른키 :';
    txt += chr(event.keycode);
    lable1.configure(text=txt);
    
def openFile() :
    lable1.configure(text="메뉴 : 파일 >> 열기")
def copyFile() :
    lable1.configure(text="메뉴 : 파일 >> 복사")
def addImage() :
    value = askinteger("밝게할 값", "값 입력:",minvalue=1, maxvalue=255);
    lable1.configure(text="밝게하기"+str(value))

window = Tk();
#마우스 이벤트
# window.bind("<Button-1>",leftMouseClick)

#키보드 이벤트
window.bind("<Key>",keyEvent);

#메뉴 만들기
mainMenu = Menu(window);
window.configure(menu=mainMenu);

fileMenu = Menu(mainMenu);
mainMenu.add_cascade(label="파일",menu=fileMenu);
fileMenu.add_command(label="열기(Open)", command=openFile)
fileMenu.add_separator();
fileMenu.add_command(label="닫기(Close)")

editMenu = Menu(mainMenu);
mainMenu.add_cascade(label="영상처리",menu=editMenu);
editMenu.add_command(label="복사(Copy)", command=copyFile);
editMenu.add_command(label="밝게하기", command=addImage);


window.title("요기 제목");
window.geometry('500x500');
window.resizable(width=False, height=False);

lable1 = Label(window, text="lable1");
lable2 = Label(window, text="lable2" ,font=("궁서체",30), fg="red");
lable3 = Label(window, text="lable3" ,font=("궁서체",30), fg="red", bg="blue");
#그림 삽입349
#파이썬은 gif파일만 인식한다.
photo=PhotoImage(file='C:/images/GIF/cat.gif')
lable4 = Label(window, image=photo);
lable4.bind("<Button-1>",leftMouseClick)

#버튼은 단순이 이미지, 눌렀을 때 반응하는 이벤트를 넣어주어야 반응한다.
button1 = Button(window, text='button1command 없는 버튼', fg='red');
#command 뒤에 나오는 clickButton은 콜뱃함수로 괄호가 붙지않는다.
button2 = Button(window, text='button2command 있는 버튼', fg='red', command=clickButton);

lable1.pack()
lable2.pack()
lable3.pack()
lable4.pack()

button1.place(x = 300, y = 400);
button2.pack();

window.mainloop();


