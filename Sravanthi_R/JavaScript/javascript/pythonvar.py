# num=int(input())
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial is:",fact)

# num=int(input())
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10*digit
#     num=num//10
# print("reversed number:",rev)

                        # 05/05/2026
# if True:
#     print("this is a true statement")
# else:
#     print("this ia a false statement")

# a=int(input())
# if a>18:
#     print("yor are eligible for vote")
# else:
#     print("yor are not eligible for vote")

# marks = int(input("Enter marks: "))

# if marks >= 90 and marks <= 100:
#     print("Grade A")

# elif marks >= 80 and marks < 90:
#     print("Grade B")

# elif marks >= 70 and marks < 80:
#     print("Grade C")

# elif marks >= 40 and marks < 70:
#     print("Grade D")

# elif marks >= 0 and marks < 40:
#     print("Grade F")

# else:
#     print("Invalid marks")

# nums = []
# for i in range(5):
#     value = int(input("Enter value: "))
#     nums.append(value)
# print(nums)

# s=[20,20,40,50,10,2]
# print(max(s))
# print(min(s))

# lst=[10,20,30,40,50]
# s=lst.copy()
# print(s)
# s[1]="S"
# print(s)
# print(lst)

# k=[10,20,30,40,50]
# s=k
# s[1]="A"
# print(s)
# print(k)

# s=[10,20,30,40,50]
# for i in range(len(s)):
#     print(s[i],end=",")


# s = [10,20,30,40,50]
# i = 0
# while i < len(s):
#     print(s[i], end=",")
#     i += 1

# for i in range(128):
#     print(i, "=", chr(i))


# s = [7,8,3,5,4,9]
# big =s[0]
# small = s[0]
# for i in s:
#     if i > big:
#         big = i
#     elif i < small:
#         small = i
# print("Max =", big)
# print("Min =", small)

# s = [10,20,60,70,90,40,50]
# for i,j in enumerate(s):
#     print(i,"->",j)


# s=[10,20,10,20,30,30,40,50]
# result = []
# for i in s:
#     if i not in result:
#         result.append(i)
# print(result)

# s=[10,-2,40,-5,20,-10,-20]
# positive = []
# negative = []
# for i in s:
#     if i >= 0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print("Positive:", positive)
# print("Negative:", negative)

# s=[10,20,30,40,50,60]
# # Left Shift by 2 positions
# left_shift = s[2:] + s[:2]
# print(left_shift)
# # Right Shift by 2 positions
# right_shift = s[-2:] + s[:-2]
# print(right_shift)

# num = 783549
# dgt = [int(i) for i in str(num)]
# max_v = max(dgt)
# min_v = min(dgt)
# print(max_v)
# print(min_v)


# num = 783549
# min_d = 9
# max_d = 0
# for digit in str(num):
#     if int(digit) > max_d:
#         max_d = int(digit)
#     if int(digit) < min_d:
#         min_d = int(digit)
# print(max_d)
# print(min_d)


# Tuple unpacking using user input

a, b, c = input("Enter 3 values: ").split()
print(a)
print(b)
print(c)

name,detailes="logic","develoer","logicwhile",50000
