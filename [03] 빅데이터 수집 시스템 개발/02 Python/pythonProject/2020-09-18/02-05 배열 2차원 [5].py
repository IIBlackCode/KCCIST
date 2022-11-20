# 2차원 배열
import random
# ary2 = [
#         [1,2,3,4],
#         [5,6,7,8],
#         [9,0,11,12],
#     ];

# print(ary2[2][2]);

ary2 = [];#2차원 배열
tmp = []; #임시 1차원 배열

num = 1;
for i in range(3)  : # 행
    tmp = [] #행이 돌기전 tmp를 비우는것을 권장
    for k in range(4) : # 열
        num += 1;
    ary2.append(tmp)
i = 0;
k = 0;
#
# for i in range(3)  : # 행
#     for k in range(4) : # 열
#         print(ary2[i][k]);


#이미지를 읽어서 2차원 배열에 채우기(가상)



# 1.파일의 크기를 알아내기
row = random.randint(5,7);
col = random.randint(5,7);

#2. 메모리 할당
image = []
tmp = []
for i in range(row) :
    tmp = []
    for k in range(col) :
        tmp.append(0);
    image.append(tmp)
print("=======================================")
#3. 파일 --> 메모리
for i in range(row) :
    for k in range(col) :
        image[i][k] = random.randint(0,255);
print("=======================================")
#출력하기
for i in range(row) :

    for k in range(col) :

        print("%3d" % (image[i][k]), end=' ')

    print()
print("=======================================")
#4-1 밝게하기 영상처이 알고리즘 적용
for i in range(row) :
    for k in range(col) :
        print('%3d'% (image[i][k]),end =' ');
    print()
print("=======================================")