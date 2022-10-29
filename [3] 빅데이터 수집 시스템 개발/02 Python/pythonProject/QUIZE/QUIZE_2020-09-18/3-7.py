#랜덤(10~20)한 크기의 NxN배열(이미지)를 생성
import math

print("랜덤(10~20)한 크기의 NxN배열(이미지)를 생성")
image = [];
import random
#행
row = random.randint(10,20);
#열
col = random.randint(10,20);

image = []
tmp = []
for i in range(row) :
    tmp = []
    for k in range(col) :
        tmp.append(0);
    image.append(tmp)
print('\n')

#랜덤(0~255)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
for i in range(row) :
    for k in range(col) :
        image[i][k] = random.randint(0,255);
print('\n');

# 미션 3-7<심화>. 이미지를 2배 축소한다
print("미션 3-7<심화>. 이미지를 2배 축소한다")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

# 1/2 크기의 배열을 만들어준다
col2 = math.ceil(col/2);
row2 = math.ceil(row/2);
image2 = [];
for i in range(row2) :
    tmp = []
    for k in range(col2) :
        tmp.append(0);
    image2.append(tmp)
print('\n\n')

rowCnt = 0;
colCnt = 0;

for i in range(row2) :
    for k in range(col2) :

        # 패턴을 분석하기 위한 출력문
        print('[i=',i,',k=',k,'] :', '[',i+i,k+k,']', '[',i+i,k+k+1,']', '[',i+i+1,k+k,']','[',i+i+1,k+1+k,']');
        # 4개의 픽셀 평균값을 구해 저장한다.
        image2[i][k] = math.ceil((image[i+i][k+k] + image[i+i][k+k+1] + image[i+i+1][k+k+1] + image[i+i+1][k+k+1])/4);
    print()

print('\n');



print("After");
for i in range(row2) :
    for k in range(col2) :
        print("%3d" % (image2[i][k]), end=' ');
    print()
print('\n\n');

# [ 0 0 ][ 0 1 ][ 0 2 ][ 0 3 ][ 0 4 ][ 0 5 ][ 0 6 ]
# [ 1 0 ][ 1 1 ][ 1 2 ][ 1 3 ][ 1 4 ][ 1 5 ][ 1 6 ]
# [ 2 0 ][ 2 1 ][ 2 2 ][ 2 3 ][ 2 4 ][ 2 5 ][ 2 6 ]
# [ 3 0 ][ 3 1 ][ 3 2 ][ 3 3 ][ 3 4 ][ 3 5 ][ 3 6 ]
# [ 4 0 ][ 4 1 ][ 4 2 ][ 4 3 ][ 4 4 ][ 4 5 ][ 4 6 ]
# [ 5 0 ][ 5 1 ][ 5 2 ][ 5 3 ][ 5 4 ][ 5 5 ][ 5 6 ]
# [ 6 0 ][ 6 1 ][ 6 2 ][ 6 3 ][ 6 4 ][ 6 5 ][ 6 6 ]
