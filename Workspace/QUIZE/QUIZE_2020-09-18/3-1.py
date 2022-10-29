# 미션3. 랜덤(10~20)한 크기의 NxN배열(이미지)를 생성하고, 랜덤(0~255)한 값을 채운다.
#       그리고 다음 요구사항 새 배열로 저장한다.

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


#출력
print("** 출력 **")
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');


# 미션 3-1. 이미지에 모두 100을 더한다.
print("미션 3-1. 이미지에 모두 100을 더한다.")
for i in range(row) :
    for k in range(col) :
        if image[i][k] + 100 > 255 :
            image[i][k] = 255;
        else:
            image[i][k] += 100;

for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');