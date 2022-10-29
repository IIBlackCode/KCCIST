#랜덤(10~20)한 크기의 NxN배열(이미지)를 생성
import math

print("랜덤(10~20)한 크기의 NxN배열(이미지)를 생성")
image = [];
import random
#행
row = random.randint(3,4);
#열
col = random.randint(3,4);

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

#중위수

# 같은 크기의 배열을 만들어준다
print('같은 크기의 배열을 만들어준다')
image2 = [];
count = 0
for i in range(row*col) :

    image2.append(count);
    count += 1;
    print(count,end='\t');
print();

sum = 0;
count = 0

#2차원 배열을 1차원배열에 대입
print('2차원 배열을 1차원배열에 대입')
for i in range(row) :
    for k in range(col) :
        # image2[count] = image[i][k];
        image2[count] = image[i][k];
        print(image2[count], end='\t');
        count += 1;

        sum = sum + image[i][k];
        # sum = image.append(i);
print()

#1차원 배열을 정렬한다.
print('1차원 배열을 정렬한다.\n');

temp = 0;
cnt = 0;
for i in range(0,(count+1)*3) :
    check = False;
    print(i,'회 정렬 : ',temp)
    for k in range(0,count-1) :
        if image2[k] > image2[k+1] :
            cnt +=1;
            temp = image2[k];
            image2[k] = image2[k+1];
            image2[k+1] = temp;
            check = True;
            print(check, '교환 ', temp, 'index:',k,' image2[k]: ',image2[k],' image2[k+1]:',image2[k+1]);
        if check == True :
            print(check)
            break;
        print(image2[k],end='\t');
    print()
print('\n')

#1차원 배열 출력
print('정렬된 1차원 배열 출력')
for i in range(count) :
    print('[',i,':',image2[i],']',end='');
print('\n');

#반올림할 때 짝수에 묶는 "ROUND_HALF_EVEN" 방식을 사용하기 때문에 round를 사용하지 않음
center = math.ceil((count)/2-1);

print('총합 :',sum,', 총 갯수 :',count , ', 평균 :',math.ceil(sum/count),', 중간INDEX :' ,center, ', 중위수 :',image2[round(center)])
for i in range(row) :
    for k in range(col) :
        if image[i][k] <= image2[round(center)]:
            image[i][k] = 0;
        else:
            image[i][k] = 255;



print("After");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n\n');