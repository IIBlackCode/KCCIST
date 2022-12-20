#랜덤(10~20)한 크기의 NxN배열(이미지)를 생성

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
print('\n\n')


#랜덤(0~255)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
for i in range(row) :
    for k in range(col) :
        image[i][k] = random.randint(0,255);
print('\n\n');



# 미션 3-7<심화>. 이미지를 2배 축소한다
print("미션 3-7<심화>. 이미지를 2배 축소한다")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

col2 = (col/2).__int__();
row2 = (row/2).__int__();
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

        # print("[", i, ':', k, ']', '[',i+1,k+1,']', '[',i,k+1,']', '[',i+1,k,'][',rowCnt,colCnt,']');
        image2[i][k] = ((image[i][k] + image[i+1][k] + image[i][k+1] + image[i+1][k+1])/4).__int__();
    # print()

print('\n');



print("After");
for i in range(row2) :
    for k in range(col2) :
        print("%3d" % (image2[i][k]), end=' ');
    print()
print('\n\n');