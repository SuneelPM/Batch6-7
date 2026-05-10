#Declaration:-
# s={}
# print(type(s))
# set=set()
# print(type(set))

# s={1,2,2,3,4,5,5,"karthik",6}
# print(s)

# s=set([10,20,30,40,50])
# print(s)

#Accessing elements:-
# s={10,20,30,40,50}
# for i in s:
#     print(i,end=" ")

# s={"karthik",10,20,"nagarjuna",30,40,"krishna",50,60}
# for i in s:
#     print(i,end=" ")

#Methods in sets:-
# s={10,20,30,40,50}
# s.add(80)
# print(s)
# s.add(90)
# print(s)

# s=set():-
# for i in range(5):
#     n=int(input())
#     s.add(n)
# print(s)

#Update:-
# s={10,20,30,40}
# s.update([50,60,70])
# print(s)

# s1={10,20,30,40}
# s2={"karthik","nagarjuna","krishna"}
# s1.update(s2)
# print(s1)

#Remove:-
# s1={4,543,34,232333,3,4,43445,455,5}
# (s1.remove(4))
# print(s1)

#Discard:-
# s={10,20,30,40,50}
# (s.discard(70))
# print(s)
# s.discard(100)
# print(s)

#pop():-
# s={10,20,30,40,50}
# print(s.pop())
# print(s)

#clear:-
# s={10,20,30,40,50}
# s.clear()
# print(s)

#Copy:-
# s={10,20,30,40,50}
# new_set=s.copy()
# print(new_set)

#Operations:-
#Union:-
# s1={10,20,30,40}
# s2={50,60,70,80}
# s3=s1.union(s2)
# print(s3)

#Intersection:-
# s1={10,20,30,40}
# s2={50,60,70,10,20,30,80}
# s3=s1.intersection(s2)
# print(s3)

#Difference:-
# s1={10,20,30,40}
# s2={50,60,70,80}
# s3=s1.difference(s2)
# print(s3)

#Symmetric_difference:-
# s1={10,20,30,40}
# s2={50,60,70,80}
# s3=s1.symmetric_difference(s2)
# print(s3)

#intersection_update:-
# s1={10,20,30,40}
# s2={50,60,70,10,20,30,80}
# s3=s1.intersection_update(s2)
# print(s3)

# a=frozenset([10,20,40,50,20,10])
# print(a)

#Set Comprehsension:-
# set_comp={i for i in range(1,11)}
# print(set_comp)

# a={1,2,3,4,5,1,2,3}
# set_comp={i for i in a}
# print(set_comp)


















