#미션 1-1. 구구단을 출력한다. 그리고 단의 제목도 쓴다.

print('구구단 세로출력')
for i in range(2,10) :
    print(' *** ', i, '단 *** ');
    for k in range(1,10) :
        print(i,' X ',k,' = ',(i*k));

print()

print('구구단 가로출력')
for i in range(1,10) :
    # print('*** ', i, '단 ***');
    for k in range(2,10) :
        if i*k>=10 :
            print(k,'X',i,'=',(i*k),'\t ',end='');
        else :
            print(k,'X',i,'=',(i*k),' \t ', end='');
    print()