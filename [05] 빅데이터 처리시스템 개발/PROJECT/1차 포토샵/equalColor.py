def equalColor() :
    global window, canvas, paper, inImage, outImage, inH, inW, outH, outW, filename
    global cvInImage, cvOutImage
    print('Run equalColor() Method ...')

    if filename == '' or filename == None :
        return

    ## 알고리즘에 의해 출력이미지의 높이,폭이 결정된다.
    outH = inH;
    outW = inW;

    ## 출력이미지 메모리 할당
    outImage = []
    for _ in range(RGB):  # 칼라는 r,g,b로 3개이지만 이런경우 전역상수로 만들어주는게 좋다.
        outImage.append(malloc(inH, inW));

    ### 진짜 영상처리 알고리즘 ###
    for rgb in range(RGB) :
        for i in range(inH):
            for k in range(inW):
                outImage[rgb][i][k] = inImage[rgb][i][k]

    ########################
    displayImageColor()