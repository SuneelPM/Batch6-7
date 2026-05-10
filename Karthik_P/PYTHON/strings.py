# print("Welcome to \
# python  \
# programming")

# print("""Welcome
# to python
# Programming""")

# print('Welcome'
#       'to python'
#       'programming')

# print('Welcome\nto python\nprogramming')

# n="KARTHIK"
# print(n[6])

# n="KARTHIK"
# print(n[-1])

# s="PYTHONPROGRAMMING"
# print(s[0:17])

# s="PYTHONPROGRAMMING"
# print(s[-17:-1])

# s="PYTHONPROGRAMMING"
# print(s[-17:-11:2])

# s="PYTHONPROGRAMMING"
# print(s[6:])

# s="PYTHONPROGRAMMING"
# print(s[:16])

# s="PYTHONPROGRAMMING"
# print(s[-1:])

# s="PYTHONPROGRAMMING"
# print(s[:-12])

# n="KARTHIK"
# n="KARTHIK"+".P"

# M1="PYTHON"
# M2="PROGRAMMING"
# M3=M1+M2
# print(M3)

# s="python"
# print(5*s)

# s="python"
# print(s*5)

# s='python'
# 'programming'
# print(s*5)

# s="karthik"
# print(s.isalpha())

# s="123"
# print(s.isdigit())

# s="karthik123"
# print(s.isalnum())

# s="KARTHIK"
# print(s.isupper())

# s="karthik"
# print(s.islower())

# s="Karthik Paidipaga"
# print(s.startswith("Karthik"))
# print(s.endswith("Paidipaga"))

# while True:
#     n=input()
#     if n.isalpha():
#         print("Alphabets")
#     elif n.isdigit():
#         print("digits")
#     elif n.isalnum():
#         print("both alphabets and digit")
#     elif n.isupper():
#         print("upper")
#     elif n.islower():
#         print("lower")
#     else:
#         print("invalid")

# s="Paidipaga Karthik"
# print(s.find("Karthik"))

# s="Paidipaga Karthik"
# # print(s.find("Karthik",0,10))

# s="Paidipaga Karthik"
# print(s.replace("Karthik","Anil"))

# s="     KARTHIK     "
# print(s)
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# s="karthik paidipaga"
# print(s.split())

# s="welcome to python programming"
# print(s.partition("python"))

# s="welcome to python programming"
# print("-".join(s))

# s="welcome", "to", "python", "programming"
# print("-".join(s))

# s="welcome to python programming"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

#write a program to print all ASCII values and their corresponsding characters.

# for i in range(1,128):
#     print(i,"\t:",chr(i))

# n=input()
# for i in n:
#     print(i,":",ord(i))

# n="logic"
# print(n[::-1])

# s="logic"
# rev=""
# for chr in s:   #l      #o      #g        #i          #c
#     rev=chr+rev #l=l+"" #0l=0+l #gol=g+ol #igol=i+gol #cigol=c+igol
# print(rev)

# s=input()
# temp=s
# rev=""
# for chr in s:  
#     rev=chr+rev 
# if temp==rev:
#     print("palindrome")
# else:
#     print("not a palindrome")

# write a program to get a string from a given string where all occuttences of its first character have been changed to $, except the first character itself.

# n=input()
# fc=n[0]
# for i in range(len(n)):
#     if n[i]==fc.lower() or n[i]==fc.upper():
#         n=n[:i]+"$"+n[i+1:]
# res=fc+n[1:]
# print(res)

# write a python program to add 'ing' at the end of a given string.if the given string already ends with 'ing' then add 'ly'.if the string length is less than 3,leave it unchanged.

# s=input()
# if len(s)>3:
#     if s.endswith("ing"):
#         ns=s+"ly"
#     else:
#         ns=s+"ing"
# else:
#     ns=s
# print(ns)

#write a program that takes a string as input and returns the length of the longest word in it

# s=input()
# words=s.split()
# length=0
# for word in words:
#     if len(word)>length:
#         length=len(word)
# print("length of longest word is",length)

# LIST:

# lst=['K','S','KS',1,4,3,True,False]
# print(lst)
# print(type(lst))

# lst=[11,22,33,[44,55,66],77,88]
# print(lst)

# lst=[11,22,33,[44,55,66],77,88]
# print(lst[0])


# lst=[11,22,33,[44,55,66],77,88]
# print(lst[2])

# lst=[11,22,33,[44,55,66],77,88]
# print(lst[-1])

# lst=[11,22,33,[44,55,66],77,88]
# print(lst[-3])

# s=input()
# count=0
# o=('a','e','i','o','u')
# for i in s:
#     if i in o:
#         count+=1
# print(count)











