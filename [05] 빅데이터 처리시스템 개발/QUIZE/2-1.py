#미션2. 2~10000까지 소수를 모두 배열에 저장한 후, 배열의 합계를 출력한다.

print('미션2. 2~10000까지 소수를 모두 배열에 저장한 후, 배열의 합계를 출력한다.')
sum = 0
list = []
for i in range (3,10001) :
    check = True;
    for j in range (2,i) :
        if (i%j == 0) :
            check = False;
            break;
    if check :
        # print(i, end=',')
        list.append(i);

print(sum(list));