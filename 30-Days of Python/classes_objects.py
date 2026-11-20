# Python is an OOP language.
# Everything in python is an object, with its properties and methods.
# A number, list, string, tuple,set, dictioanry etc is an object of a corresponding built-in classs.
# We create class to create an object.
# Class is a blueprint for creating objects.
# We instantiate a class to create an object.
# The class defines the attributes and behaviour of teh object,
# while the object represents the class.

# Every element in a python program is an  object of  a class.

num=10
print(type(num))

string='string'
print(type(string))

boolean=True
print(type(boolean))

lst=[]
print(type(lst))

tpl=()
print(type(tpl))

set1=set()
print(type(set1))

dct={}
print(type(dct))


# Creating a Class
# Class name should be CamelCase.
class Person:
    pass
print(Person)    


# Creating an Object
# We can create an object by calling the class.
p=Person()
print(p)


# Class Constructor
# The init constructor function has self parameter which is a reference to the current instance of the class 
class Person:
    def __init__(self,name):
        self.name=name
        # self allows to attach parameter to the class

p=Person('Sneha')
print(p.name)
print(p)


# Let us add more parameters to the constructor function.
class Person:
    def __init__(self,firstname,lastname,age,country,city):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.city=city

p=Person('Sneha','Nair',25,'India','Mumbai')
print(p.firstname)        
print(p.lastname)        
print(p.age)        
print(p.country)        
print(p.city)        


# Object Methods
# Objects can have methods.
# The methods are functions that belong to an object.
class Person:
    def __init__(self,firstname,lastname,age,country,city):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.city=city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p=Person('Sneha','Nair',34,'India','Mumbai')
print(p.person_info())    


# Object Default Methods
class Person:
    def __init__(self,firstname='Sneha',lastname='Nair',age=20,country='India',city='Mumbai'):
        self.firtsname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.city=city

    def person_info(self):
        return f'{self.firtsname} {self.lastname} is {self.age} years old and lives in {self.city}, {self.country}.'

p1=Person()
print(p1.person_info())
p2=Person('John','Doe',30,'USA','Texas')
print(p2.person_info())    


# Method to Modify Class Default Values
class Person3:
    def __init__(self,firstname='Alice',lastname='Philip',age=34,country='UK',city='London'):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
        self.country=country
        self.city=city
        self.skills=[]

    def person_info(self):
            return f'{self.firstname} {self.lastname} is {self.age} years old and lives in {self.city}, {self.country}.'
    def add_skill(self,skill):
            self.skills.append(skill)

p1=Person3()
print(p1.person_info())            
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('Python')
p2=Person3('John','Doe',35,'Finland','Noman')
print(p2.person_info())
print(p1.skills)
print(p2.skills)


# Inheritance
# Using inheritance , we can resue the parent class code.
# Inheritance allows us to define a class that inherits all the methods and properties from parent class.
# The parent/super/base class is the class which gives all the methods and properties.
# Child class is the classs which inherits from anothe ror parent class.
class Student(Person3):
     pass

s1=Student('Eyob','Thomas',30,'Finland','Helsinki')
s2=Student('Lidiya','Philip',27,'China','Shanghai')
print(s1.person_info())
s1.add_skill('Python')
s1.add_skill('Java')
s1.add_skill('Rust')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Marketing')
s2.add_skill('Finance')
s2.add_skill('Management')
print(s2.skills)

# We did not init() constructor in the child class.
# If we didnt call it then we can still access all the propeerties from the parent.
# But if we do call the constructor , we can access the parent properties by calling super.

# We can add a new method to the child or we can override the parent class methods by creating the same method inside the child class.
# When we add the init() function, the child class will no llonger inherit the parent's init() function.

# Overriding parent method
class Student3(Person3):
    def __init__(self,firstname='Naina',lastname='Agarwal',age=40,country='USA',city='Chicago',gender='Female'):
          self.gender=gender
          super().__init__(firstname,lastname,age,country,city)
    def person_info(self):
         gender='He' if self.gender=='Male' else 'She'
         return f'{self.firstname} {self.lastname} is {self.age} yaers old. {gender} lives in {self.city}, {self.country}.'

s1 = Student3('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','Male')
s2 = Student3('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'Female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)   

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


# We can use the super() built-in function or the parent name Person to automatically inherit the methods and properties from its parent.

