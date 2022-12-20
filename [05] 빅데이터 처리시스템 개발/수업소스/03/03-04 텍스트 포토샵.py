#함수 선언부
#기본 기능은 소스가 변하지 않는다.
def malloc(h, w) :
    # 메모리할당
    retImage = [];
    tmp = [];
    for _ in range(h):
        tmp = []
        for _ in range(w):
            tmp.append(0);
        retImage.append(tmp);
    return  retImage;

def openImage() :
    global image, height, width, filename # 전역변수로 선언
    rfp = open(filename, 'rb')
    for i in range(height):
        for k in range(width):
            image[i][k] = int(ord(rfp.read(1)))
    rfp.close()

def displayImage() :
    global image, height, width, filename   # 전역변수로 선언
    print()
    for i in range(10):
        for k in range(10):
            print("%3d" % (image[i][k]), end=' ')
        print()

#영상처리 함수 모음(계속 소스가 바뀐다)
def addImage() :
    global image, width, height, filename;  # 전역변수로 선언
    value = int(input('밝게할 값 -->'));
    for i in range(height) :
        for k in range(width) :

            if image[i][k]+value > 255 :
                image[i][k] = 255;
            else :
                image[i][k] += value;
    displayImage();


def minusImage():
    global image, width, height, filename;  # 전역변수로 선언
    value = int(input('밝게할 값 -->'));
    for i in range(height):
        for k in range(width):

            if image[i][k]-value < 0:
                image[i][k] = 0;
            else:
                image[i][k] -= value;
    displayImage();

#전역 변수부
image=[] ; height,width = 0,0;
filename = 'C:/images/Etc_Raw(squre)/512/'


#메인 코드부
if __name__ == '__main__' :
    tempFname = input('파일명 -->');
    filename += tempFname +".raw";

    #파일의 높이 X 폭
    height = width = 512;

    #메모리할당
    image = malloc(height, width);

    #파일 -->메모리 로딩
    openImage()
    
    #원본이미지 보기
    displayImage()
    
    #메뉴 선택하기
    menu = -1;
    while menu != 0 :
        print("영상처리 : (1)밝게 (2)어둡게 (0)종료 -->")
        menu = int(input('입력 -->'))
        if menu == 1 :
            addImage()
        elif menu == 2 :
            minusImage()
        elif menu == 0 :
            print('프로그램 종료');
            break;
    pass;

## 3일차 미션