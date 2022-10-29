#미션 3-10<심화*2> 이미지를 45도 회전한다.
from statistics import median

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



# 미션 3-9<심화>. 이미지를 90도 회전한다.
print("미션 3-9<심화>. 이미지를 90도 회전한다.")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

# 90도 회전시 담아줄 배열 선언
image2 = [];
for i in range(col) :
    tmp = []
    for k in range(row) :
        tmp.append(0);
    image2.append(tmp)
print('\n\n')

# i행 k열일 때 찍는 좌표값 패턴을 파악한다.
for i in range(row) :
    for k in range(col) :
        # print("[", i, ':', k, ']','[',i,k,'],[',k,row-i-1,']');
        print("[", i, ':', k, ']','[',image[i][k], '],[', k, row - i - 1, ']');
        # if row-i >0 :
        image2[k][row-i-1] = image[i][k];
        # else:
        #     pass;

    print()

print('\n');



print("After");
for i in range(col) :
    for k in range(row) :
        print("%3d" % (image2[i][k]), end=' ');
    print()
print('\n\n');