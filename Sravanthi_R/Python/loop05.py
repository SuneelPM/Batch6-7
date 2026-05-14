# n=int(input())
# sum=0
# evn_cnt=0
# odd_cnt=0
# for i in range(1,n+1):
#     sum=sum+i
#     if i%2==0:
#         print(i,end=" ")
#         evn_cnt+=1
#     else:
#         odd_cnt+=1
# print()
# print(sum)
# print(evn_cnt)
# print(odd_cnt)

# num=input()
# count=0
# for i in num:
#     count+=1
# print(count)

# num=input()
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum)


# i=0
# while i<5:
#     print("while loop")
#     i=i+1

# battery=int(input())
# while battery>0:
#     print("battery percentage:",battery)
#     battery=battery-10
# print("phone switched off")

n=int(input())
rev=0
while n!=0:
    print("reverse number",n)
    dig=n%10
    rev=rev*10+dig
    n=n//10
print(rev)