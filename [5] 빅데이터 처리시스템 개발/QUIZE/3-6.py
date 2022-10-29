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
print('\n\n')


#랜덤(0~255)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
for i in range(row) :
    for k in range(col) :
        image[i][k] = random.randint(0,255);
print('\n\n');

# 미션 3-6. 이미지를 좌우 미러링 한다.
print("미션 3-6. 이미지를 좌우 미러링 한다.")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

# print('총합 :',sum,', 총 갯수 :',count , ' 평균 :',(sum/count), ' 중위수 :',center)
for i in range(row) :
    for k in range(col) :

        print('[i:',i,' k:',k,' ',image[i][k],',',row-i-1,' ',col-k-1,image[i][col-k-1],']')
        temp = image[i][k];
        image[i][k] = image[i][col-k-1];
        image[i][col-k-1] = temp;

    print()

print('\n');



print("After");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');