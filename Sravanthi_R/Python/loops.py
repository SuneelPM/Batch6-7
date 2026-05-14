# s_num = int(input())
# if s_num % 8 == 1:
#     print("Lower")
# elif s_num % 8 == 4:
#     print("Lower")
# elif s_num % 8 == 2:
#     print("Middle")
# elif s_num % 8 == 5:
#     print("Middle")
# elif s_num % 8 == 3:
#     print("Upper")
# elif s_num % 8 == 6:
#     print("Upper")
# elif s_num % 8 == 7:
#     print("S.lower")
# else:
#     print("S.upper")
 

# s_num=int(input())
# if s_num%8==1 or s_num%8==4:
#     print("lower")
# elif s_num%8==2 or s_num%8==5:
#     print("middle")
# elif s_num%8==3 or s_num%8==6:    
#     print("upper")
# elif s_num%8==7:
#     print("S.lower")
# else:
#     print("S.upper")

# s_num=int(input())
# if s_num>=1 and s_num<=80:
#   if s_num%8==1 or s_num%8==4:
#     print("lower")
#   elif s_num%8==2 or s_num%8==5:
#     print("middle")
#   elif s_num%8==3 or s_num%8==6:    
#     print("upper")
#   elif s_num%8==7:
#     print("S.lower")
#   else:
#     print("S.upper")
# else:
#     print("invalid")


              #LOOPS#

# for i in range(5):
#     print(i,end="")

# for i in range(10,16):
#     print(i,end="")

# for i in range(20,30,2):
#     print(i,end="")

# for i in range(22,11,-4):
#     print(i,end="")



# for i in range(1,15,2):
#     print(i,end=" ")

# for i in range(15):
#  if i%2!=0:
#     print(i,end=" ")

s=int(input())
e=int(input())
count=0
for i in range(s,e):
 if i%2==0:
    print(i,end=" ")
    count=count+1
print()
print(count)


# s_num = int(input())
# if s_num % 8 == 1:
#     print("Lower")
# elif s_num % 8 == 4:
#     print("Lower")
# elif s_num % 8 == 2:
#     print("Middle")
# elif s_num % 8 == 5:
#     print("Middle")
# elif s_num % 8 == 3:
#     print("Upper")
# elif s_num % 8 == 6:
#     print("Upper")
# elif s_num % 8 == 7:
#     print("S.lower")
# else:
#     print("S.upper")
 

# s_num=int(input())
# if s_num%8==1 or s_num%8==4:
#     print("lower")
# elif s_num%8==2 or s_num%8==5:
#     print("middle")
# elif s_num%8==3 or s_num%8==6:    
#     print("upper")
# elif s_num%8==7:
#     print("S.lower")
# else:
#     print("S.upper")

# s_num=int(input())
# if s_num>=1 and s_num<=80:
#   if s_num%8==1 or s_num%8==4:
#     print("lower")
#   elif s_num%8==2 or s_num%8==5:
#     print("middle")
#   elif s_num%8==3 or s_num%8==6:    
#     print("upper")
#   elif s_num%8==7:
#     print("S.lower")
#   else:
#     print("S.upper")
# else:
#     print("invalid")


              #LOOPS#

# for i in range(5):
#     print(i,end="")

# for i in range(10,16):
#     print(i,end="")

# for i in range(20,30,2):
#     print(i,end="")

# for i in range(22,11,-4):
#     print(i,end="")



# for i in range(1,15,2):
#     print(i,end=" ")

# for i in range(15):
#  if i%2!=0:
#     print(i,end=" ")

# x=int(input())
# y=int(input())
# count=0
# for i in range(x,y+1):
#  if i%2==0:
#     print(i,end=" ")
#     count=count+1
# print()
# print(count)

bal=int(input())
for i in range(bal):
    amt=int(input())
    if amt%100!=0:
        print("invalid amount")
    elif amt>bal:
        print("insufficient balance")
    else:
        bal=amt
        print("transction succesfully")
        print(bal)