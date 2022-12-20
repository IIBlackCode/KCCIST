#랜덤(10~20)한 크기의 NxN배열(이미지)를 생성
from statistics import median

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
print('\n')

#랜덤(0~255)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
for i in range(row) :
    for k in range(col) :
        image[i][k] = random.randint(0,255);
print('\n\n');

# 미션 3-9<심화>. 이미지를 90도 회전한다.
print("미션 3-9<심화>. 이미지를 90도 회전한다.[시계방향]")
print("Before");
for i in range(row) :
    for k in range(col) :
        print("%3d" % (image[i][k]), end=' ');
    print()
print('\n');

# 90도 회전시 담아줄 배열 선언 [행과 열이 같지않을 수 있기 때문에 대입해줄 배열의 행렬은 기존의 값과 반대]
image2 = [];
for i in range(col) :
    tmp = []
    for k in range(row) :
        tmp.append(0);
    image2.append(tmp)
print('\n\n')

# i행 k열일 때 찍는 좌표값 패턴을 파악한다.
for i in range(row) :
    for k in range(col) :
        # 이동해야할 좌표값 패턴 분석, [아래 if문은 출력시 칸을 맞추기 위함]
        if image[i][k]<10 :
            print('[',i,':',k,'] = ',image[i][k],' \t\t>>> [',k,row-i-1,']');
        elif image[i][k] < 100 :
            print('[', i, ':', k, '] = ', image[i][k], ' \t\t>>> [', k, row - i - 1, ']');
        else :
            print('[', i, ':', k, '] = ', image[i][k], '   \t>>> [', k, row - i - 1, ']');
        
        #90도 회전된 좌표로 대입
        # image2[k][row-i-1] = image[i][k];
        image2[i][k] = image[row - k - 1][i];

    print();
print('\n');

print("After");
for i in range(col) :
    for k in range(row) :
        print("%3d" % (image2[i][k]), end=' ');
    print()
print('\n\n');