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

# lst=[10,20,30,40,50,60]
# print(lst[1:5])

# lst=[10,20,30,40,50,60]
# print(lst[-5:-1])

# lst=[10,20,30,40,50,60]
# print(lst[-2:-6:-1])

# lst=[10,20,30,40,50,60]
# print(lst[4:0:-1])

# lst1=[10,20,30]
# lst2=[40,50,60]
# lst=lst1+lst2
# print(lst)

# lst1=[10,20,30] 
# print(lst1*2)

# lst=[10,20,30,40,50]
# lst[3]="karthik"
# print(lst)

# lst=[10,20,30,40,50,60,70,80,90,100]
# print(max(lst))
# print(min(lst))
# print(len(lst))
# print(sum(lst))
# print(any(lst))
# print(all(lst))
# # print(del(lst))
# print(list(reversed(lst)))
# print(sorted(lst))

# lst=[10,30,40,59]
# lst.append(90)
# print(lst)

# lst=[]
# for i in range(5):
#     n=input()
#     lst.append(n)
# print(lst)

# lst=[10,10,20,30,40,50]
# print(lst.count(10))
# print(lst.index(10))

# lst=[10,20,30,20,30,20,50]
# srch=20
# if srch in lst:
#     if lst.count(srch)==1:
#         print(lst.index(srch))
#     else:
#         for i in range(len(lst)):
#             if lst[i]==srch:
#                 print(i ,end=" ")
# else:
#     print(srch,"element not found")

# lst=[10,20,30,[40,50,60],70,80]
# print(lst[3][0])
# print(lst[3][1])
# print(lst[3][2])

# lst=[10,20,30,[40,50,60],70,80]
# lst.insert(3,50)
# lst.insert(-2,100)
# print(lst)

# lst=[10,20,30,[40,50,60],70,80]
# lst2=["karthik","sindhu","Aadhya"]
# lst.extend(lst2)
# print(lst)

# lst=[10,20,30,40,50,60]
# lst.remove(40)
# print(lst)

# lst=[10,20,30,40,50,60]
# print(lst.pop(4))

# lst=[10,20,30,40,50,60]
# lst.clear()
# print(lst)

# lst=[10,20,30,40,50,60]
# lst[1:4]="karthik"
# print(lst)

# lst=[50,30,20,60,10]
# lst.sort()
# print(lst)

# lst=[10,20,30,40,50,60]
# lst.reverse()
# print(lst)

# lst=[10,20,30,40,50,60]
# lst.copy()
# print(lst)

# lst=[50,30,20,60,10]
# for i in lst:
#     print(i,end=" ")

# lst=[50,30,20,60,10]
# index=0
# while index < len(lst):
#     print(lst[index],end=" ")
#     index+=1

# lst=[10,20,30,40,50,60]
# for i,j in enumerate(lst):
#     print(i,j,end=" | ")

# lst=[10,20,30,40,50,60]
# for i in range(len(lst)):
#     print(lst[i],end=" ")

# lst=[10,20,30,3,5,7,40,50,60]
# lst2=[i for i in lst if i%2==0]
# print(lst2)

# lst=[1,2,3,4,5]
# dbl_lst=[i ** 2 for i in lst]
# print(dbl_lst)

# lst=[10,20,30,10,20,30,50]
# unq_ele=[]
# for ele in lst:
#     if ele not in unq_ele:
#         unq_ele.append(ele)
# print("Original list:",lst)
# print("Unique elements:",unq_ele)

# n=int(input())
# lst=[]
# for i in range(n):
#     ele=int(input())
#     lst.append(ele)
# print("Original list",ele)

# pstv_lst=[]
# ngtv_lst=[]
# for ele in lst:
#     if lst>0:
#         pstv_lst.append(ele)
#     elif lst<0:
#         ngtv_lst.append(ele)
# print("Positive list:",pstv_lst)
# print("Negative list:",ngtv_lst)

# a=input("User name:")
# b=input("Roll no:")
# c=input("branch:")
# tple=(a,b,c)
# print(type(tple))


