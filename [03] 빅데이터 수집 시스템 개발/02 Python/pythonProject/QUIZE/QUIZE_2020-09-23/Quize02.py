from tkinter.filedialog import *
from tkinter.simpledialog import *
import math


##  함수 선언부
def malloc(h, w, value=0):
    retMemory = [[value for _ in range(w)] for _ in range(h)]
    return retMemory


def openFile():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    ## 파일 선택하기
    filename = askopenfilename(parent=window,
                               filetypes=(('RAW 파일', '*.raw'), ('All File', '*.*')))

    ## (중요!) 입력이미지의 높이와 폭 알아내기
    fsize = os.path.getsize(filename)
    inH = inW = int(math.sqrt(fsize))

    ## 입력이미지용 메모리 할당
    inImage = malloc(inH, inW)

    ## 파일 --> 메모리 로딩
    with open(filename, 'rb') as fp:
        for i in range(inH):
            for k in range(inW):
                inImage[i][k] = int(ord(fp.read(1)))
    equalImage()


import struct


def saveFile():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename

    if filename == '' or filename == None:
        return
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.raw',
                           filetypes=(('RAW 파일', '*.raw'), ('All File', '*.*')))

    for i in range(outH):
        for k in range(outW):
            saveFp.write(struct.pack('B', outImage[i][k]))
    saveFp.close()

    # 저장 후 정보 확인
    status.configure(text='저장파일 : ' + saveFp.name);


def displayImage():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    # canvas의 크기에 따라 윈도우의 크기 변환 > 없어도 자동적으로 변환된다.
    window.geometry(str(outH) + 'x' + str(outW))
    if canvas != None:
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
    rgbString = ""
    for i in range(outH):
        tmpString = ""  # 각 줄
        for k in range(outW):
            r = g = b = outImage[i][k]
            tmpString += "#%02x%02x%02x " % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)
    canvas.pack()

    # status 상태정보 불러오기
    status.configure(text='이미지정보 : ' + str(outW) + 'x' + str(outW) + ' ' + filename);


######  영상처리 함수 ######
def equalImage():  # 동일영상 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]
    ########################
    displayImage()


def addImage():  # 밝게하기 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    value = askinteger("밝게할 값", "값-->", minvalue=1, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] + value > 255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = inImage[i][k] + value
    ########################
    displayImage()


def gammaImage():  # 감마연산 알고리즘
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


def paraCapImage():  # 감마연산 알고리즘
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


def paraCupImage():  # 감마연산 알고리즘
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


def bw1Image():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 이진화 기본 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2
    for i in range(inH):
        for k in range(inW):
            v = 255 - 255.0 * ((inImage[i][k] / 128.0 - 1.0) ** 2);
            if inImage[i][k] < 127:
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255
    ########################
    displayImage()


def bw2Image():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 이진화(평균) 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2
    sum = 0;
    for i in range(inH):
        for k in range(inW):
            sum += inImage[i][k];
    avg = sum / (inH * inW)

    for i in range(inH):
        for k in range(inW):
            v = 255 - 255.0 * ((inImage[i][k] / 128.0 - 1.0) ** 2);
            if inImage[i][k] < avg:
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255
    displayImage()


def bw3Image():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 이진화(중위수) 알고리즘 ###
    ### Out = 255.0*(inImage/128.0-1.0) ** 2
    mid = 0;
    tmpArray = [];
    for i in range(inH):
        for k in range(inW):
            tmpArray.append(inImage[i][k])

    # 배열 정렬
    tmpArray.sort();

    mid = tmpArray[int((inH * inW) / 2)];

    for i in range(inH):
        for k in range(inW):
            v = 255 - 255.0 * ((inImage[i][k] / 128.0 - 1.0) ** 2);
            if inImage[i][k] < mid:
                outImage[i][k] = 0
            else:
                outImage[i][k] = 255
    displayImage()


def point2Image():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    p1 = askinteger("", "Value : ")
    p2 = askinteger("", "Value : ")

    if p1 > p2:
        p1, p2 = p2, p1
        # tmp = p1;
        # p1 = p2;
        # p2 = tmp;

    for i in range(inH):
        for k in range(inW):
            # if p1< inImage[i][k] and inImage[i]][k]<p2 :
            if p1 < inImage[i][k] < p2:
                outImage[i][k] = 255
            else:
                outImage[i][k] = inImage[i][k];
    ########################
    displayImage()


