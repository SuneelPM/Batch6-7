#                                  Date:-16-2-26
                                    # Day-1
#                                  Topic:-Basics

# print("hello world")

# print("name:sravanthi")
# print("class:b.tech")
# print("branch:ai&ds")
# print("secton:c")
# print("rollno:54h5")

# name=input()
# print("hello:",name)

# name="sravss"
# age=20
# perc=7.7
# print(name)
# print(age)
# print(perc)

# name=input()
# age=int(input())
# perc=float(input())
# print("name",name)
# print("age",age)
# print("perc",perc)

# a=10
# b=20
# sum=a+b
# print(sum)

# a=int(input())
# b=int(input())
# sum=a+b
# print(sum)

# city="tenali"
# state="ap"
# country="india"
# print("city",city,"state",state,"country",country)

# name=input()
# print("hello",name,"have a great day")

# age=int(input())
# print("your are",age,"years old after 5 years you will be",age+5)

# num=int(input())
# print(num*num)

# a=10
# b=20
# print(a+b,a-b,a*b,a/b)

# len=20
# bre=20
# area=len*bre
# print(area)

# c=int(input())
# f=(c*9/5)+32
# print(f)

# name=input()
# age=int(input())
# city=input()
# print(f"hello {name}\n you are {age} years old\nyou live in {city}")


                                            #  DATE;-17-2-26
                                            #   DAY-2
                                            #   TOPIC:datatypes
                                            #         type casting
                                            #         user input
                                                    
# a=10
# b=20.2
# c="sravss"
# d=True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# x="20"          
# y=int(x)
# print(y)

# a=input()
# print("hello",a)
# a=int(input())
# print("this is integier",a)

# a=int(input())
# b=int(input())
# sum=a+b
# print(sum)

# a=10
# if a%2==1:
#     print("this is even number")
# else:
#     print("this is odd number")

# name=input()
# age=int(input())
# print("hello",name,"you are",age,"years old" )
# print(f"hello {name}, you are {age} years old")

# number=int(input())
# if number%2==0:
#     print("even number")
# else:
#     print("odd number")


# number=int(input())
# if number%2==0:
#     print("positive number")
# else:
#     print("negative number")

# p=int(input())
# r=int(input())
# t=int(input())
# simple_intrest=p*r*t/100
# print(simple_intrest)

# a=int(input())
# b=int(input())
# if a>b:
#     print("largest number is:",a)
# else:
#     print("lagest number is:",b)

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b:
#     print("a is biggest number")
# elif b>c:
#     print("b is biggest number")
# else:
#     print("c is biggest number")

# age=int(input())
# if age<13:
#     print("this is child")
# elif age<=19:
#     print("this is teen")
# elif age<=59:
#     print("this is adult")
# else:
#     print("this is senior")

# num1=int(input())
# num2=int(input())
# sum=num1*num2
# print(sum)

# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# age=int(input())
# if age>=90:
#     print("grade A")
# elif age>=74:
#     print("grade B")
# elif age>=50:
#     print("grade C")
# else:
#     print("fail")

                                        #   DATE:-18-2-26
                                        #    DAY:-3
                                        # TOPIC:-LOOP
# HOW TO PRINT 5 NUMBER
# for i in range(5):
#     print(i)

# i=1
# while i<=5:
#     print(i)
#     i+=1

# HOW TO PRINT 10 NUMBERS
# for i in range(10+1):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1
 
# HOW TO PRINT EVEN NUMERS
# for i in range(10):
#     if i%2==0:
#         print(i)

# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# HOW TO CALCULATE SUM
# sum=0
# for i in range(10+1):
#     print(i)
#     sum+=i
# print(sum)

# sum=0
# i=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)

# HOW TO CALCULATE SUM FROM THE USER
# num=int(input())
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print(sum)

# num=int(input())
# sum=0
# i=1
# while i<=10:
#     sum+=i
#     i+=i
# print(sum)

# HOW TO PRINT 3 TABLE
# n=3
# for i in range(10+1):
#  print(n,"*",i,"=",n*i)

# HOW TO PRINT FACTORIAL PROBLEM
# num=int(input())
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)
    
# HOW TO PRINT PEIME NUMBER
# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")

                                                #    Date:-19-2-26
                                                #     Day:-4
                                                #     Topic:-strings
# string="sravanthi" 
# print(string)  

# HOW TO PRINT STRING INDEXING
# name="sravanthi"
# print(name[0])
# print(name[4])
# print(name[-1])
# print(name[0:4])
# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())

# name="sravss"
# print(name[0])
# print(name[-1])
# print(len(name[2]))

# HOW TO PRINT NAME REVERSE ORDER
# name="sravss"
# print(name[::-1])

# COUNT OWELS IN A STRING
# name=input()
# count=0
# for i in name:
#     if i in "aeiou":
#         count+=1
# print(count)
 
# PALINDROM CHECK 
# word="madam"
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# HOW TO IDENTIFY THE INPUT SPACES
# WITH LOOP
# name=input()
# count=0
# for i in name:
#     if i==" ":
#         count+=1
# print(count)

# WITHOUT LOOP 
# name=input()
# print(name.count(" "))

# CORRECT WAY TO COUNT WORDS
# name=input()
# words=name.split()
# print(len(words))

#STRING REPLACE
# text="i love python"
# print(text.replace("python","ai"))

# FIND STRING
# name="i love you"
# print(name.find("you"))

# STRING CONCATENATION
# a="Hello"
# b="Sravanthi"
# print(a+" "+b)

# F-STRINGS 
# name="sravanthi"
# age="20"
# print(f"hello i am {name} {age} years old")

                                    # DATE:-20-2-26
                                    #  DAY-5
                                    # TOPIC:-LISTS

# number=[10,20,30,50]
# print(number)

# LIST INDEXING
# num=[10,20,30,40]
# print(num[0])
# print(num[2])

# LIST SLICING
# num=[10,20,30,40,50]
# print(num[1:4])

# ADD ELEMENTS
# num=[10,20,30,40,50]
# num.append(4)
# print(num)

# INSERT ELEMENTS
# num=[10,20,30,40,50]
# num.insert(2,99)
# print(num)
# num.remove(99)
# print(num)

# list=[1,2,3,4,5]
# print(list[4])

# list.insert(2,22)
# print(list)

# list.insert(6,10)
# print(list)

# print(len(list))

# list.remove(1)
# print(list)

# IDENTIFY THE TOTAL SUM
# list=[10,10,30,50]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# lst=[2,3,5,7,9]
# print(max(lst))

# IN LIST IDENTIFY THE BIG NUMBER
# lst=[1,2,5,7,9]
# big=lst[0]
# for i in lst:
#     if i>big:
#         big=i
# print(big)


# EVEN NUMBER
# lst=[1,2,3,4,5,6]
# for i in lst:
#     if i%2==0:
#        print(i)

# lst=[1,2,3,4,5]
# big=lst[0]
# low=lst[0]
# for i in lst:
#     if i>big:
#         big=i
#     if i<low:
#         low=i
# print(big)
# print(low)

# lst=[2,1,4,3,7,5]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)
# new_lst=sorted(lst)
# print(lst)
# print(new_lst)

# lst1=[10,4,7,1,9]
# lst1.sort(reverse=True)
# print(lst1)

