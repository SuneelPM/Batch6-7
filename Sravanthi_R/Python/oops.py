# class python():
#     a=10
#     def first():
#         print("this is my first method")
# print(python.a)
# print(python.first())

# class first:
#     a=10
#     def first(self):
#         a=20
#         print("this is my first method")
# s1=first()
# print(s1.a)

# class first:
#     def first(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b) 
# s1=first()
# s1.first(10,20)
# s2=first()
# s2.first(30,50)

# class car():
#     company="TATA"
#     def start(self,name,color,model):
#         self.name=name
#         self.color=color
#         self.model=model
#         print(self.name,self.color,self.model,"starting")
#     def stop(self):
#         print("stopping")
# c1=car()
# c1.start("benz","red","v8")
# c2=car()
# c2.start("adio","white","v10")

# class car():
#     company = "TATA"
#     def __init__(self, name, color, model):
#         self.name = name
#         self.color = color
#         self.model = model
#     def details(self):
#         print(self.name, self.color, self.model, self.company, "Starting")
# c1 = car("Benz", "Blue", "V8")
# c1.details()


                                                    # date:10-2-26

# withouth using oops
# students={}
# students[101]={
#     "name":"sravss",
#     "marks":80
# }
# print(students)


#with using oops

# students = {}
# def add_student(student_id, name, marks):
#     students[student_id] = {
#         "name": name,
#         "Marks": marks
#     }
# def update_marks(student_id, up_marks):
#     if student_id in students:
#         students[student_id]["Marks"] = up_marks
#     else:
#         print("Student not found")
# def print_details(student_id):
#     if student_id in students:
#         print("ID:", student_id)
#         print("Name:", students[student_id]["name"])
#         print("Marks:", students[student_id]["Marks"])
#     else:
#         print("Student not found")
# add_student(101,"sravss",73)
# add_student(102,"suji",74)
# print(students)


# class student:
#     college="JNTUK"
#     def add_student(self,id,name,marks):
#        self.id=id
#        self.name=name 
#        self.marks=marks 
#     def up_marks(self,new_marks):
#        self.marks=new_marks
#     def print_details(self):
#         print("ID:",self.id)
#         print("name:",self.name)
#         print("marks:",self.marks)
#         print("college:",self.college)
# s1=student()
# s2=student()
# s1.add_student(101,"sravss",90)
# s2.add_student(102,"suji",60)
# s1.print_details()
# s2.print_details()

#ENCAPSULAION(public,private,protected)
# class student:
#     def employe(self,id,name,salary):
#         self.id=id
#         self._name=name
#         self.__salary=salary
#     def private(self):
#         print(self.__salary)
# Emp=student()
# Emp.employe(1,"sravss",30000)
# print(Emp._name)
# Emp.private()

#setter method
# class student:
#     def employe(self,id,name,salary):
#         self.id=id
#         self._name=name
#         self.__salary=salary
#     def getter_method(self):
#         return self.__salary
#     def setter_method(self):
#         if 0<self.__salary<=40000:
#             self.__salary=50000
#         else:
#             print("No Hike")
# Emp=student()
# Emp.employe(1,"sravss",30000)
# print(Emp._name)
# print(Emp.getter_method())
# Emp.setter_method()
# print(Emp.getter_method())
    

                                                         #Date:-11-2-26

                        # Inheritence 
    #1.single inheritence
# class person:
#     def walk(self):
#         print("this is method belongs walking")
#     def speak(self):
#         print("this method belongs speaking")
# class child(person):
#     def student(self):
#         print("this is student method")
# s1=child()
# s1.walk()
# s1.speak()
# s1.student()

           #2.multilevel inheritence

# class first:
#     def one(self):
#         print("this is first method")
#     def two(self):
#         print("this is second method")
# class second(first):
#     def third(self):
#         print("this is third method")
#     def four(self):
#         print("this is four method")
# class third(second):
#     def fifth(self):
#         print("this is fifth method")
#     def six(self):
#         print("this is six method")
# s1=third()
# s1.one()
# s1.two()
# s1.third()
# s1.four()
# s1.fifth()
# s1.six()

                 #3.multiple inheritence