def moveImage():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    dx = askinteger("", "x Value : ")
    dy = askinteger("", "y Value : ")

    for i in range(inH):
        for k in range(inW):
            if 0 <= i + dx < outH and 0 <= k + dy < outW:
                outImage[i + dx][k + dy] = inImage[i][k]

    ########################
    displayImage()


def zoomoutImage():  # 영상축소 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("축소", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH / scale)
    outW = int(inW / scale)

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###

    for i in range(inH):
        for k in range(inW):
            outImage[int(i / scale)][int(k / scale)] = inImage[i][k]
    ########################
    displayImage()


def zoomout2Image():  # 영상축소(백워딩) 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("축소", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH / scale)
    outW = int(inW / scale)

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(outH):
        for k in range(outW):
            print('[', i, k, ']:', (i * scale), (k * scale))
            outImage[(i)][(k)] = inImage[int(i * scale)][int(k * scale)]
    ########################
    displayImage()


def zoominImage():  # 영상확대 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("확대", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH * scale)
    outW = int(inW * scale)

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###

    for i in range(inH):
        for k in range(inW):
            outImage[int(i * scale)][int(k * scale)] = inImage[int(i)][int(k)]
    ########################
    displayImage()


def zoomin2Image():  # 영상확대(백워딩) 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    scale = askinteger("확대", "배율 : ")  # 짝수입력을 전제로 한다.
    outH = int(inH * scale)
    outW = int(inW * scale)

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(outH):
        for k in range(outW):
            print('[', i, k, ']:', (i / scale), (k / scale))
            outImage[(i)][(k)] = inImage[int(i / scale)][int(k / scale)]
    ########################
    displayImage()
def zoomin3Image(): ## 영상확대(양선형)
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    scale = askinteger("확대", "배율 : ")
    outH = inH * scale
    outW = inW * scale

    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    for i in range(inH):
        for k in range(inW):
            outImage[i * scale][k * scale] = inImage[i][k]

    ## 직선, 대각선 보간##
    for i in range(0, outH - scale, scale):
        for k in range(0, outW - scale, scale):
            for l in range(1, scale):
                outImage[i + l][k] = outImage[i][k] + int((outImage[i + scale][k] - outImage[i][k]) * l / scale)

            for l in range(1, scale):
                outImage[i][k + l] = outImage[i][k] + int((outImage[i][k + scale] - outImage[i][k]) * l / scale)

            for l in range(1, scale):
                outImage[i + l][k + l] = outImage[i][k] + int(
                    (outImage[i + scale][k + scale] - outImage[i][k]) * l / scale)

            for l in range(1, scale):
                outImage[i + scale - l][k + l] = outImage[i + scale][k] + int(
                    (outImage[i][k + scale] - outImage[i + scale][k]) * l / scale)
    displayImage()

####    화소영역 처리 알고리즘
def embossImage():  # 엠보싱 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW

    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    ### 중요! 마스크
    mSize = 3
    mask = [[-1, 0, 0],
            [0, 0, 0],
            [0, 0, 1]]
    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage > 임시 input
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH + 1):
        for k in range(1, inW + 1):
            # 각 점을 처리
            S = 0.0
            for m in range(mSize):
                for n in range(mSize):
                    S += mask[m][n] * tmpInImage[m + i - 1][n + k - 1]
            tmpOutImage[i - 1][k - 1] = S
    ##  마무리 .. 마스크에 따라서 127 더할지 결정
    for i in range(outH):
        for k in range(outW):
            tmpOutImage[i][k] += 127.0
        ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])

    ########################
    displayImage()

def blurrImage():  # 블러링 효과
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)
    ### 진짜 영상처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    mask = [[1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]]

    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage --> 임시input
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])
    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH + 1):
        for k in range(1, inW + 1):
            # 각 점을 처리
            S = 0.0
            for m in range(mSize):
                for n in range(mSize):
                    S += mask[m][n] * tmpInImage[m + i - 1][n + k - 1]
            tmpOutImage[i - 1][k - 1] = S

    ## 마무리.. 마스크에 따라서 127 더할지 결정
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tmpOutImage[i][k] += 127.0
    ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    ########################
    displayImage()

