# OOP
# Class and object
# creating classes and objects

# Defining a class
# length and breadth as attributes
# init() - constructor of class
# self parameter - refers to the newly created instance of the class
# attributes length and breadth are associated with self keyword to identify themselves as instance variables.
class Rectangle :
  def __init__(self):
    self.length=10
    self.breadth=5

# create the object by calling name of the class  followed by parenthesis.
# print the values using dot operator.  
rect=Rectangle()
rect.length
rect.breadth 
print("Length= ",rect.length,"\nBreadth= ",rect.breadth)

# Parameterised Constructor
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
rect=Rectangle(15,40)
print(rect.length)    
print(rect.breadth)  

# Class variable and instance variable
class Circle:
  pi=3.14
  def __init__(self,radius):
    self.radius=radius
# pi = class variable
# radius = instance variable
circle_1=Circle(5) # Instatiating the circle class
print(circle_1.pi)

circle_1=Circle(5)
print("Radius = {} \t pi = {}".format(circle_1.radius,circle_1.pi))

circle_2=Circle(2)
print("Radius = {} \t pi = {}".format(circle_2.radius,circle_2.pi))

# Changing the class variable
Circle.pi=3.1436
circle_1.pi

# Adding a method to a class
class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth
  def calculate_area(self):
     return self.length*self.breadth
  
rect_1=Rectangle(10,20)
print(rect_1.length)  
print(rect_1.breadth) 
print("Area is : ",rect_1.calculate_area()) 

# Significance of self
# The attributes length and breadth are associated with an instance
# self makes sure that each instance refers to its own copy of attributes.
new_rect=Rectangle(3,5)
print("Length= ",new_rect.length,"\t Breadth= ",new_rect.breadth,"\t Area = ",new_rect.calculate_area())

# Inheritance and overriding
class Employee:
  def function_1(self):
    print("Hello world!")
class Department(Employee):
  pass
emp=Employee()
emp.function_1()
dept=Department()
dept.function_1()

class Shape:
  def set_color(self,color):
    self.color=color
  def calculate_area(self):
    pass
  def color_the_shape(self):
    color_price={"red":10,"blue":15,"green":20}
    return self.calculate_area() * color_price[self.color]  
  
class Circle(Shape):
  pi=3.14
  def __init__(self,radius):
    self.radius=radius
  def calculate_area(self):
    return Circle.pi*self.radius**2
c=Circle(5)
c.set_color("red")
print("Circle with radius ",c.radius," when colored ",c.color," costs ",c.color_the_shape())   
print(c.calculate_area())  

class Rectangle(Shape):
  def __init__(self,length,breadth):
    self.length=length 
    self.breadth=breadth
  # Overriding user defined method  
  def calculate_area(self):
    return self.length*self.breadth
  # Overriding python default method
  def __str__(self):
    return "Area of rectangle = " + str(self.calculate_area())

r=Rectangle(5,10)
r.set_color("blue")
print("Area is : ",r.calculate_area())
print("Rectangle with length= ",r.length," and breadth= ",r.breadth," when colored ",r.color," costs ",r.color_the_shape())
r.__str__()



