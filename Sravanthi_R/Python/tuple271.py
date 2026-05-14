                             # syntax:
# tuple=(10,20,40,20.5,"SS",True)
# print(tuple)
# print(type(tuple))


# name=input()
# r_n=int(input())
# bra=input()
# tuple=(name,r_n,bra)
# print(tuple)
# print(type(tuple))

                             #1.creastion of tuple
# a=tuple()
# b=(10,20,30)
# c=(10,)
# d=10,20,30
# print(a)
# print(b)
# print(d)
# print(type(c))
                          #2.creation of tuple
# a=tuple([10,20,30])
# print(a)

                         #3.Accessing tuple
   #1.indexing
# tpl=(73,"sravs",73.5,True)
# print(tpl[1])
# print(tpl[-2])
               
   #2.slice operation
# tpl=[10,20,30,40,50,60,70]
# print(tpl[1:6])
# print(tpl[-2:-7:-1])
      # how to take middle value without uisn index values
# tpl=[10,20,30,40,50,60,70]            
# i=len(tpl)//2
# print(tpl[i])

                         #4.looping in tuple
# tpl=(10,20,30,40,50)
# for i in tpl:
#      print(i,end=" ")

     #index values and tuple values
# tpl=(10,20,30,40,50)
# for i in range(len(tpl)):
#      print(i,":",tpl[i])

     #index numbering and same variable values print
# tpl=(0,1,2,2,3,4,5,6,7)
# c=0
# for i in range(len(tpl)):
#     if tpl[i]==i:
#         c=c+1
# print(c)

              #with using break
# tpl=(0,1,2,2,3,4,5,6,7)
# for i in range(len(tpl)):
#     if tpl[i]==i:
#      print(i)
#      break

                 #5.tuple operation
    #concatenate operator(+)
# tpl=(10,20,30,40,50)
# tpl2=(60,70,80)
# tpl3=tpl+tpl2
# print(tpl3)
    #repeation operation(*)
# tpl=2,3,4,5
# print(tpl*3)

                #6.methods in tuple
  #count()
# tpl=1,2,3,2,3,4,1,4
# print(tpl.count(1))
  #index()
# tpl=1,2,3,2,3,4,1,4
# print(tpl.index(1))

                #Unpacking of tuple done by (*)
# tpl=(10,20,30,40,50)
# print(tpl)
# print(*tpl)

# emp=("sravss","73143","IT","wiproo","100000")
# name,id,sector,company,salary=emp
# print("name:",name)
# print("id:",id)
# print("sector:",sector)
# print("company:",company)
# print("salary:",salary)


