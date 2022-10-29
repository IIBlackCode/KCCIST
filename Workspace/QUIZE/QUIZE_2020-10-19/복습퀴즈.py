'''

파이썬 뇌를 깨우는 복습퀴즈
(1) 3333부터 200000까지 숫자에서 123의 배수의 합계를 구한다.
(2) 2부터 100000까지 소수를 배열 sosuList에 저장한 후, 합계를 낸다.
(3) win.ini파일을 읽어서 출력하되, 각 행번호 및 문자를 거꾸로 출력한다.
(4) 다음 내용을 메모장에서 num.txt로 저장한다.
        100,200,300
        10,20,30,
        1,2,3
    이 파일을 읽어서 2차원 배열에 저장한다.
    그리고 2차원 배열의 합계를 출력한다.
(5) MySQL 또는 MariaDB에 SQL문으로 간단한 [회원테이블]을 만들고 데이터를 3건 입력한다.
    그리고, 이 테이블을 조회하는 파이썬 코드를 작성한다.

'''

#(1) 3333부터 200000까지 숫자에서 123의 배수의 합계를 구한다.
print("(1) 3333부터 200000까지 숫자에서 123의 배수의 합계를 구한다.")
temp = 0;
for i in range(3333,200000) :
    if i%123 == 0:
        temp += i;
print(temp)
print("===========================================================")
#(2) 2부터 100000까지 소수를 배열 sosuList에 저장한 후, 합계를 낸다.
print('(2) 2부터 100000까지 소수를 배열 sosuList에 저장한 후, 합계를 낸다.')
sosuSum = 0
sosuList = []
i = 0;
for i in range (3,100) :
    check = True;
    for j in range (2,i) :
        if (i%j == 0) :
            check = False;
            break;
    if check :
        print(i, end=',')
        sosuList.append(i)

for i in range(sosuList.__len__()) :
    sosuSum += sosuList[i];
print("소수 합 :",sosuSum);
print("===========================================================")
print('(3) win.ini파일을 읽어서 출력하되, 각 행번호 및 문자를 거꾸로 출력한다.')
#파일 열기
rfp = open('c:/windows/win.ini','r');   #1
#파일 쓰기
wfp = open('win2.txt','w');

lineArr = []
lineNum = 0
while True :
    lineNum +=1
    line = rfp.readline();
    if (line is None or line == '') :
        break;
    print('lineNum :',lineNum,' ',line, end='');
    wfp.writelines(line);
    lineArr.append(str(line))

strArr = []
for i in range(lineArr.__len__()):
    print('행번호:',lineArr.__len__()-i-1, '문자 :',lineArr[lineArr.__len__()-i-1][::-1])

#파일 닫기
rfp.close()                             #3
#파일을 먼저 열어주고 닫는다.
wfp.close()                             #
print("===========================================================")
print('(4) 다음 내용을 메모장에서 num.txt로 저장한다.')
'''
        100,200,300
        10,20,30,
        1,2,3
    이 파일을 읽어서 2차원 배열에 저장한다.
    그리고 2차원 배열의 합계를 출력한다.
'''