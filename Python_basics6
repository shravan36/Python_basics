# 14. Object Oriented Programming

#Class
# User defined objects created x using Class- Initializing Class

class Student:
  print("Hello All")
x = Student() #Object Instantiation
print(type(x))

class Student:
  def func():
    print("Hello all welcome to the session")
Student.func()

class Student:
  def func(self):
    print("Hello all welcome to the session")
x = Student()
x.func()

#Class Object attribute - same for any instance of the class

class Student:
  year = '2021'
  def func():
    print("Hello all welcome to the session")
x = Student()
x.year

class Student:
  year = '2021'
  def func(self):
    print("Hello all welcome to the session", self.year)
x = Student()
x.func()

# Attribute of an Object (characteristic of an object) Attribute won't take any argument

class Student:
    def __init__(self,name): #__init__ (Method) to initialize attribute of an object (Constructor)
        self.name = name #self.name = attribute initialized
 #(Creating Instance of Student class{Object of certain class})       
elon = Student(name='Elon Musk !') #name: argument

print(elon.name) #accessing class attribute through object

class Student:
    def __init__(self,name): 
        self.name = name 
elon = Student(name='Elon Musk !')
champ = Student(name='I am Champ !')

print(elon.name) 
print(champ.name)

class Student:
    def __init__(self,name,age): 
        self.name = name 
        self.age = age
elon = Student(name='Elon Musk !',age=40) 

print(elon.name)
print(elon.age)

class Student:
    Total = 500

    def __init__(self, marks):
        self.marks=marks
        print("Initialized...")

    def findLoss(self):
        return self.Total - self.marks

    def findPercentage(self):
        return self.marks/self.Total*100
        
a = Student(marks=450)

print('Total Marks: ',a.Total)
print('Lossed Marks: ',a.findLoss())
print('Percentage is: ',a.findPercentage())

#Special Methods

class Student:
    Total = 500

    def __init__(self, name,marks,gender):
        self.name=name
        self.marks=marks
        self.gender=gender
        print("Initialized...")

    def __len__(self):
        return self.marks

    def __str__(self):
        return "Name: %s | Marks: %s | Gender: %s" %(self.name,self.marks,self.gender)

    def __del__(self):
        print("Student Database is Deleted")
        
a = Student('champ',450,'male')

print(a)
print('Marks: ',len(a))
del a

#Inheritance - Help to reduce complexity of the program 
#Base Class & Derived Class

class Elon:
    def __init__(self):
        print("Profile created")

    def name(self):
        print("Elon Musk")

    def age(self):
        print("40")


class SpaceX(Elon):
    def __init__(self):
        Elon.__init__(self)
        print("Company Profile created")

    def name(self):
        print("SpaceX")

    def type(self):
        print("Private Space travel")

a = SpaceX()

a.name() #Derived class modified behavior of base class

a.age()

#Polymorphism
#Different object classes can share the same method name, and those methods can be called from the same place even though a different objects passed in

class Elon:
    def __init__(self,name):
        self.name = name
    def type(self):
        return "Entrepreneur"
class Sundar:
    def __init__(self,name):
        self.name = name
    def type(self):
        return "CEO"
          
person1 = Elon('Elon Musk') #name: argument
person2 = Sundar('Sundar Pichai')

#returning unique result of object which have same method(type)
print(person1.type())
print(person2.type())

for i in [person1,person2]:
  print(i.name)
  print(i.type())
  print("**************")
