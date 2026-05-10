                 #nested list 
# lst=[11,22,33,[44,55,66,77],88,99]
# print(lst[3][1])
                 
                 #insert method
# lst=[11,22,33,[44,55,66,77],88,99]
# lst.insert(3,50)
# print(lst)
# lst.insert(-2,"sravss")
# print(lst)
                 
                 #extend method
# lst1=[11,22,33,44,55,66]
# lst2=[10,20,30,40,50,60]
# lst1.extend(lst2)
# print(lst1)

                 #remove method &pop method
# lst=[11,33,22,44,55,77,66]
# lst.remove(44)
# print(lst)

# lst=[11,33,22,44,55,77,66]
# lst.pop()
# print(lst)

# lst=[11,33,22,44,55,77,66]
# print(lst.pop(3))
# print(lst)

# lst=[11,33,22,44,55,77,66]
# lst.clear()
# print(lst)

                 #ittarable
# lst=[10,20,30,40,50,60]
# lst[1:4]="s"
# print(lst)

                 #sort()
# v=[44,22,11,55,33]
# print(v)
# v.sort()
# print(v)

                  #reverse
# k=[11,22,33,44,55,66]
# print(k)
# k.reverse()
# print(k)
        
                  #copy
# lst1=[11,22,33,44,55,66,77,88]
# lst2=lst1
# print(lst2)
# lst3=lst1.copy()
# print(lst3)

# s=[11,22,33,44,55,66,77,88]
# f=s
# print(id(s))
# print(id(f))
# print(f.pop())
# print(s)
                   
                   #cloning lists
# s=[11,22,33,44,55,66,77,88]
# f=s[:]
# print(id(s))
# print(id(f))
# print(f.pop())
# print(s)
# print(f)

                  #list looping
# lst=[11,12,13,14,15,16,17]
# for i in lst:
#     print(i,end=" ")

# lst=[11,12,13,14,15,16,17]
# i=0
# while i<len(lst):
#     print(lst[i],end=" ")
#     i+=1
                # using enumerate method
# lst=[11,12,13,14,15,16,17]
# for i,j in enumerate(lst):
#     print(i,j)

                # using range method
# lst=[11,12,13,14,15,16,17]
# for i in range(len(lst)):
#     print(lst[i],end=" ")

                 #list comprension
# lst=[11,22,33,44,55,66,77]
# lst2=[i for i in lst]
# print(lst2)

# lst=[11,22,33,44,55,66,77]
# lst2=[i for i in lst if i%2==0]
# print(lst2)

lst=[11,22,33,44,55,66,77]
d_lst=[i** 2 for i in lst]
print(d_lst)

# lst=[10,20,30,30,50,20,70]
# u=[]
# for i in lst:
#     if i not in u:
#         u.append(i)
# print(lst)
# print(u)

# num = [10, -5, 20, -15, 0, 30, -2]
# p = []
# n = []
# for i in num:
#     if i > 0:
#         p.append(i)
#     elif i < 0:
#         n.append(i)
# print(p)
# print(n)

# num=int(input())
# lst=[]
# for ele in range(num):
#     n=int(input())
#     lst.append(n)
# print(lst)   
# pst=[]
# ngt=[]
# for ele in lst:
#     if ele>0:
#         pst.append(ele)
#     elif ele<0:
#         ngt.append(ele)
# print(pst)
# print(ngt)


