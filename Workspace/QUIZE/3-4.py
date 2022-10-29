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


# 미션 3-4. 이미지를 2진화 시킨다. 평균값 기준
print("미션 3-4. 이미지를 2진화 시킨다. 평균값 기준")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

#평균값
sum = 0;
count = 0
for i in range(row) :
    for k in range(col) :
        sum = sum + image[i][k];
        count +=1;
print('총합 :',sum,', 총 갯수 :',count , ' 평균 :',(sum/count))

for i in range(row) :
    for k in range(col) :
        if image[i][k]  <= (int)(sum/count) :
            image[i][k] = 0;
        else:
            image[i][k] = 255;

print("After");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');

# 미션 3-6. 이미지를 좌우 미러링 한다.
# 미션 3-7<심화>. 이미지를 2배 축소한다.
# 미션 3-8<심화>. 이미지를 2배 확대한다.
# 미션 3-9<심화>. 이미지를 90도 회전한다.
# 미션 3-10<심화*2> 이미지를 45도 회전한다.