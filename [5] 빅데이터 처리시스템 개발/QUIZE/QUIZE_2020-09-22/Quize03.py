from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import math

### 함수 선언부
#### 공통 함수 ####

def malloc(h, w, value=0) :
    retMemory = [ [ value for _ in range(w)]  for _ in range(h) ]
    return retMemory

def openFile() :
    global window, canvas, paper, inImage, outImage ,inH, inW, outH, outW ,filename

    ## 파일 선택하기
    filename = askopenfilename(parent=window,
        filetypes=( ('RAW 파일', '*.raw'),('All File', '*.*') ) )

    ## (중요!) 입력이미지의 높이와 폭 알아내기
    fsize = os.path.getsize(filename)
    inH = inW = int(math.sqrt(fsize))

    ## 입력이미지용 메모리 할당
    inImage = malloc(inH, inW)

    ## 파일 --> 메모리 로딩
    with open(filename,'rb') as fp :
        for i in range(inH) :
            for k in range(inW) :
                inImage[i][k] = int(ord(fp.read(1)))
    pixelMenu_1()

import struct

def saveFile() :
    global window, canvas, paper, inImage, outImage ,inH, inW, outH, outW ,filename

    if filename == '' or filename == None :
        return
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw',
                           filetypes=(('RAW 파일', '*.raw'), ('All File', '*.*')))

    for i in range(outH) :
        for k in range(outW) :
            saveFp.write(struct.pack('B', outImage[i][k]))
    saveFp.close()

def displayImage() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    window.geometry(str(outH)+'x'+str(outW))
    if canvas != None :
        canvas.destroy()
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)

    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal')

    # 볼펜으로 콕콕콕 찍기  --> 열라 느림
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put("#%02x%02x%02x" % (r, g, b), (k, i))

    # 메모리에서 처리한 후, 한방에 화면에 보이기 --> 완전 빠름
    rgbString =""
    for i in range(outH) :
        tmpString = "" # 각 줄
        for k in range(outW) :
            r = g = b = outImage[i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack()

##### 영상처리 함수 ######

def pixelMenu_1() :  # 동일영상 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW

    ## 출력이미지 메모리 할당
    outImage=malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
    ########################

    displayImage()

#미션1 : 화소점 처리 --> 동일영상/밝게/어둡게/이진화/이진화(평균값)/이진화(중위수)
#영상반전/포스터라이징/감마/파라볼라(캡)/파라볼라(컵)

def pixelMenu_2() :  # 밝게하기 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None :
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;    outW = inW

    ## 출력이미지 메모리 할당
    outImage=malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("밝게할 값", "값-->", minvalue=1, maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] + value > 255 :
                outImage[i][k] = 255
            else :
                outImage[i][k] = inImage[i][k] + value
    ########################
    displayImage()

#어둡게
def pixelMenu_3() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("어둡게 할 값", "값-->", minvalue=1, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] - value < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] - value
    ########################
    displayImage()


#이진화
def pixelMenu_4() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 이진화 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < 127:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = 255;
    ########################
    displayImage()


#이진화(평균값)
def pixelMenu_5() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 이진화 평균값 알고리즘 ###

    ##평균값
    sum = 0;
    count =0;
    for i in range(inH):
        for k in range(inW):
            count +=1
            sum = sum + inImage[i][k];

    avg = math.ceil(sum/count)

    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < avg:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = 255;
    ########################
    displayImage()

#이진화(중위수)
def pixelMenu_6() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 이진화 평균값 알고리즘 ###

    ##중위수
    temp = []; #2차원 배열을 1차원 배열에 담기위한 temp변수
    for i in range(inH):
        for k in range(inW):
            temp.append(inImage[i][k]);

    #temp배열 정렬
    temp.sort();
    centerNum = math.ceil((inH * inW) / 2);
    center = temp[centerNum];

    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < center:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = 255;
    ########################
    displayImage()

#영상반전
def pixelMenu_7() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 영상반전 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] - 255 < 0:
                outImage[i][k] = (inImage[i][k]-255)*(-1);
            else :
                outImage[i][k] = (inImage[i][k] - 255);
    ########################
    displayImage()

#포스터라이징
def pixelMenu_8() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 포스터라이징 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] < 127:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = 255;
    ########################
    displayImage()
