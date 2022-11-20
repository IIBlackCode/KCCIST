### 함수 선언부

def malloc(h, w) :

    retImage = []
    tmp = []
    for _ in range(h):
        tmp = []
        for _ in range(w):
            tmp.append(0)
        retImage.append(tmp)
    return  retImage

def openImage() :

    global image, height, width, filename
    rfp = open(filename, 'rb')
    for i in range(height):
        for k in range(width):
            image[i][k] = int(ord(rfp.read(1)))
    rfp.close()

def displayImage() :

    global image, height, width, filename
    print()
    for i in range(10):
        for k in range(10):
            print("%3d" % (image[i][k]), end=' ')
        print()

### 영상처리 함수 모음 ###

def addImage() :
    global image, height, width, filename
    value = int(input('밝게할 값-->'))
    for i in range(height) :
        for k in range(width) :
            image[i][k] += value
    displayImage()

# ** 4일차 (빅데이터 수집 시스템 개발) **
# 복습 퀴즈 --> Windows 환경에서 작업

 # 이미지를 GUI로 선택하고, 다양한 해상도(1024x1024, 512x512, 256x256 ...)
 #         아무거나 선택해도 처리되도록 한다. (카페 참조)
# (1) 이미지 색상해상도 256가지에서 128, 64, 32 가지로 변경한다.
#     예) 0,1,2,.....255 --> 0, 2, 4, 8 .... 254
def quize_01() :
    global image, height, width, filename
    print('(1) 이미지 색상해상도 256가지에서 128, 64, 32 가지로 변경한다.')
    resolution = int(input('Enter the resolution to be printed :'))
    for div in range(7,2,-1) :
        if (not(2**(div) < resolution))  :
            firstNum = 2**(div+1);
            # print('[div:',div,']',2**(div), '<= resolution:',resolution,'<=',2**(div+1),firstNum)
            outH = int(2**(div))
            outW = int(2**(div))
            for i in range(outH):
                for k in range(outW):
                    if div == 7 :
                        image[i][k] = math.ceil((image[i+i][k+k]+image[i+i+1][k+k]+image[i+i][k+k+1]+image[i+i+1][k+k+1])/4)
                    else :
                        image[i][k] = math.ceil((image[i+i][k+k]+image[i+i+1][k+k]+image[i+i][k+k+1]+image[i+i+1][k+k+1])/4)
        else :
            print('[div:', div, ']',2**(div))
    displayImage()

# (2) 이미지를 입력한 숫자 (예: 4, 8, 16, 32)로 포스터라이징 한다.
#     --> 4가지 색상, 8가지 색상, 16가지 색상....
def quize_02() :
    global image, height, width, filename
    print('(2) 이미지를 입력한 숫자 (예: 4, 8, 16, 32)로 포스터라이징 한다.')
    pass

# (3) 이미지를 입력한 특정 영역만을 255로 변경한다.
#     예) 50, 100 을 입력하면 50~100 영역만 255로 변경하고, 나머지는 그대로
def quize_03() :
    global image, height, width, filename
    print('(3) 이미지를 입력한 특정 영역만을 255로 변경한다.')
    pass

# (4) 이미지를 2배 축소시키되, 평균값에 의해서 축소한다.
#      --> 축소되는 4점의 평균값
def quize_04() :
    global image, height, width, filename
    print('(4) 이미지를 2배 축소시키되, 평균값에 의해서 축소한다.')
    pass

# (5)<심화> 감마 변환을 구현한다.
def quize_05() :
    global image, height, width, filename
    print('(5)<심화> 감마 변환을 구현한다.')
    pass

# (6)<심화> 파라볼라 변환을 구현한다.
def quize_06() :
    global image, height, width, filename
    print('(6)<심화> 파라볼라 변환을 구현한다.')
    pass

# 제출 : [복습퀴즈 9/22] 홍길동

### 전역 변수부
image=[] ; height, width=0,0;
filename = 'C:/images/Etc_Raw(squre)/512/'

## 메인 코드부
if  __name__ == '__main__' :
    ## 파일 선택
    # tmpFname = input('파일명-->')
    # filename += tmpFname + ".raw"

    from tkinter.filedialog  import *
    filename = askopenfilename(parent=None,
        filetypes = (('RAW File','*.raw'), ('All File', '*.*')))

    ## 파일의 높이x폭
    #height = width = 512

    import math
    fsize = os.path.getsize(filename)
    height = width = int(math.sqrt(fsize))

    ## 메모리 할당
    image = malloc(height,width)

    ## 파일 --> 메모리 로딩
    openImage()

    ## 원본 이미지 보기
    displayImage()

    ### 메뉴 선택하기 ###

    menu = -1
    while menu!=0 :
        print("(1) 이미지 색상해상도 256가지에서 128, 64, 32 가지로 변경" )
        print("(2) 이미지를 입력한 숫자 (예: 4, 8, 16, 32)로 포스터라이징")
        print("(3) 이미지를 입력한 특정 영역만을 255로 변경")
        print("(4) 이미지를 2배 축소시키되, 평균값에 의해서 축소한다.")
        print("(5)<심화> 감마 변환을 구현")
        print("(6)<심화> 파라볼라 변환을 구현")
        menu = int(input('입력-->'))
        if menu==1 :
            quize_01()
        elif menu==2 :
            quize_02()
        elif menu==3 :
            quize_03()
        elif menu==4 :
            quize_05()
        elif menu==5 :
            quize_05()
        elif menu==6 :
            quize_06()

        elif menu ==0 :
            print('프로그램 끝!')
            break