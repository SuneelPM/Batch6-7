# a={}
# print(type(a))
# dic2={10:20,20:30}
# print(type(dic2))
# dic3=dic()
# print(type(dic3))

# dic={"name":"logic",20:225}
# print(dic)

         #unique
# data={"sravss":73,"sravss":84}
# print(data)

# data={"sravss":73,"suji":73}
# print(data)

# data={"name":"sravss","roll":73,"branch":"cseaids"}
# print(data)

        #dic operation with list

# data={"name":"sravss","roll":73,"branch":"cseaids"}
# print(data["branch"])
# data["branch"]="aids"
# print(data)

# dic={1:"sravss",2:"suji",3:"praggu"}
# print(dic)
# print(dic[1])

        #dic operation with tuple
# dic={(0,1):"sravss",(0,2):"suji",(0,3):"praggu"}
# print(dic)

# dic={(0,1):(1,1),(0,2):(2,2),(0,3):(3,3)}
# print(dic)

         #Dictionary methods
# dic={(0,1):"sravss",(0,2):"suji",(0,3):"praggu"}
# print(dic.keys())

# print(dic.values())

# print(dic.items())

# print(dic.get((0,1)))

# print(dic.update({"firoze":(0,4),"raj":(0,5)}))
# print(dic)

# print(dic.update({(0,5):(0,3)}))
# print(dic)

# print(dic.update(s=73,f=78))
# print(dic)

# print(dic.setdefault((0,4),"chamu"))
# print(dic)

# del dic[(0,1)]
# print(dic)

# dic.pop((0,1))
# print(dic)

# dic.popitem()
# print(dic)

# dic.clear()
# print(dic)

# del dic



                         # set  looping
#keys
# d={"s":73,"f":786,"p":23}
# print(d.keys())
# for i in d.keys():
#         print(i,end=" ")

#values
# d={"s":73,"f":786,"p":23}
# print((d.values()))
# for i in d.values():
#         print(i,end=" ")

#items
# d={"s":73,"f":786,"p":23}
# print((d.items()))
# for i in d.items():
#         print(i,end=" ")

#In empty dic we can give the 3 students details
# dic={}
# for i in range(3):
#    print("enter student details") 
#    stu=input()  
#    roll=int(input())
#    dic[roll]=stu
# print(dic)

#nested dictionaries
# d={"s":73,"f":78,"p":87,"d":{"a":1,"v":7},"r":22}
# print(d)

# d={"73":{"name":"sravss","roll":73786},
#    "43":{"name":"suji","roll":12345}}
# print(d["73"]["name"])
# print(d["73"]["roll"])
# print(d.update({"44":{"name":"praga","roll":9876}}))
# print(d)
 
#nested looping
# dic={}
# for i in range(3):
#    print("enter student details",i)
#    id=input()
#    name=input()  
#    roll=int(input())
#    dic[id]={name,roll}
# print(dic)

       #dictionary comprehensiom
# d={i:i**2 for i in range(1,8)}
# print(d)

#even&odd
# d={i:i**2 for i in range(1,8) if i%2==1}
# print(d)

#In comprehension how to add two lists
# lst1=[10,20,30,40,50]
# lst2=["s","r","a","v","s"]
# dic={lst1[i]:lst2[i] for i in range(len(lst1))}
# print(dic)

# d={10:"h",20:"a"}
# dic=d.fromkeys(d,"H")
# print(dic)

     #Dictionary functions
# d={"s":73,"r":75,"a":76,"v":77}
# print(max(d))
# print(min(d))
# print(len(d))
# print(sorted(d))
# d={73:"s",74:"r",75:"a",76:"v"}
# print(sum(d))