#감마
def pixelMenu_9() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    ### Out = I ** (1/r)

    r = askfloat("감마연산", "값-->", )
    for i in range(inH):
        for k in range(inW):
            v = int(inImage[i][k] ** (1 / r));
            if v > 255:
                outImage[i][k] = 255;
            elif v < 0:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = int(inImage[i][k] ** (1 / r));
    ########################
    displayImage()
#파라볼라(캡)
def pixelMenu_10() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2

    r = askfloat("감마연산", "값-->", )
    for i in range(inH):
        for k in range(inW):
            v = 255.0 * ((inImage[i][k] / 128.0 - 1.0) ** 2);
            if v > 255:
                outImage[i][k] = 255;
            elif v < 0:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = int(v);
    ########################
    displayImage()
#파라볼라(컵)
def pixelMenu_11() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2

    r = askfloat("감마연산", "값-->", )
    for i in range(inH):
        for k in range(inW):
            v = 255 - 255.0 * ((inImage[i][k] / 128.0 - 1.0) ** 2);
            if v > 255:
                outImage[i][k] = 255;
            elif v < 0:
                outImage[i][k] = 0;
            else:
                outImage[i][k] = int(v);
    ########################
    displayImage()

# 미션2 : 미러링(좌우)
def geometryMenu_1() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 미러링(좌우) 알고리즘 ###
    inW2 = math.ceil(inW);
    for i in range(inH):
        for k in range(inW2):
            outImage[i][k] = inImage[i][inW-k-1];

    ########################
    displayImage()

# 미션2 : 미러링(상하)
def geometryMenu_2() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 미러링(상하) 알고리즘 ###
    inW2 = math.ceil(inW);
    for i in range(inH):
        for k in range(inW2):

            outImage[i][k] = inImage[inH-i-1][k];

    ########################
    displayImage()

# 미션2 : 이동
def geometryMenu_3() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    x_axis = askinteger("움직일 크기값", "Enter the x-axis value[1~255]:", minvalue=1, maxvalue=255)
    y_axis = askinteger("움직일 크기값", "Enter the y-axis value[1~255]:", minvalue=1, maxvalue=255)

    for i in range(inH-y_axis):
        for k in range(inW-x_axis):
            outImage[i+y_axis][k+x_axis] = inImage[i][k];

    displayImage()

# 미션2 : 90도회전
def geometryMenu_4() :

    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 90도회전 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            outImage[k][inW-i-1] = inImage[i][k];
    ########################
    displayImage()

# 미션2 : 회전
def geometryMenu_5() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH*2;
    outW = inW*2-1;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 45도회전 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            outImage[k*-1][outW-k-i-1] = inImage[i][k];
    ########################
    displayImage()

# 미션2 : 확대
def geometryMenu_6() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH*2;
    outW = inW*2;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 확대 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            outImage[i+i][k+k] = inImage[i][k];
            outImage[i+i][k+k+1] = inImage[i][k];
            outImage[i+i+1][k+k] = inImage[i][k];
            outImage[i+i+1][k+k+1] = inImage[i][k];
    ########################
    displayImage()

# 미션2 : 축소
def geometryMenu_7() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = math.ceil(inH / 2);
    outW = math.ceil(inW / 2);

    ## 출력이미지 메모리 할당
    outImage = malloc(inH, inW)

    ### 축소 알고리즘 ###
    for i in range(outH):
        for k in range(outW):

            outImage[i][k] = math.ceil((inImage[i+i][k+k]+inImage[i+i+1][k+k]+inImage[i+i][k+k+1]+inImage[i+i+1][k+k+1])/4)
    ########################
    displayImage()

# (미션3) : 화소영역 처리 --> 블러링/샤프팅/엠보싱/경계추출.......
#블러링
def pixelAreaMenu_1():
    pass
#샤프팅
def pixelAreaMenu_2():
    pass
#엠보싱
def pixelAreaMenu_3():
    pass
#경계추출
def pixelAreaMenu_4():
    pass

# (미션4) : 히스토그램 처리 --> 히스토그램 평활화 .....
def HistogramMenu_1():
    pass

