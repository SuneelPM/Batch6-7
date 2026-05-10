#1.Remove duplicates without changing order
# lst = [1,2,3,2,4,1,5]
# result = []
# for item in lst:
#     if item not in result:
#         result.append(item)
# print(result)

#2.Find the second largest number (no sorting)
# lst = [10, 5, 20, 8, 15]
# largest = lst[0]
# second_largest = lst[0]
# for num in lst:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
# print(second_largest)

#3.Rotate a list to the right by k positions
# lst = [1, 2, 3, 4, 5]
# k = 2
# k = k % len(lst)
# rotated = lst[-k:] + lst[:-k]
# print(rotated)

#4.Find common elements between two lists
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common = []
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)
# print(common)

#5.Separate even and odd numbers
# lst = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
# for num in lst:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Even:", even)
# print("Odd:", odd)

#1.Count occurrences of an element
# tup = (1, 2, 3, 2, 4, 2)
# element = 2
# count = 0
# for item in tup:
#     if item == element:
#         count += 1
# print(count)

#2.Largest and smallest (no max/min)

# tup = (10, 5, 20, 3, 15)
# largest = smallest = tup[0]
# for num in tup:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("Largest:", largest)
# print("Smallest:", smallest)

# 3. Remove an element from a tuple

# tup = (1, 2, 3, 4, 2)
# remove_element = 2
# new_tup = tuple(item for item in tup if item != remove_element)
# print(new_tup)

# 4. Sort a tuple and return as tuple

# tup = (4, 1, 3, 2)
# sorted_list = list(tup)
# for i in range(len(sorted_list)):
#     for j in range(i + 1, len(sorted_list)):
#         if sorted_list[i] > sorted_list[j]:
#             sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]
# sorted_tup = tuple(sorted_list)
# print(sorted_tup)

# 5. Find all pairs with sum = k
# tup = (1, 2, 3, 4, 5)
# k = 6
# pairs = []
# for i in range(len(tup)):
#     for j in range(i + 1, len(tup)):
#         if tup[i] + tup[j] == k:
#             pairs.append((tup[i], tup[j]))
# print(pairs)

# Function to store personal information
# def personal_info(name, age, account_number):
#     return {
#         "Name": name,
#         "Age": age,
#         "Account Number": account_number
#     }
# # Function to check balance
# def check_balance(balance):
#     return balance
# # Function to withdraw money
# def withdraw(balance, amount):
#     if amount <= 0:
#         print("Invalid withdrawal amount.")
#     elif amount > balance:
#         print("Insufficient balance.")
#     else:
        
#         balance -= amount
#         print(f"Withdrawal successful. New balance: ₹{balance}")
#     return balance
# # Function to deposit money
# def deposit(balance, amount):
#     if amount <= 0:
#         print("Invalid deposit amount.")
#     else:
#         balance += amount
#         print(f"Deposit successful. New balance: ₹{balance}")
#     return balance
# # -------- Main Program --------
# balance = 20000
# info = personal_info("Karthik", 21, "ACC1001")
# print("\nPersonal Information:")
# for key, value in info.items():
#     print(f"{key}: {value}")
# print("\nCurrent Balance:", check_balance(balance))
# balance = withdraw(balance,2500)
# balance = deposit(balance,4000)
# print("\nFinal Balance:", check_balance(balance))



#Practice--------------------------------------------------------------------------------------------------------------------------
# a=10
# b="karthik"
# print(type(a))
# print(type(b))

# a="100"
# sum=int(a)
# print(type(sum))

# b="200"
# num=str(b)
# print(type(num))

# a,b,c=10,20,30
# sum=a+b+c
# print("sum of 3 numbers:",sum)

# a=10
# b=20
# a,b=b,a
# print("a=",a)
# print("b=",b)

# p=int(input())
# t=int(input())
# r=int(input())
# s=(p*t*r)/100
# print("simple interst:",s)

# m=int(input())
# i=int(input())
# if m>=90 and m<=100:
#     if i<200000:
#         print("FULL+BONUS")
#     else:
#         print("FULL")
# elif m>=75 and m<90:
#     if i<200000:
#         print("FULL")
#     else:
#         print("HALF")
# elif m<75:
#     if i<20000:
#         print("HALF")
#     else:
#         print("NO SCHOLARSHIP")
# else:
#     print("INVALID")

# s="karthik123"
# print(s.isalpha())
# print(s.isdigit())
# print(s.isupper())
# print(s.islower())
# print(s.isalnum())
# print(s.startswith())
# print(s.endswith())



# s=input()
# alph=""
# num=""
# for i in s:
#     if i.isalpha():
#         alph+=i
#     elif i.isdigit():
#         num+=i
# print(alph)
# print(num)

s=input()
ow=""
con=""
owel=['a','e','i','o','u']
for i in s:
    if s==owel:
        print()
    else:
        
        


