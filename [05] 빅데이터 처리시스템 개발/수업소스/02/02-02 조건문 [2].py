#조건문

num1 = 100;
#블럭을 묶을 때 콜론사용 :
#블럭이 없기 때문에 줄맞추는것이 중요
#스페이스바 4번 = tab키

#주석처리방법
#Ctrl + / : 해당범위만큼 주석 처리
"""
    문자열 처리로 주석 효과
"""
if num1 > 100 :
    print('100 보다 크다');
    print('수고했어요.')
elif num1 < 100:
    print('100보다 작다');
    print('수고했어요');
else :
    print('num1의 값은 ',num1);

#Quize 점수를 입력받기 (0~100) --> 학점 출력하기

score = int(input('숫자(0~100)-->'));

if score > 100:
    print('잘못 입력하셧습니다.')
elif score >= 90 :
    print('A' , end = '');
elif score >=80 :
    print('B' , end = '');
elif score >= 70 :
    print('C' , end = '');
elif score >= 60 :
    print('D' , end = '');
elif score <60 :
    print('F', end = '');

print('입니다.')
