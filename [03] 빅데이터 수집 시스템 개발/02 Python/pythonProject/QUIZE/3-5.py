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

# 미션 3-5<심화>. 이미지를 2진화 시킨다. 중위수 기준
print("미션 3-5<심화>. 이미지를 2진화 시킨다. 중위수 기준")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

#평균
sum = 0;
count = 0
for i in range(row) :
    for k in range(col) :
        sum = sum + image[i][k];
        count +=1;

count1 = 0;

#중위수
temp = [row*col];
for i in range(row*col) :
    temp.append(i);

for i in range(row) :
    for k in range(col) :
        temp[count1] = image[i][k];
        count1 = count1+1;
center = (row*col/2).__int__()

print('총합 :',sum,', 총 갯수 :',count , ' 평균 :',(sum/count).__int__(), ' 중위수 :',center)
for i in range(row) :
    for k in range(col) :
        if image[i][k]  <= center :
            image[i][k] = 0;
        else:
            image[i][k] = 255;



print("After");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');