def sharpImage():  # 샤프닝 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 진짜 영상처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    mask = [[ 0.0, -1.0,  0.0],
            [-1.0,  5.0, -1.0],
            [ 0.0, -1.0,  0.0]]

    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage --> 임시input
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])
    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH + 1):
        for k in range(1, inW + 1):
            # 각 점을 처리
            S = 0.0
            for m in range(mSize):
                for n in range(mSize):
                    S += mask[m][n] * tmpInImage[m + i - 1][n + k - 1]
            tmpOutImage[i - 1][k - 1] = S

    ## 마무리.. 마스크에 따라서 127 더할지 결정
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tmpOutImage[i][k] += 127.0
    ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    ########################
    displayImage()

def sharp2Image():  # 고주파 통과 필터를 이용한 샤프닝 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)
    ### 고주파 통과 필터를 이용한 샤프닝 처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    #필터 계수의 합 0
    #고주파 필터의 계수
    mask = [[-1 / 9.0, -1 / 9.0, -1 / 9.0],
            [-1 / 9.0,  8 / 9.0, -1 / 9.0],
            [-1 / 9.0, -1 / 9.0, -1 / 9.0]]

    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage --> 임시input
    #한치수 큰 입력받을 tmpInImage 배열에 inImage의 값 대입
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH + 1):
        for k in range(1, inW + 1):
            # 각 점을 처리
            S = 0.0
            for m in range(mSize):
                for n in range(mSize):
                    # print('[',i,k,'] tmpInImage[m+i-1:',m+i-1,' n+k-1:',n+k-1,']:',tmpInImage[m + i - 1][n + k - 1],' \tmask[',m,'][',n,']',mask[m][n],'=',S)
                    S += mask[m][n] * tmpInImage[m + i - 1][n + k - 1]
            tmpOutImage[i - 1][k - 1] = S

    ## 마무리.. 마스크에 따라서 127 더할지 결정
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tmpOutImage[i][k] += 127.0
    ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    ########################
    displayImage()

def sharp3Image():  # Unsharp Masking 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)
    ### Unsharp Masking 처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    #필터 계수의 합 0
    #저주파 필터의 계수
    mask = [[1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]]

    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage --> 임시input
    #한치수 큰 입력받을 tmpInImage 배열에 inImage의 값 대입
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])

    #Unsharp Masking = (원 영상) – (저주파 통과 필터링 결과 영상)
    #High-Boost = α(원 영상) – (저주파 통과 필터링 결과 영상)
    # resolution = askinteger("축소할 값", "Enter the resolution to be printed :", minvalue=32, maxvalue=128);
    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH + 1):
        for k in range(1, inW + 1):
            # 각 점을 처리
            S = 0.0
            for m in range(mSize):
                for n in range(mSize):
                    # print('[',i,k,'] tmpInImage[m+i-1:',m+i-1,' n+k-1:',n+k-1,']:',tmpInImage[m + i - 1][n + k - 1],' \tmask[',m,'][',n,']',mask[m][n],'=',S)
                    S += mask[m][n] * tmpInImage[m + i - 1][n + k - 1]
            tmpOutImage[i - 1][k - 1] = inImage[i-1][k-1] - S

    ## 마무리.. 마스크에 따라서 127 더할지 결정
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tmpOutImage[i][k] += 127.0
    ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    ########################
    displayImage()

def sharp4Image():  # High-Boost 알고리즘
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)
    ### Unsharp Masking 처리 알고리즘 ###
    # (중요!) 마스크
    mSize = 3
    #필터 계수의 합 0
    #저주파 필터의 계수
    mask = [[1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0],
            [1 / 9.0, 1 / 9.0, 1 / 9.0]]

    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage --> 임시input
    #한치수 큰 입력받을 tmpInImage 배열에 inImage의 값 대입
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])

    #Unsharp Masking = (원 영상) – (저주파 통과 필터링 결과 영상)
    #High-Boost = α(원 영상) – (저주파 통과 필터링 결과 영상)
    α = 0.1*askinteger("축소할 값", "Enter the resolution to be printed :", minvalue=1, maxvalue=30);
    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH + 1):
        for k in range(1, inW + 1):
            # 각 점을 처리
            S = 0.0
            for m in range(mSize):
                for n in range(mSize):
                    # print('[',i,k,'] tmpInImage[m+i-1:',m+i-1,' n+k-1:',n+k-1,']:',tmpInImage[m + i - 1][n + k - 1],' \tmask[',m,'][',n,']',mask[m][n],'=',S)
                    S += mask[m][n] * tmpInImage[m + i - 1][n + k - 1]
            tmpOutImage[i - 1][k - 1] = α*(inImage[i-1][k-1]) - S

    ## 마무리.. 마스크에 따라서 127 더할지 결정
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tmpOutImage[i][k] += 127.0
    ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    ########################
    displayImage()

