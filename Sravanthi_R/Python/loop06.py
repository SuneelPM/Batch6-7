# num=int(input())
# temp=num
# rev=0
# while num!=0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if rev==temp:
#         print("palimdrom number")
# else:
#         print("not palindrom number")



# num=int(input())                            
# if num<0:                                  
#     print("positive number")
# else:
#     temp=num
#     rev=0
#     while num!=0:
#       digit=num%10
#       rev=rev*10+digit
#       num=num//10
#     if rev==temp:
#         print("palimdrom number")
#     else:
#         print("not palindrom number")  


# num=int(input())
# sum=0
# i=1
# while num>i:
#     if num%i==0:
#         sum+=i
#     i+=1
# if sum==num:
#      print("perfect number")
# else:
#     print("not perfect number")   


# num=int(input())
# check=0
# for i in range(2,num):
#    if num%i==0:
#       check=1
# if check==0:
#      print("prime num")
# else:
#      print("not prime")


# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print("factorial:",fact)

n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c