# def Sum(a,b):
#     Sum=a+b
#     print(Sum)
# Sum(10,20)

# def Sum(a,b):
#     Sum=a+b
#     print(Sum)
#     return Sum
# a=Sum(10,20)
# print(a)

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
#     print(Sum)
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

# def perform():
#     while True:
#         n=int(input())
#         a=int(input())
#         b=int(input())
#         if n==1:
#                 sum=a+b
#                 print(sum)
#         elif n==2:
#                 sub=a-b
#                 print(sub)
#         elif n==3:
#                 mul=a*b
#                 print(mul)
#         elif n==4:
#                 div=a//b
#                 print(div)
#         else:
#                 print("invalid")
#                 break
#     perform()

# def fact(n):                    #5
#     fact=1                      
#     for i in range(1,n+1):
#         fact*=i
#     return fact
# nmbr=int(input())
# f=fact(nmbr)
# print(f)

# def fact(n):                    #5              #4              #3              #2              #1
#     if n==1:                    #5==1 F         #4==1 F         #3==1 F         #2==1 F         #1==1
#         return 1                                                                                #return 1               
#     else:
#         return n*fact(n-1)      #5*fact(4=5-1)  #4*fact(3=4-1)  #3*fact(2=3-1)  #2*fact(1=2-1)
# nmbr=int(input())  #5
# f=fact(nmbr)
# print(f)

# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n+sum(n-1)
# nmbr=int(input())  
# sum=sum(nmbr)
# print(sum)

# n=int(input())
# fib=[0,1]
# for i in range(2,n):
#     next_value=fib[i-1]+fib[i-2]
#     fib.append(next_value)
# print(fib)

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input())  
# for i in range(n):
#     print(fib(i),end=" ")

#Map Function:-
# a=list(map(int,input().split()))
# print(a)

# def sqr(n):
#     return n*n
# lst=[1,2,3,4,5]
# sqrt=list(map(sqr,lst))
# print(sqrt)

# def sum(n):
#     return sum
# lst=[1,2,3,4,5]
# s=list(map(lambda n,x: n+x,[1,2,3,4,5]))
# print(s)

#anonimus function:-
# res=lambda x: x%2==0
# print(res(4))

# res=lambda x: "even" if x%2==0 else "odd"
# print(res(5))

# sum=lambda x,y,z: x+y+z
# n1=int(input())
# n2=int(input())
# n3=int(input())
# print(sum(n1,n2,n3))

# a=list(map(lambda x:x*x,[10,20,30]))
# print(a)

#Filter:-
# a=list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10]))
# print(a)

# a=list(filter(lambda x:x%2!=0,[1,2,3,4,5,6,7,8,9,10]))
# print(a)

#Reduce function:-
# from functools import reduce
# res=reduce(lambda s,x:s+x,[10,20,30])
# print(res)

#Decorators:-
# def first(k):
#     return k.upper()
# @first
# def second(name):
#     print(name)
# second("logic")