def OnHomogenOperator() :   #유사 연산자
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return
    ## (중요!) 출력이미지의 높이, 폭을 결정 ---> 알고리즘에 의존
    outH = inH;
    outW = inW
    ## 출력이미지 메모리 할당
    outImage = malloc(outH, outW)

    ### 유사 연산자 처리 알고리즘 ###
    tmpInImage = malloc(inH + 2, inW + 2, 127)
    tmpOutImage = malloc(outH, outW)
    # inImage --> 임시input
    # 한치수 큰 입력받을 tmpInImage 배열에 inImage의 값 대입
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = float(inImage[i][k])

    # 회선 연산 : 마스크로 긁어가면서 처리하기
    for i in range(1, inH):
        for k in range(1, inW):
            temp=[]
            for m in range(-1,2):
                for n in range(-1,2):
                    # 3x3행렬 내에서 max값을 구하는 알고리즘
                    #S.append(abs(tempIn[i][j] - tempIn[i-1+m][j-1+n]))
                    if tmpInImage[i][k]-tmpInImage[m][n] < 0 :
                        temp.append((tmpInImage[i][k] - tmpInImage[m+i][n+k])*(-1))
                        # print('[',i,k,']', tmpInImage[i][k], '\t', '[',m+i,n+k,']', tmpInImage[m+i][n+k], '\t')

                    else :
                        temp.append(tmpInImage[i][k] - tmpInImage[m+i][n+k])
                        # print('[',i,k,']', tmpInImage[i][k], '\t', '[',m+i,n+k,']', tmpInImage[m+i][n+k], '\t')

            # temp.sort()
            # outImage[i][k] =temp[8];
            tmpOutImage[i-1][k-1] = max(temp)
            # print(i,k,' max(temp):',max(temp),tmpOutImage[i-1][k-1])


    ## 마무리.. 마스크에 따라서 127 더할지 결정
    # for i in range(outH) :
    #     for k in range(outW) :
    #         tmpOutImage[i][k] += 127.0
    ## 임시Output --> outImage .... 오버플로 체크
    for i in range(outH):
        for k in range(outW):
            if tmpOutImage[i][k] > 255:
                outImage[i][k] = 255
            elif tmpOutImage[i][k] < 0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = int(tmpOutImage[i][k])
    ########################
    displayImage()

# 차 연산자
def diffOperImage():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    outH = inH;    outW = inW
    outImage = malloc(outH, outW)

    msize = 3
    mask = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    tempIn = malloc(inH + 2, inW + 2, 128)
    tempOut = malloc(outH, outW)

    # tempIn --> tempOut
    for i in range(inH):
        for j in range(inW):
            tempIn[i+1][j+1] = float(inImage[i][j])

    # 회선 연산: 마스크로 긁어가며 처리
    for i in range(1, inH + 1):
        for j in range(1, inW + 1):
            S = []
            # 차 연산자 계산
            for m in range(int(msize/2)):
                for n in range(msize):
                    S.append(abs(tempIn[i-1+m][j-1+n] -
                                 tempIn[i-2+msize-m][j-2+msize-n]))
            m = int(msize/2)+1
            for n in range(int(msize/2)):
                S.append(abs(tempIn[i-1+m][j-1+n] -
                             tempIn[i-2+msize-m][j-2+msize-n]))
            tempOut[i-1][j-1] = max(S)

    # 오버/언더플로 체크
    for i in range(outH):
        for j in range(outW):
            if tempOut[i][j] > 255:
                outImage[i][j] = 255
            elif tempOut[i][j] < 0:
                outImage[i][j] = 0
            else:
                outImage[i][j] = int(tempOut[i][j])
    displayImage()

