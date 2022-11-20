#tkinter : GUI관련 제공해주는 표준 윈도우 라이브러리
#          윈도우 창 생성시 사용
from tkinter import *

#Tk() : 윈도우 반환
window = Tk();

    #window 창 구현부
window.title("Window.title");               #윈도우 창 제목
window.geometry("500x600");                 #윈도우 창 크기 지정
window.resizable(width=False, height=False) #윈도우 창 크기 고정
    #The end of Window

    #Lable 구현부
lable1 = Label(window, text=" 1");
lable2 = Label(window, text=" 2", font=("D2Coding",30)); #bg : background, 배경색
lable3 = Label(window, text=" 3", font=("D2Coding",30), bg='blue');     #fg : foreground 약자, 글자색
lable4 = Label(window, text=" 4", font=("D2Coding",30), bg='red',       fg='black');             #anchor : 위젯의 위치,
lable5 = Label(window, text=" 5", font=("D2Coding",30), bg='green',     fg='black', width=20);   #SE : South East,
lable6 = Label(window, text=" 6", font=("D2Coding",30), bg='yellow',    fg='black', width=20, height=5);
lable7 = Label(window, text=" 7", font=("D2Coding",30), bg='magenta',   fg='black', width=20, height=5, anchor=SE);

    #이미지 삽입 구현부 349Page
photo = PhotoImage(file="C:/Users/kccistc/Desktop/김민서/images/GIF/froyo.gif");
lable8 = Label(window, image=photo);

lable1.pack();
lable2.pack();
lable3.pack();
lable4.pack();
lable5.pack();
lable6.pack();
lable7.pack();
lable8.pack();
    #The end of Lable

#윈도우창에 이벤트 처리
window.mainloop();