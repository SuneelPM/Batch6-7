# x=int(input())
# y=int(input())
# count=0
# if x>y:
#     x,y=y,x
# for i in range(x,y+1):
#   if i%2==0:
#      print(i,end=" ")
#      count=count+1
# print()
# print(count)

# n=int(input())
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)

# f=int(input())
# sum=0
# for i in range(f):
#     num=int(input())
#     sum=sum+num
# print(sum)
# avg=sum/f
# print(avg)



# for i in "sravanthi":
#  print(i,end=" ")
 

# name=input()
# for i in name:
#     print(i,end=' ')

s=int(input())
e=int(input())
x=int(input())
y=int(input())
for i in range(s,e+1):
    if i%x==0 and i%y==0:
        print(i,end=" ")
   