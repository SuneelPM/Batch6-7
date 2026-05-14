#Declaration
# s={}
# print(type(s))
# set=set()
# print(type(s))
# s3={1,2,3}
# print(s3)
# print(type(s3))

# s=set([10,20,30,40])
# print(s)

# s={1,2,3,2,4,"logic",6}
# print(s)

           #accessing elments
# s={10,20,30,40,50}
# for i in s:
#     print(i,end=" ")

# s={"sravss","suji","praggu"}
# for i in s:
#     print(i,end=" ")
          
                #Methods in sets
# s={10,20,30,40,50}
# s.add(80)
# print(s)
# s.add(90)
# print(s)
              #Inempty set we can print the valus
    #1type:

# s=set()
# s.add(10)
# print(s)
# s.add(30)
# print(s)

    #2tye:

# s=set()
# s.update([10,20,30,40,50])
# print(s)

    #3type:
# s=set()
# for i in range(5):
#     n=input()
#     s.add(n)
# print(s)

# s1={40,50,60,70}
# s1.update([10,20,30])
# print(s1)
# s2={"S","F","S"}
# s1.update(s2)
# print(s1)

#Remove

# s1={40,50,60,70,80,90}
# s1.remove(50)
# print(s1)

#discard
# s1={10,20,30,40,50,60,70}
# s1.discard(40)
# print(s1)

#pop
# s1={10,20,30,40,50,60}
# print(s1.pop())
# print(s1)
# print(s1.pop())
# print(s1)

#clear
# s1={10,20,30,40,50}
# s1.clear()
# print(s1)

#copy
# s={10,20,30}
# ns=s.copy()
# print(ns)

#union
# s1={10,20,30,40,50,60}
# s2={70,80,90,100}
# s3=s1.union(s2)
# print(s3)

#intersection
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s3=s1.intersection(s2)
# print(s3)

#difference
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s3=s1.difference(s2)
# print(s3)

#symmetric difference
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s3=(s1^s2)
# print(s3)

#intersectoion update
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s1.intersection_update(s2)
# print(s1)


#difference update
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s1.difference_update(s2)
# print(s1)


#symmetric difference update

# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s1.symmetric_difference_update(s2)
# print(s1)

#issubset
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s1.issubset(s2)
# print(s1)


#issuperset
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s1.issuperset(s2)
# print(s1)


#isdisjoint
# s1={10,20,30,40,50,60}
# s2={20,30,50,80}
# s1.isdisjoint(s2)
# print(s1)


# frozen set

# a=frozenset([10,20,30,40,50,20])
# print(a)
# a.add(20)
# print(a)

# set comprehension

# sc={i for i in range(1,11)}
# print(sc)

# even & odd
# sc={11,22,33,44,55,66}
# rslt=set(i for i in sc if i%2==1)
# print(rslt)

# unique values 
# str="python programming"
# sc={i for i in str}
# print(sc)