def test1():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(inH, inW)

    ### 축소 알고리즘 ###
    resolution = askinteger("축소할 값","Enter the resolution to be printed :", minvalue=32, maxvalue=128);

    for div in range(7,2,-1) :
        if (not(2**(div) < resolution))  :
            firstNum = 2**(div+1);
            # print('[div:',div,']',2**(div), '<= resolution:',resolution,'<=',2**(div+1),firstNum)
            outH = int(2**(div))
            outW = int(2**(div))
            for i in range(outH):
                for k in range(outW):
                    if div == 7 :
                        outImage[i][k] = math.ceil((inImage[i+i][k+k]+inImage[i+i+1][k+k]+inImage[i+i][k+k+1]+inImage[i+i+1][k+k+1])/4)
                    else :
                        outImage[i][k] = math.ceil((outImage[i+i][k+k]+outImage[i+i+1][k+k]+outImage[i+i][k+k+1]+outImage[i+i+1][k+k+1])/4)
        else :
            print('[div:', div, ']',2**(div))
    displayImage()

### 전역 변수부
window, canvas, paper = None, None, None
inImage, outImage = [], []
inH, inW, outH, outW = [0] * 4
filename = ''



### 메인 코드부
if __name__ == '__main__' :
    window = Tk()
    window.title('그레이 영상처리 Ver 0.01')
    window.geometry('512x512')
    window.resizable(height=False, width=False)



    ### 메뉴 만들기 ###

    mainMenu = Menu(window)
    window.configure(menu=mainMenu)

    #파일 메뉴
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="열기(Open)", command=openFile)
    fileMenu.add_command(label="저장(Save)", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="닫기(Close)")

    #화소점처리 메뉴
    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)

    pixelMenu.add_command(label="원본이미지",    command=pixelMenu_1)
    pixelMenu.add_command(label="밝게",         command=pixelMenu_2)
    pixelMenu.add_command(label="어둡게",       command=pixelMenu_3)
    pixelMenu.add_command(label="이진화",       command=pixelMenu_4)
    pixelMenu.add_command(label="이진화(평균값)",command=pixelMenu_5)
    pixelMenu.add_command(label="이진화(중위수)",command=pixelMenu_6)
    pixelMenu.add_command(label="영상반전",     command=pixelMenu_7)
    pixelMenu.add_command(label="포스터라이징",  command=pixelMenu_8)
    pixelMenu.add_command(label="감마",         command=pixelMenu_9)
    pixelMenu.add_command(label="파라볼라(캡)",  command=pixelMenu_10)
    pixelMenu.add_command(label="파라볼라(컵)",  command=pixelMenu_11)

    # 기하학처리 메뉴
    # 미션2 : 기하학 처리 --> 미러링(좌우)/미러링(상하)/이동/90도회전/회전/확대/축소
    geometryMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="기하학 처리", menu=geometryMenu)

    geometryMenu.add_command(label="미러링(좌우)",command=geometryMenu_1)
    geometryMenu.add_command(label="미러링(상하)",command=geometryMenu_2)
    geometryMenu.add_command(label="이동",       command=geometryMenu_3)
    geometryMenu.add_command(label="90도회전",    command=geometryMenu_4)
    geometryMenu.add_command(label="45도회전",    command=geometryMenu_5)
    geometryMenu.add_command(label="확대",       command=geometryMenu_6)
    geometryMenu.add_command(label="축소",       command=geometryMenu_7)

    # (미션3) : 화소영역 처리 --> 블러링/샤프팅/엠보싱/경계추출.......
    pixelAreaMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소영역 처리", menu=pixelAreaMenu)

    pixelAreaMenu.add_command(label="블러링", command=pixelAreaMenu_1)
    pixelAreaMenu.add_command(label="샤프팅", command=pixelAreaMenu_2)
    pixelAreaMenu.add_command(label="엠보싱", command=pixelAreaMenu_3)
    pixelAreaMenu.add_command(label="경계추출", command=pixelAreaMenu_4)


    # (미션4) : 히스토그램 처리 --> 히스토그램 평활화 .....
    HistogramMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="히스토그램 처리", menu=HistogramMenu)

    HistogramMenu.add_command(label="히스토그램 평활화", command=HistogramMenu_1)

    # TEST
    test = Menu(mainMenu)
    mainMenu.add_cascade(label="이미지 축소 테스트", menu=test)

    test.add_command(label="이미지 축소 테스트", command=test1)

    ######################

    window.mainloop()