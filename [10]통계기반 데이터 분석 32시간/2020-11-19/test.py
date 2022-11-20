# Numeric - Integer, Complex Number, Float
# Dictionary
# Boolean
# Set
# Sequence Type - Strings, List, Tuple
a = 10
print(type(a))
b = 10.2
print(type(b))
c = 1 + 2j
print(type(c))
str = "Hello Python"
print(str)
print(str[0:2], str[4], str * 2)
list1 = [1, "hello", 2]
print(list1, list1[0:2], list1[1])

tup1 = (1, 'Hello', 'test')
print(tup1, tup1[0:2], tup1[1])
dic1 = {1:'one', 2:'two', 3:'three'}
print(dic1, dic1[1], dic1.keys(), dic1.values())

# Set
set2 = {'Tom', 1, 2, 2, 'Jane'}
print(set2)

# pass
tests = {'p', 'y', 't'}
for s in tests:
    pass

# function
# .py
# function, class
a = 10
b = 20
def add(a, b):
    temp = a
    a = b
    b = temp
    return a, b
x, y = add(a, b)
print(x, ',', y)

def change_list(list1):
    list1.append(20)
    list1.append(30)
    print('안에', list1)

list1 = [10, 30, 40, 50]
change_list(list1)
print('밖에', list1)

def add3(a, b=0, c=0):
    return a + b + c

add3(1)
add3(1,2)
add3(1,2,3)
d = add3(a=1, b=2, c=3)
print(d)

# *
def myfunc(*names):
    print(type(names))

myfunc(1,2,3,4,5)
# **
def myfunc2(**vals):
    print(vals)

myfunc2(name='Tom', age=30)

def x1(a):
    return a + 10
x1(10)
# lambda
x = lambda a : a + 10
x(10)

def myfunc3(n):
    return lambda a : a + n

x2 = myfunc3(4)
print(type(x2), x2(10))
# Apache Spark ML

# map()
list4 = (10,20,30,40,50)
result = list(map(lambda x: x*2, list4))
print(result)





