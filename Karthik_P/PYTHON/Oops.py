# class One:
#     def first(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
# s1=One()
# s1.first(10,20)
# s2=One()
# s2.first(30,40)

# class One:
#     def first(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
#     def second(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a-self.b)
#     def thrid(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a*self.b)
#     def fourth(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a/self.b)
# s=One()
# s.first(10,20)
# s.second(20,30)
# s.thrid(30,40)
# s.fourth(40,50)

# class Car():
#     name=""
#     colour=""
#     model=""
#     def start(self,name,colour,model):
#         self.name=name
#         self.colour=colour
#         self.model=model
#         print("name:",self.name,"color:",self.colour,"model:",self.model,"Starting")
#     def stop(self):
#         print("Stoping")
# c1=Car()
# c1.start("Benz","Black","V8")
# c2=Car()
# c2.start("Fortuner","Red","V9")

# class Car():
#     Company="TATA"
#     def start(self,name,colour,model):
#         self.name=name
#         self.colour=colour
#         self.model=model
#         print("name:",self.name,"color:",self.colour,"model:",self.model,Car().Company,"Starting")
#     def stop(self):
#         print("Stoping")
# c1=Car()
# c1.start("Benz","Black","V8")
# c2=Car()
# c2.start("Fortuner","Red","V9")

# class Car():
#     Company="TATA"
#     def __init__(self,name,colour,model):
#         self.name=name
#         self.colour=colour
#         self.model=model
#     def details(self):
#         print("name:",self.name,"color:",self.colour,"model:",self.model,self.Company,"Starting")

# c1=Car("Benz","Blue","V8")
# c1.details()

# students={}
# def add_student(student_id,name,marks):
#     students[student_id]={
#         "name":name,
#         "marks":marks
#     }
# def update_marks(student_id,up_marks):
#     if student_id in students:
#         students[student_id]["marks"]=up_marks
#     else:
#         print("Students not found")
# def print_details(student_id):
#     if student_id in students:
#         print("ID:",student_id)
#         print("Name:",students[student_id]["name"])
#         print("marks:",students[student_id]["marks"])
#     else:
#         print("Students not found")

# add_student(101,"karthik",10)
# add_student(102,"nagarjuna",20)
# update_marks(101,50)
# print_details(101)
# print(students)

# class student:
#     college="JNTUK"
#     def add_student(self,id,name,marks):
#         self.id=id
#         self.name=name
#         self.marks=marks
#     def up_marks(self,new_marks):
#         self.marks=new_marks
#     def print_details(self):
#         print("ID:",self.id)
#         print("Name:",self.name)
#         print("Marks:",self.marks)
#         print("College:",student.college)
# s1=student()
# s2=student()
# s1.add_student(101,"karthik",100)
# s1.print_details()

# class student:
#     college="JNTUK"
#     def __init__(self,id,name,marks):
#         self.id=id
#         self.name=name
#         self.marks=marks
#     def up_marks(self,new_marks):
#         self.marks=new_marks
#     def print_details(self):
#         print("ID:",self.id)
#         print("Name:",self.name)
#         print("Marks:",self.marks)
#         print("College:",student.college)
# s1=student(101,"karthik",100)
# s2=student(102,"Sindhu",100)
# s1.print_details()
# s2.print_details()

# class student:
#     def employe(self,id,name,salary):
#         self.id=id
#         self._name=name
#         self.__salary=salary
#     def getter_method(self):
#         return self.__salary
#     def setter_method(self):
#         if 0<=self.__salary<=40000:
#             self.__salary=50000
#         else:
#             print("No Hike")
# Emp=student()
# Emp.employe(1,"karthik",30000)
# print(Emp._name)
# print(Emp.getter_method())
# Emp.setter_method()
# print(Emp.getter_method())

#Method Overloading
# from multipledispatch import dispatch
# class First:
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(str,str,str)
#     def add(self,a,b,c):
#         return a+b+c
# s=First()
# print(s.add(3,4))
# print(s.add(2,3,2))
# print(s.add("karthik","nagarjuna","krishna"))

# class payment:
#     def pay(self):
#         print("payment processing")
# class UPI(payment):
#     def pay(self,money):
#         print(f"payment using UPI:{money}")
# class net_banking(payment):
#     def pay(self,money):
#         print(f"payment using net banking {money}")
# class card(payment):
#     def pay(self,money):
#         print(f"payment using card {money}")
# c=[card(),net_banking(),UPI()]
# for i in c:
#     i.pay(5000)

# from abc import ABC , abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class child(payment):
#     def one(self):
#         print("this is child")
#     def pay(self):
#         print("Processing")
# c=payment()
# c.one()
# c.pay() 
# 
#    
    
# from abc import ABC , abstractmethod
# class banking_system():
#     @abstractmethod
#     def bank():
#         print("StateBank of india")
#     def creation(self):
#         pass
#     def withdraw(self):
#         pass
#     def deposit(self):
#         pass
#     def fixeddepo(self):
#         pass
# class savings_acc(Bankaccount):
#     def creation(self):
#         print("Account Creation")
#     def withdraw(self):
#         print("withdraw amount")
#     def deposit(self):
#         print("deposit amount")

    









