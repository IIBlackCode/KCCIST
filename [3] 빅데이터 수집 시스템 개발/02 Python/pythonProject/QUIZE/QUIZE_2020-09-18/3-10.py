# 랜덤(10~20)한 크기의 NxN배열(이미지)를 생성

print("랜덤(10~20)한 크기의 NxN배열(이미지)를 생성")
image = [];
import random

# 행
row = random.randint(3, 4);
# 열
col = row;
# col = random.randint(10, 20);

image = []
tmp = []
for i in range(row):
    tmp = []
    for k in range(col):
        tmp.append(0);
    image.append(tmp)
print('\n\n')

# 랜덤(0~255)한 값을 채우기
print("랜덤(0~255)한 값을 채우기")
for i in range(row):
    for k in range(col):
        image[i][k] = random.randint(0, 255);


# 미션 3-10<심화*2> 이미지를 45도 회전한다.
print("미션 3-10<심화*2> 이미지를 45도 회전한다.")
print("Before");
for i in range(row):
    for k in range(col):
        print("[%3d]" % (image[i][k]), end=' ');
    print()
print('\n');

# 45도 회전시 담아줄 배열 선언 [행과 열이 같지않을 수 있기 때문에 대입해줄 배열의 행렬은 기존의 값과 반대]
image2 = [];
count = 0;
col2 = round(col*2-1/2)-1;
row2 = round(row*2-1/2)-1;

for i in range(row2):
    tmp = []
    for k in range(col2):
        print('[', i, k, ']', end='')
        tmp.append(None);
    print()
    image2.append(tmp)
print('\n\n')

for i in range(col):
    for k in range(row,0,-1):

        if row2 - k -i >= 0 :
            # print('[', i, ':', k, '] \t\t>>> [', k,row2 - k -i, ']');
            print('[', i, ':', k, '] \t\t>>> [', col-k, row2 - k - i, ']');
            image2[k*-1][row2-k-i] = image[i][k*-1];
            # image2[col-k][row2-k-i] = image[i][k];
        else :
            pass;

    print()

print('\n\n')

print("After");
for i in range(row2):
    for k in range(row*2-1):
        if image2[i][k] is None :
            print('[',i,k,']', end='\t');
        else :
            print("[%3d]" % (image2[i][k]), end='\t');

    print()
print('\n\n');