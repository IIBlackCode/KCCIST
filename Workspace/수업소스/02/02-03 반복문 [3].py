# 1부터 10까지 출력하기

for i in range(0,10,1) :
    print(i);

#Quize2. 1~100까지의 합 구하기

for i in range (0, 101 ,1) :
    print( i );

sum = 0;
for i in range (0, 101 ,1) :
    sum = sum + i;

print( '0~ 100까지의 합 : ',sum );

sum = 0
i = 0;
for i in range (101) :
    sum = sum + i;

print( '0~ 100까지의 합 : ',sum );

print('=============================================');

#Quize 3-1. -3333 ~ + 4444까지의 합계
print('[Quize 3-1]. -3333 ~ + 4444까지의 합계')
sum = 0
i = 0;
for i in range (-3333,4444) :
    sum = sum + i;
print('-3333 ~ + 4444까지의 합계 :', sum);
print('=============================================');

#Quize 3-2. -77 ~ + 2345까지의 홀수의 합계

print('[Quize 3-2]. -77 ~ + 2345까지 홀수의 합계')
sum = 0
i = 0;
for i in range (-77,2345) :
    if i%2 != 0:
        sum = sum + i;
print('-77 ~ + 2345까지 홀수의 합계 :', sum);
print('=============================================');

#Quize 3-3. 777 ~ + 23456까지의 555의 배수의 합계
print('[Quize 3-3]. 777 ~ + 23456까지의 555의 배수의 합계')
sum = 0
i = 0;
for i in range (777,23456) :
    if i%555 == 0:
        sum = sum + i;
    else :
        pass
print('777 ~ + 23456까지의 555의 배수의 합계 :', sum);
print('=============================================');

#Quize 4(심화). 2부터 10000까지의 소수를 모두 출력하고 합계내기
#소수 : 1과 자신을 제외하고 나눠지는 수가 없는 수.


print('[Quize 4(심화)].  2부터 10000까지의 소수를 모두 출력하고 합계내기')
sum = 0
i = 0;
for i in range (3,10001) :
    check = True;
    for j in range (2,i) :
        if (i%j == 0) :
            check = False;
            break;
    if check :
        print(i, end=',')
        sum += i;
print()
print('2부터 10000까지의 소수 :',sum);


print('=============================================');
