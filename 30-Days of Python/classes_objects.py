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
class Person:
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

            