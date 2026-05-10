                            # single prime number(with single value)
# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not a prime  number")


                #  All prime number(with multiple numbers)
n=int(input())
for i in range(1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,"prime number")
    else:
        print(i,"not a prime  number")