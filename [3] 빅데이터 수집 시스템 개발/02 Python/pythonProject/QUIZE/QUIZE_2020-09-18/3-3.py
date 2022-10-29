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
print('\n')


#랜덤(0~255)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
for i in range(row) :
    for k in range(col) :
        image[i][k] = random.randint(0,255);
print('\n');

# 미션 3-3. 이미지를 2진화 시킨다. 127기준 (0과 255만 있는 배열)
print("미션 3-3. 이미지를 2진화 시킨다. 127기준 (0과 255만 있는 배열)")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

for i in range(row) :
    for k in range(col) :
        if image[i][k]  <= 127 :
            image[i][k] = 0;
        else:
            image[i][k] = 255;

print("After");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');