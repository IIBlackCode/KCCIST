#Python의 입력받기
# 주석
num1 = int(input('숫자1-->'));
num2 = int(input('숫자2-->'));

result1 = num1 + num2;
result2 = num1 - num2;
result3 = num1 * num2;
result4 = num1 / num2;


print(num1, ' + ', num2, ' = ',sum);

##print의 여러가지 형태
print("%d + %d = %d" %(num1, num2, result1));
print("{} + {} = {}".format(num1, num2, result1));
print("{0} + {1} = {2}".format(num1, num2, result1));
print("{1} + {0} = {2}".format(num1, num2, result1));
print("{1:d} + {0:f} = {2:5.2f}".format(num1, num2, result1));

print("계산기 프로그램");

#계산기
print("{} + {} = {}".format(num1, num2, result1));
print("{} - {} = {}".format(num1, num2, result2));
print("{} * {} = {}".format(num1, num2, result3));
print("{} / {} = {}".format(num1, num2, result4));

num1 = 100;
num1 = num1 + 1

print(num1);

num1 += 1;
print(num1);



