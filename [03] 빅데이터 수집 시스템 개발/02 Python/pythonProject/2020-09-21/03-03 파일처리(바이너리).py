
#rb = read binary
# rfp = open('C:/images/Etc_Raw(squre)/512/LENA512.RAW','rb'); # 512x512 크기
rfp = open('C:/images/Etc_Raw(squre)/512/LENNA512.RAW', 'rb') # 512x512 크기
#   1. 이미지 크기 알아내기
height = 512;
width = 512;

#   2. 메모리 할당(배열)
image = [];
tmp = [];
for _ in range(height) :
    tmp = []
    for _ in range(width) :
        tmp.append(0)
    image.append(tmp)

#   3. 파일 --> 메모리
for i in range(height) :
    for k in range(width) :
        image[i][k] = rfp.readline(1);

print(image[111][111])