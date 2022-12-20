#함수 선언부
def plus (n1,n2,n3=0) :
    retval = 0

    retval1 = n1 + n2 + n3;
    retval2 = n1 - n2 - n3;

    return  retval, retval2;


#전역 변수부
#   : 모든 함수에서 공통으로 사용할 수 있는 변수
num1, num2 = 100, 200;
sum, sub = 0, 0;
myValue = 1234;

#메인 코드부
if __name__ == '__main__' :

    sum  = num1 + num2;
    print(sum);

    sum = num1 + 50;
    print(sum);
    pass;

    sum, _ = plus(num1,num2,500);
    print(sum);
