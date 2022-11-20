#10시까지 카페에 제출 : [복습퀴즈9/24]김민서

#복습퀴즈 : 그레이 영상처리 Ver 0.1 완성하기

# 새로 파이썬 코드 GrayPhotoShop.py를 작성하고 5일차 미션까지 완성한 영상처리를 다시 만든다.



#(1) 코드의 내용을 복사해서 사용해도 좋으나, 전체구성/전역변수/함수명 등은 직접 입력한다.

#(2: 심화) [파일] 옆에 [편집] 메뉴를 추가해서, [실행취소] 기능을 추가해 본다.
#   즉, 바로 직전의 화면으로 돌아가도록 한다.

# (3: 심화) [편집] 메뉴의 [다시실행] 기능을 추가해서 취소한 영상처리를 다시 실행하도록 한다.
import struct
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter import Tk
import math

#(1) 코드의 내용을 복사해서 사용해도 좋으나, 전체구성/전역변수/함수명 등은 직접 입력한다.
##  함수 선언부, 함수 이름은 뒤에 Gray를 붙인다. 예) equalGray, embossGray


# =======================================    **   <<1>> 공통 함수    **   =======================================
# [1].공통 함수(소스수정X) : 메모리 할당 함수
def createImageArray_GrayVer(hight, width, value=0):
    print('Run createImageArray_GrayVer() Method ...', hight, width)
    #메모리 할당
    allocationMemory = [[value for _ in range(hight)] for _ in range(width)]
    return allocationMemory