def logImage():
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    if filename == '' or filename == None:
        return

    outH = inH;    outW = inW
    outImage = malloc(outH, outW)

    msize = 5
    nsize = int(msize/2)
    mask = [[ 0,  0, -1,  0,  0],
            [ 0, -1, -2, -1,  0],
            [-1, -2, 16, -2, -1],
            [ 0, -1, -2, -1,  0],
            [ 0,  0, -1,  0,  0]]
    for i in range(msize):
        temp = []
        for j in range(msize):
            temp.append(1/(msize**2))
        mask.append(temp)
    # print(mask)

    tempIn = malloc(inH+2*nsize, inW+2*nsize, 128)
    # 가장자리에 추가해야 할 픽셀이 msize의 절반이므로
    # 미리 계산한 nsize의 2배만큼을 더 추가한다
    tempOut = malloc(outH, outW)

    # tempIn --> tempOut
    for i in range(inH):
        for j in range(inW):
            tempIn[i+nsize][j+nsize] = float(inImage[i][j])

    # 회선 연산: 마스크로 긁어가며 처리
    for i in range(1, inH + 1):
        for j in range(1, inW + 1):
            S = 0.0
            for m in range(msize):
                for n in range(msize):
                    S += mask[m][n] * tempIn[m+i-nsize][n+j-nsize]
            tempOut[i-nsize][j-nsize] = S

    # 오버/언더플로 체크
    for i in range(outH):
        for j in range(outW):
            if tempOut[i][j] > 255:
                outImage[i][j] = 255
            elif tempOut[i][j] < 0:
                outImage[i][j] = 0
            else:
                outImage[i][j] = int(tempOut[i][j])
    displayImage()


##  전역 변수부
from tkinter import Tk

window, canvas, paper = None, None, None
inImage, outImage = [], []
inH, inW, outH, outW = [0] * 4
filename = ''

##  메인 코드부
if __name__ == '__main__':
    window = Tk()
    window.title('그레이 영상처리 Ver 0.02')
    window.geometry('512x512')
    window.resizable(height=False, width=False)

    ##Loading 상태바 구현
    status = Label(window, text='이미지정보 : ', bd=1, relief=SUNKEN, anchor=W);
    status.pack(side=BOTTOM, fill=X);

    ### 메뉴 만들기 ###

    mainMenu = Menu(window)
    window.configure(menu=mainMenu)
    fileMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="열기(Open)", command=openFile)
    fileMenu.add_command(label="저장(Save)", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="닫기(Close)")

    pixelMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=pixelMenu)
    pixelMenu.add_command(label="동일영상", command=equalImage)
    pixelMenu.add_command(label="밝게하기", command=addImage)
    pixelMenu.add_command(label="감마연산", command=gammaImage)
    pixelMenu.add_command(label="파라볼라(캡)", command=paraCapImage)
    pixelMenu.add_command(label="파라볼라(캡)", command=paraCupImage)
    pixelMenu.add_command(label="이진화(기본)", command=bw1Image)
    pixelMenu.add_command(label="이진화(평균)", command=bw2Image)
    pixelMenu.add_command(label="이진화(중위수)", command=bw3Image)
    pixelMenu.add_command(label="범위강조 변환", command=point2Image)

    geometryMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소점 처리", menu=geometryMenu)
    geometryMenu.add_command(label="영상 이동", command=moveImage)
    geometryMenu.add_command(label="영상 축소", command=zoomoutImage)
    geometryMenu.add_command(label="영상 축소(백워딩)", command=zoomout2Image)
    geometryMenu.add_command(label="영상 확대", command=zoominImage)
    geometryMenu.add_command(label="영상 확대(백워딩)", command=zoomin2Image)
    geometryMenu.add_command(label="영상 확대(양선형)", command=zoomin3Image)

    areaMenu = Menu(mainMenu)
    mainMenu.add_cascade(label="화소영역 처리", menu=areaMenu)
    areaMenu.add_command(label="엠보싱", command=embossImage)
    areaMenu.add_command(label="블러링", command=blurrImage)
    areaMenu.add_command(label="샤프닝", command=sharpImage)
    areaMenu.add_command(label="고주파 필터 통과 샤프닝", command=sharp2Image)
    # areaMenu.add_command(label="Unsharp Masking", command=sharp3Image)
    areaMenu.add_command(label="High-Boost", command=sharp4Image)
    areaMenu.add_command(label="유사 연산자", command=OnHomogenOperator)
    # areaMenu.add_command(label="유사 연산자", command=OnHomogenOperator2)
    areaMenu.add_command(label="차연산자", command=diffOperImage)

    ######################

    window.mainloop()