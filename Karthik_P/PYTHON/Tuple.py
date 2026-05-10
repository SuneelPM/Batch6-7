# a=input("User name:")
# b=input("Roll no:")
# c=input("branch:")
# tple=(a,b,c)
# print(type(tple))

#2.creation of Tuple

# t1=tuple()
# t2=(10,20,30)
# t3=(10,)
# t4=10,20,30
# print(t1)
# print(t2)
# print(t3)
# print(t4)

#3.Accessing Tuple Elements
#1.Indexing:-

# tpl=(10,20.5,"karthik",True)
# print(tpl[2])
# print(tpl[-1])

#2.slice:-

# tpl=(10,20.5,"karthik",True)
# print(tpl[:3])

# a=(10,20,30,40,50,60,70)
# print(a[1:6])
# print(a[-6:-1])

# a=(10,20,30,40,50,60,70)
# b=len(a)//2
# c=b+1
# print(a[b])
# print(a[c])

#3.Looping in Tuple:-

# a=(10,20,30,40,50,60,70)    #0
# for i in range(len(a)):     #
#     print(i,a[i])

# a=(0,1,2,2,4,5)
# count=0
# for i in range(len(a)):
#     if a[i]==i:
#         print(i,end=" ")
#         count+=1
# print()
# print(count)

# a=(0,1,2,2,4,5)
# for i in range(len(a)):
#     if a[i]==i:
#         print(i,end=" ")
#         break

#4.Tuple operations:-
#1.Concatenation(+):-
# a=(10,20,30,40)
# b=(50,60,70)
# c=a+b
# print(c)

# 2.Repitation(*):-
# a=(10,20,30,40)
# print(a*3)

# Methods in Tuple:-
#1.count()
# tpl=(10,20,30,40,50,60,10,10,30)
# print(tpl.count(10))

#2.Index()
# tpl=(10,20,30,40,50,60,10,10,30)
# print(tpl.index(60))

#5.Unpacking of Tuple(*):-
# tpl=(10,20,30,40,50,60)
# print(tpl)
# print(*tpl)

# emp=("karthik","12134","IT","TCS","500000")
# name,id,sector,company,salary=emp
# print("name:",name)
# print("id:",id)
# print("sector:",sector)
# print("company:",company)
# print("salary:",salary)

#Nested Tuple:-

# a=(10,20,(30,40,50,50),50,60)
# print(a[1])
# print(a[2][1])

# students=(("nagarjuna",10,(10,20,30)),
#           ("karthik",20,(20,30,40)),
#           ("krishna",30,(30,40,50)))
# for student in students:
#     Name,RollNo,scores=student
#     # print(Name,RollNo,scores)
#     eng=scores[2]
#     avg=scores[0]+scores[1]+scores[2]//3
#     print("Name:",Name,"English:",eng,"Average:",avg)

# *a,b=10,20,30,40,50
# print(a)
# print(b)

# ComName,*Batches,Domain="Logic",1,2,3,4,5,6,"Software Training"
# print(ComName)
# print(Batches)
# print(Domain)

#_:-

# emp=("karthik","12134","IT","TCS","500000")
# name,_,sector,_,salary=emp
# print("name:",name)
# # print("id:",id)
# print("sector:",sector)
# # print("company:",company)
# print("salary:",salary)

#Zip():-
# tple1=("Python","JAva","C","React")
# tple2=("Back End","SEcurity","First Languag","Front End")
# Result=tuple((zip(tple1,tple2)))
# print(Result)

# plyrs=["Virat","Rohit"]
# jrsy=[18,45]
# tm=tuple(zip(plyrs,jrsy))
# print(type(tm))
# print(tm)

#Tuple Comprehsension:-

# a=(10,20,7,40,50,60)
# Result=tuple(i for i in a if i%2==0)
# print(Result)

# a=(10,20,7,40,50,60)
# Result=tuple(i**2 for i in a)
# print(Result)

# a=(10,20,7,40,50,60,3,5,7)
# Result=tuple(i for i in a if i%2==1)
# print(Result)

# a=("pushpa","animal","kgf")
# Result=tuple(movie.upper()for movie in a)
# print(Result)


# lst=[]
# for i in range(3):
#     print("enter student details:")
#     std=input()
#     roll=int(input())
#     lst.append((std,roll))
# print(lst)

# lst=[]
# for i in range(3):
#     print("enter student details:")
#     std=input()
#     roll=int(input())
#     lst.append((std,roll))
# print(tuple(lst))








  











