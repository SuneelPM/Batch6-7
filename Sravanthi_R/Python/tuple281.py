                  #Nested tuples
# a=(10,20,(30,40,50,60,),70,80)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[2][0])
# print(a[2][1])
# print(a[2][2])
# print(a[2][3])

# ts=(
    # ("sravss",73,(10,20,30)),
    # ("suji",81,(20,10,30)),
    # ("praggu",92,(30,20,10))
#     )
# for student in ts:
#     name,roll,score=student
#     english=score[2]
#     avg=score[0]+score[1]+score[2]//3
#     print("Name",name,"english",english,"avg",avg)
    
#packing in tuple

# *a,b=10,20,30,40,50,60,70,80
# print(a)
# print(b)

# a,*b=10,20,30,40,50,60,70,80
# print(a)
# print(b)

# comname,*batches,domain="logic",1,2,3,4,"sf training"
# print(comname)
# print(batches)
# print(domain)

#Zip()

# tpl=("sravss","suji","firoze","praggu")
# tpl2=("fire","introvert","patience","ego")
# rslt=tuple((zip(tpl,tpl2)))
# print(rslt)

#Zip with looping

# tpl=("sravss","suji","firoze","praggu")
# tpl2=("fire","introvert","patience","adjust")
# for i in zip(tpl1,tpl2):
#     print(i)

#zip without looping
# actrs=["mahesh","sai pallavi","ram"]
# num=[1,2,3]
# tm=tuple(zip(actrs,num))
# print(tm)
# print(type(tm))

           #Tuple comprehension
# tpl=(10,20,30,40,50)
# rslt=tuple(i for i in tpl)
# print(rslt)

           #odd number & even nunbers
# tpl=(20,37,26,57,99)
# rslt=tuple(i for i in tpl if i%2==1)
# print(rslt)
 
# mvs=("amaran","fida","guntur karam")
# res=tuple(movie.upper() for movie in mvs)
# print(res)

# n=int(input())
# students=[(input("name:"),int(input("marks:")))for i in range(n)]
# print(students)

#type 1:

# lst=[]
# n=int(input())
# for i in range(n):
#     lst.append((input("name: "),int(input("marks: "))))
#     tpl=tuple(i for i in lst)
# print(tpl)

#type 2:

# lst=[]
# for i in range(3):
#     print("Enter student details")
#     std=input()
#     roll=int(input())
#     lst.append((std,roll))
# print(lst)