# class first:
#     def one(self):
#         print("this is first method")
#     def two(self):
#         print("this is second method")
# class second(first):
#     def third(self):
#         print("this is third method")
#     def four(self):
#         print("this is four method")
# class third(first):
#     def fifth(self):
#         print("this is fifth method")
#     def six(self):
#         print("this is six method")
# s1=third()
# s1.one()
# s1.two()
# s1.fifth()
# s1.six()

                 #4.hieraechical inheritence

# class first:
#     def one(self):
#         print("this is first method")
#     def two(self):
#         print("this is second method")
# class second:
#     def third(self):
#         print("this is third method")
#     def four(self):
#         print("this is four method")
# class third(first,second):
#     def fifth(self):
#         print("this is fifth method")
#     def six(self):
#         print("this is six method")
# s1=third()
# s1.one()
# s1.two()
# s1.third()
# s1.four()
# s1.fifth()
# s1.six()

           
           #5.hybrid inheritence

# class first:
#     def one(self):
#         print("this is first method")
#     def two(self):
#         print("this is second method")
# class second:
#     def third(self):
#         print("this is third method")
#     def four(self):
#         print("this is four method")
# class third(first):
#     def fifth(self):
#         print("this is fifth method")
#     def six(self):
#         print("this is six method")
# class four(second,third):
#     def hybrid(self):
#         print("this is hybrid mothod")       
# s1=four()
# s1.one()
# s1.two()
# s1.third()
# s1.four()
# s1.fifth()
# s1.six()
# s1.hybrid()

                      #Constucter or initilizer

# class first:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def output(self):
#         print(self.name,self.age)
# s1=first("sravss",20)
# s1.output()


# class first:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def output(self):
#         print(self.name,self.age)
# class second(first):
#     def __init__(self,name,age):
#         super().__init__(name,age)
# s1=second("suji",20)
# s1.output()

             #method overloading
            
# class one:
#     def add(self,*a):
#         sum=0
#         for i in a:
#             sum+=i
#         print(sum)
# s1=one()
# s1.add(4,4)
# s1.add(7,3)


                                                # date:-12-2-26

            #polymorphism
# print(2+3)
# print("f"+"s")
# print(3*3)
# print("S"*7)
 
    #method overloading
# from multipledispatch import dispatch
# class first:
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(str,str,str)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(int,int,int,int)
#     def add(self,a,b,c,d):
#         return a+b+c
# s=first()
# print(s.add(5,6,7,8))
# print(s.add(5,6,7))
# print(s.add(5,6))
# print(s.add("sravss","suji","praggu"))
      

# class parent:
#     def method(self):
#         print("this is parent method")
# class child(parent):
#     def method(self):
#         parent.method(self)
#         super().method()
#         print("this is child method")
# s=child()
# s.method()

          #method overriding
# class payment:
#     def pay(self):
#         print("payment processing")
# class upi(payment):
#     def pay(self,money):
#         print(f"payment using upi{money}")
# class net_banking(payment):
#     def pay(self,money):
#         print(f"payment using net banking {money}")
# class card(payment):
#     def pay(self,money):
#         print(f"payment using card {money}")
# c3=[card(),net_banking(),upi()]
# for i in c3:
#     i.pay(50000)

         #abstraction

# from abc import ABC ,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass
# class child(payment):
#     def one(self):
#         print("this is child")
#     def pay(self):
#         print("processing")
# c=child()
# c.one()
# c.pay()

from abc import ABC ,abstractmethod
class banking(ABC):
    def bank(self):
        pass
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdrow(self):
        pass
    @abstractmethod
    def pin(self):
        pass
class child(banking):
    def deposit(self):
        print("deposit the money")
    def withdrow(self):
        print("withdrow the money")
    def pin(self):
        print("change the pin")
c=child()
c.deposit()
c.withdrow()
c.pin()
