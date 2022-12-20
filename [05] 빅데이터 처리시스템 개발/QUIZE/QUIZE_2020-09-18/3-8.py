#랜덤(10~20)한 크기의 NxN배열(이미지)를 생성
from statistics import median

print("랜덤(10~20)한 크기의 NxN배열(이미지)를 생성")
image = [];
import random
#행
row = random.randint(5,10);
#열
col = random.randint(5,10);

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
print('\n\n');

# 미션 3-8<심화>. 이미지를 2배 확대한다
print("미션 3-8<심화>. 이미지를 2배 확대한다")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

# 확대된 이미지를 담은 행과 열의 2배인 2차원 배열을 만들어준다.
col2 = (col*2);
row2 = (row*2);
image2 = [];
for i in range(row2) :
    tmp = []
    for k in range(col2) :
        tmp.append(0);
    image2.append(tmp)
print('\n\n')

# i행 k열일 때 찍는 좌표값 패턴을 파악한다.
for i in range(row) :
    for k in range(col) :

        # 패턴을 분석하기 위한 출력문
        print("[",i,':',k,'] >>>', '[',i+i,k+k,']\t', '[',i+i,k+k+1,']\t', '[',i+i+1,k+k,']\t', '[',i+i+1,k+k+1,']\t');

        # print("[", i, ':', k, ']', '[', i + 1, k + 1, ']', '[', i, k + 1, ']', '[', i + 1, k, ']');
        # image2[i][k] = ((image[i][k] + image[i+1][k] + image[i][k+1] + image[i+1][k+1])/4).__int__();
        image2[i+i][k+k] = image[i][k];
        image2[i+i][k+k+1] = image[i][k];
        image2[i+i+1][k+k] = image[i][k];
        image2[i+i+1][k+k+1] = image[i][k];
    print()

print('\n');

print("After");
for i in range(row2) :
    for k in range(col2) :
        print("%3d" % (image2[i][k]), end=' ');
    print()
print('\n\n');