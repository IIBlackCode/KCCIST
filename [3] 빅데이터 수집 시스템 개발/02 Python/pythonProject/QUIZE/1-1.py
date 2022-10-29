#미션 1-1. 구구단을 출력한다. 그리고 단의 제목도 쓴다.

for i in range(2,9) :
    print('*** ', i, '단 ***');
    for k in range(1,9) :
        print(i,' X ',k,' = ',(i*k));