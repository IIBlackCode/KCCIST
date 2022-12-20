# ** 3일차 (빅데이터 수집 시스템 개발) **
# 복습 퀴즈
# (1) 3 ~ 1000 까지의 숫자를 랜덤하게 100개 발생시켜서, 배열에 저장한 후 합계 내기
print('(1) 3 ~ 1000 까지의 숫자를 랜덤하게 100개 발생시켜서, 배열에 저장한 후 합계 내기')
numArr = [];
import random
#행
arrLength = 100;

#배열 생성
for i in range(arrLength):
    numArr.append(0);
print('\n')

# 랜덤(3~1000)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
count = 0;
for i in range(arrLength):
     numArr[i] = random.randint(3, 1000);
     print(count,end='\t')
     count += 1;

print()

print("*** 출력하기 ***")
for i in range(arrLength):
    print(numArr[i], end='\t');
print('\n')

# (2) 위 1번에서 소수를 찾아서 출력하고, 소수의 합계를 내기
print('(2) 위 1번에서 소수를 찾아서 출력하고, 소수의 합계를 내기')
sum = 0
for i in range (0,100) :
    check = True;
    for j in range (2,i) :
        if (numArr[i]%j == 0) :
            check = False;
            break;
    if check :
        print(numArr[i], end=',')
        # list.append(i);
        sum = sum + numArr[i];

print('\n소수의 합 : ',sum);


# (3) <심화> 위 2번에서 찾은 소수를 '각 소수부터 1씩 감소시켜 1까지 합계'를 출력하고, 모든 합계도 출력
#
#      예)  배열의 수가  13, 14, 333, 9, 7 ..... 이라면
#
#            13+12+...+2+1 = 합계1 출력
#
#            7 + 6 + ...+2+1 = 합계2 출력
#
#            ....
#
#           합계1 + 합계2 + .... = 총합 출력
# for i in range(row) :
#     for k in range(col) :
#
#         print('[i:',i,' k:',k,' ',image[i][k],',',row-i-1,' ',col-k-1,image[i][col-k-1],']')
#         temp = image[i][k];
#         image[i][k] = image[i][col-k-1];
#         image[i][col-k-1] = temp;
#
#     print()
#
# print('\n');
print('(3) <심화> 위 2번에서 찾은 소수를 각 소수부터 1씩 감소시켜 1까지 합계를 출력하고, 모든 합계도 출력')
sum = 0
for i in range (0,100) :
    check = True;
    for j in range (2,i) :
        if (numArr[i]%j == 0) :
            check = False;
            break;
    if check :

        print(numArr[i]-1, end=',')
        # list.append(i);
        sum = sum + (numArr[i]-1);

print('\n소수의 합 : ',sum);


# (4) <심화> 3~5 크기의 랜덤한 3차원 배열 (예 : 4x3x5)을 생성하고, 해당 배열의 총 개수에 해당하는 가장 큰 소수 부터 저장하라.
print("(4) <심화> 3~5 크기의 랜덤한 3차원 배열 (예 : 4x3x5)을 생성하고, 해당 배열의 총 개수에 해당하는 가장 큰 소수 부터 저장하라.")
numArr3 = [];
import random
#X
xx = random.randint(3,5);
#Y
yy = random.randint(3,5);
#Z
zz = random.randint(3,5);

#3차원배열 생성
tmp = []
for x in range(xx) :
    tmp = []
    for y in range(yy) :
        for z in range(zz) :
            tmp.append(0);
            numArr3.append(tmp)
            print(numArr3[x][y][z], end='')
print('\n')

print(xx,yy,zz)

count = 0;

# 소수 생성
temp = [];
for i in range (3,1000) :
    if(count <= (xx*yy*zz)) :
        check = True;
        for j in range (2,i) :
            if (i%j == 0) :
                check = False;
                break;
        if check :
            print('count:',count,'i:',i);
            count +=1;
            temp.append(i);

for i in range(xx*yy*zz) :
    print(temp[i],end='\t')
count = xx*yy*zz-1;

for x in range(xx):
    for y in range(yy) :
        for z in range(zz) :
            numArr3[x][y][z] = temp[count]
            count -= 1;
            print(numArr3[x][y][z], end='')






        # list.append(i);




#       예) 4x3x5=60 이므로, 배열의[0][0][0] 번째에는  60번째 소수 (2, 3, 5, 7 ..... 60번째소수)
#
#                                     배열의[0][0][1] 번째에는   59번째 소수 (2, 3, 5, 7 .... 59번째소수)
#
#            ....
#
#                                     배열의 [3][2][4] 번째에는  첫번재 소수(2)를 저장한다.
#
# 10시까지  카페에 '미션/과제 제출방'에 제출



# [복습퀴즈 9/21] 홍길동