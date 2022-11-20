# 리스트

# 1. 배열의 메모리 할당 (+초기화)
#list = [0,0,0,0,0];
list = [];
for i in range(5) :
    list.append(0);

# 2. 배열에 초기값 대입
# list[0] = 1;
# list[1] = 2;
# list[2] = 3;
# list[3] = 4;
# list[4] = 5;

num = 1
for i in range(5) :
    list[i] = num;
    num += 1;
    print(i,': num = ',num)

# 3. 배열 활용
# sum = list[0] + list[1] + list[2] + list[3] + list[4] ;
sum = 0;
for k in range(5) :
    sum = sum + list[k];

# 4. 배열 출력
print(sum);


#Quize5. 빈 배열 20개를 0으로 초기화 한 후, 20, 18, 16 .... 을 채운다.
#        그리고 배열의 숫자 중 음수의 합계, 양수의 합계를 따로 구해서 출력한다.

#1. 빈 배열 20개를 0으로 초기화
SIZE = 20;
listQuize = [];
for _ in range(SIZE) :
    listQuize.append(0);
#2
num = 20
for i in range(SIZE) :
    listQuize[i] = num;
    num -=2;

#3
sumPlusm, sumMinus = 0, 0;
for i in range(SIZE) :
    if listQuize[i] >= 0 :
        sumPlusm += listQuize[i];
    else :
        sumMinus += listQuize[i];
#4
print(sumPlusm, sumMinus);