# [1].공통 함수(소스수정X) : 이미지 출력 함수
def displayImage_GrayVer():
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth,imagePath
    print('Run displayImage_GrayVer() Method ...',enterImage[0][0],printImageHight,printImageHight)
    #1. 이미지를 담을 윈도우창 생성 : canvas의 크기에 따라 윈도우의 크기 변환 > 없어도 자동적으로 변환된다.
    imageWindow.geometry(str(printImageHight) + 'x' + str(printImageWidth))
    if imageCanvas != None:
        imageCanvas.destroy()

    #2. 윈도우창 위에 그림그릴 Canvas 생성
    imageCanvas = Canvas(imageWindow, height=printImageHight, width=printImageWidth)

    #3. Canvas위에 그림을 찍어줄 imagePaper 생성
    imagePaper = PhotoImage(height=printImageHight, width=printImageWidth)

    #4. 캔버스위에 생성한 imagePaper 연결시킨다.
    imageCanvas.create_image((printImageHight / 2, printImageWidth / 2), image=imagePaper, state='normal')

    #5. 이미지 픽셀값을 읽어들여 tmpString에 저장 후 imagePaper tmpString값을 붙인다. 즉, imagePaper 이미지를 그림
    rgbString = ""
    for i in range(printImageHight):
        tmpString = ""  # 각 줄
        for k in range(printImageWidth):
            r = g = b = printImage[i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    imagePaper.put(rgbString)

    #6. Canvas를 pack해준다.
    imageCanvas.pack()

    # status 상태정보 불러오기
    imageStatusInfoBar.configure(text='이미지정보 : ' + str(printImageHight) + 'x' + str(printImageWidth) + ' ' + imagePath);
    ##  The end of Method

# [1].공통 함수(소스수정X) : (1)파일 > 1.이미지파일 열기
def openImage_GrayVer() :
    print('Run openImage_GrayVer() Method ...')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    ## 이미지 경로 저장
    imagePath = askopenfilename(parent=imageWindow,filetypes=(('RAW 파일', '*.raw'), ('All File', '*.*')))
    print(imagePath)

    ## 이미지 경로를 읽어 파일 사이즈로 높이와 폭 저장
    fsize = os.path.getsize(imagePath)
    enterImageHight = enterImageWidth = int(math.sqrt(fsize))

    ## 입력이미지 메모리 할당
    enterImage = createImageArray_GrayVer(enterImageHight, enterImageWidth)

    ## 파일경로를 통해 입력 이미지 생성 : 메모리 로딩
    with open(imagePath, 'rb') as fp:
        for i in range(enterImageHight):
            for k in range(enterImageWidth):
                enterImage[i][k] = int(ord(fp.read(1)))
    createSameImage_GrayVer()
    ##  The end of Method
    
# [1].공통 함수(소스수정X) : (1)파일 > 1.이미지파일 저장
def saveImage_GrayVer() :
    print('Run saveImage_GrayVer() Method ...')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    if imagePath == '' or imagePath == None :
        return
    #저장경로 불러오기
    saveImagePath = asksaveasfile(parent=imageWindow, mode='wb', defaultextension='*.raw',
                           filetypes=(('RAW 파일', '*.raw'), ('All File', '*.*')))
    #저장경로에 이미지 저장
    for i in range(printImageHight) :
        for k in range(printImageWidth) :
            saveImagePath.write(struct.pack('B', printImage[i][k]))
    saveImagePath.close()

    #저장 후 하단에 상태정보 출력
    imageStatusInfoBar.configure(text='저장파일 : ' + saveImagePath.name);
    ##  The end of Method
    
# =======================================    **   <<2>> 영상처리 함수    **   =======================================
# =======================================    **   [2] 화소점 처리    **   =======================================
# [2].화소점 처리 : (1)동일 이미지
def createSameImage_GrayVer():
    print('[2].화소점 처리 : (1)동일 이미지')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth,imagePath
    if imagePath == '' or imagePath == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    printImageHight = enterImageHight;
    printImageWidth = enterImageWidth;

    ## 출력이미지 메모리 할당
    printImage = createImageArray_GrayVer(printImageHight, printImageWidth)

    ## 이미지 출력 ###
    for i in range(enterImageHight):
        for k in range(enterImageWidth):
            printImage[i][k] = enterImage[i][k]
    ## 이미지 출력 함수 호출
    displayImage_GrayVer()
    ##  The end of Method

# [2].화소점 처리 : (2)밝게하기
def pixelMenu2_GrayVer():
    print('[2].화소점 처리 : (2)밝게하기')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (3)감마연산
def pixelMenu3_GrayVer():
    print('[2].화소점 처리 : (3)감마연산')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (4)파라볼라(캡)
def pixelMenu4_GrayVer():
    print('[2].화소점 처리 : (4)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (5)파라볼라(컵)
def pixelMenu5_GrayVer():
    print('[2].화소점 처리 : (5)파라볼라(컵)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (6)이진화(기본)
def pixelMenu6_GrayVer():
    print('[2].화소점 처리 : (6)이진화(기본)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (7)이진화(평균)
def pixelMenu7_GrayVer():
    print('[2].화소점 처리 : (7)이진화(평균)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (8)이진화(중위수)
def pixelMenu8_GrayVer():
    print('[2].화소점 처리 : (8)이진화(중위수)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [2].화소점 처리 : (9)범위강조 변환
def pixelMenu9_GrayVer():
    print('[2].화소점 처리 : (9)범위강조 변환')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method

# =======================================    **   [2] 기하학 처리    **   =======================================
# [3].기하학 처리 : (1)파라볼라(캡)
def geometryMenu1_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [3].기하학 처리 : (2)영상 이동
def geometryMenu2_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [3].기하학 처리 : (3)영상 축소
def geometryMenu3_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [3].기하학 처리 : (4)영상 축소(백워딩)
def geometryMenu4_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [3].기하학 처리 : (5)영상 확대
def geometryMenu5_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [3].기하학 처리 : (6)영상 확대(백워딩)
def pixelMenu6_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method
# [3].기하학 처리 : (7)영상 확대(양선형)
def geometryMenu7_GrayVer():
    print('[3].기하학 처리 : (1)파라볼라(캡)')
    global imageWindow, imageCanvas, imagePaper
    global enterImage, printImage, enterImageHight, enterImageWidth, printImageHight, printImageWidth, imagePath
    pass
    ##  The end of Method

##  전역 변수부
imageWindow, imageCanvas, imagePaper = None, None, None
enterImage, printImage = [], []
enterImageHight, enterImageWidth, printImageHight, printImageWidth = [0] * 4
imagePath = ''

##  메인 코드부 *********************************************************************************
if __name__ == '__main__' :
    imageWindow = Tk()
    imageWindow.title('그레이 영상처리 Ver 0.1')
    imageWindow.geometry('512x512')
    imageWindow.resizable(height=False, width=False)

    ##상태바 구현
    imageStatusInfoBar = Label(imageWindow, text='이미지정보 : ', bd=1, relief=SUNKEN, anchor=W);
    imageStatusInfoBar.pack(side=BOTTOM, fill=X);

    #============================== << Start Menu >> ==============================
    #[1] 메인메뉴 생성
    createMainMenu = Menu(imageWindow)
    imageWindow.configure(menu=createMainMenu)
    
    #[2-1] 메인메뉴 > 1.파일 메뉴
    fileMenu_Main = Menu(createMainMenu)
    createMainMenu.add_cascade(label="파일", menu=fileMenu_Main)

    #[최하위 메뉴] 메인메뉴 > 1.파일 메뉴 > 열기, 저장, 구분선, 닫기 [기본함수]
    fileMenu_Main.add_command(label="열기(Open)", command=openImage_GrayVer)
    fileMenu_Main.add_command(label="저장(Save)", command=saveImage_GrayVer)
    fileMenu_Main.add_separator()
    fileMenu_Main.add_command(label="닫기(Close)")

    #[2-2] 메인메뉴 > 2.화소점 처리 메뉴
    pixelMenu = Menu(createMainMenu)
    createMainMenu.add_cascade(label="화소점 처리 메뉴", menu=pixelMenu)

    #[최하위 메뉴] 메인메뉴 > 2.화소점 처리 메뉴 > 열기, 저장, 구분선, 닫기 [영상처리함수]
    pixelMenu.add_command(label="(1)동일영상", command=createSameImage_GrayVer)
    # pixelMenu.add_command(label="(2)밝게하기", command=addImage)
    # pixelMenu.add_command(label="(3)감마연산", command=gammaImage)
    # pixelMenu.add_command(label="(4)파라볼라(캡)", command=paraCapImage)
    # pixelMenu.add_command(label="(5)파라볼라(컵)", command=paraCupImage)
    # pixelMenu.add_command(label="(6)이진화(기본)", command=bw1Image)
    # pixelMenu.add_command(label="(7)이진화(평균)", command=bw2Image)
    # pixelMenu.add_command(label="(8)이진화(중위수)", command=bw3Image)
    # pixelMenu.add_command(label="(9)범위강조 변환", command=point2Image)
    #
    # geometryMenu = Menu(mainMenu)
    # mainMenu.add_cascade(label="기하학 처리", menu=geometryMenu)
    # geometryMenu.add_command(label="영상 이동", command=moveImage)
    # geometryMenu.add_command(label="영상 축소", command=zoomoutImage)
    # geometryMenu.add_command(label="영상 축소(백워딩)", command=zoomout2Image)
    # geometryMenu.add_command(label="영상 확대", command=zoominImage)
    # geometryMenu.add_command(label="영상 확대(백워딩)", command=zoomin2Image)
    # geometryMenu.add_command(label="영상 확대(양선형)", command=zoomin2Image)
    #
    # areaMenu = Menu(mainMenu)
    # mainMenu.add_cascade(label="화소영역 처리", menu=areaMenu)
    # areaMenu.add_command(label="엠보싱", command=embossImage)
    # areaMenu.add_command(label="블러링", command=blurrImage)
    # areaMenu.add_command(label="샤프닝", command=sharpImage)
    # areaMenu.add_command(label="고주파 필터 통과 샤프닝", command=sharp2Image)
    # # areaMenu.add_command(label="Unsharp Masking", command=sharp3Image)
    # areaMenu.add_command(label="High-Boost", command=sharp4Image)
    # areaMenu.add_command(label="유사 연산자", command=OnHomogenOperator)
    # # areaMenu.add_command(label="차연산자", command=sharp4Image)
    #
    # histoMenu = Menu(mainMenu)
    # mainMenu.add_cascade(label="히스토그램 처리", menu=histoMenu)
    # histoMenu.add_command(label="히스토그램 스트래칭", command=stretchImage)
    # histoMenu.add_command(label="앤드 - 인 탐색", command=endInImage)
    # histoMenu.add_command(label="히스토그램 평활화", command=equalizedImage)
    # ============================== << End of Menu >> ==============================
    createMainMenu.mainloop()