                         # 02/02/26

#without parameter and without return value
# def Sum():
#     a=int(input())
#     b=int(input())
#     Sum=a+b
#     print(Sum)
# Sum()

#with parameter and with return value
# def Sum(a,b):
#     a=int(input())
#     b=int(input())
#     Sum=a+b
#     print(sum)
#     return Sum
# Sum()

#with parameter and without return value
# def Sum(a,b):
#     a=int(input())
#     b=int(input())
#     Sum=a+b
#     print(Sum)
# Sum()

#without parameter and with return value
# def Sum():
#     a=int(input())
#     b=int(input())
#     Sum=a+b
#     print(Sum)
#     return Sum
# Sum()

                         #03/02/2026

#function statement with using print statement

# def first(a,b):
#     sum=a+b
#     print(sum)
# first(10,20)

#function statement with using return statement

# def first(a,b):
#     sum=a+b
#     return sum
# first(10,20) 

# def first(a,b,c):
#     sum=a+b+c
#     print(sum)
# first(10,20,30)

# def first(a,b,c):
#     sum=a+b+c
#     return sum
# a=first(10,20,30)
# print(a)

#TYPES OF ARGUMENTS
#1.POSITIONAL
# def first(a,b):
#     sum=a+b
#     print(a)
#     print(b)
#     print(sum)
# first(10,20)

#2.KEYWORD ARGUMENTS
# def first(a,b,c):
#     sum=a+b+c
#     print("A value",a)
#     print("B value",b)
#     print("C value",c)
#     print(sum)
# first(c=30,b=20,a=10)

# def sravs(name,age):
#     print("name",name)
#     print("age",age)
# sravs(age=20,name="sravanthi")

#3.DEFAULT PAREMETERS
# def sravs(name,age=20):
#     print("name",name)
#     print("age",age)
# sravs(name="sravanthi")
# sravs("suji",21)

#4.VARIABLE LENGTH ARGUMENTS
   #tupule fomet
# def first(*a):
#     print(a)
# first(10,20,30)
# first(10,20,22,33,44,55)
   #without tuple format with using loops
# def first(*a):
#     for i in a:
#         print(i,end=" ")
# first(10,20,30)
# first(10,20,22,33,44,55)

# def first(n,*a):
#     print(n,a)
# first(10,20,10)
# first(49,20,30,40,50)

#5.KWARGES(**)
# def first(**d):
#     print(d)
# first(a="s",b="r",c="a",d="v",e="s")

# def first(**d):
#     for i in d.items():
#         print(i,end=" ")
# first(a="s",b="r",c="a",d="v",e="s")

# def one(l1,l2):
#     print(l1,l2)
# lst=[10,20,30]
# lst2=[20,40,50,30]
# one(lst,lst2)

#FUNCTION PASS INTO ANOTHER FUNCTON INPUT
# def f1(n):
#     return n*n
# def f2(y):
#     print(y)
# f2(f1(5))

#NESTED FUNCTIONS
# def f1(x):
#     def f2(y):
#         print(x+y)
#     f2(10)
# f1(20)