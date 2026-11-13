
# Function as a Parameter
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f,lst):
    summation=f(lst)
    return summation

result=higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)



# Function as a Return Value
def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x>=0:
        return x
    else:
        return -(x)

def higher_order_function2(type):
    if type=='square':
        return square
    elif type=='cube':
        return cube
    elif type=='absolute':
        return absolute

res_sq=higher_order_function2('square')
print(res_sq(3))
res_cu=higher_order_function2('cube')
print(res_cu(3))
res_ab=higher_order_function2('absolute')
print(res_ab(-3))        



# Python Closures
# Python allows a nested function to access the outer scope of the enclosing function.
#  This is is known as a Closure.
def add_ten():
    ten=10
    def add(num):
        return num+ten
    return add

closure_result=add_ten()
print(closure_result(5))
print(closure_result(10))


# Python Decorators
# A decorator is a design pattern in python that allowa a user to add new functionality to an existing object without modifying its exisiting structure.
# Decorators are usually called before the definition of the function that we wanna decorate.

# Creating Decorators

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
g=uppercase_decorator(greeting)
print(g())

## Let us implement the example above with a decorator

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())


# Applying Multiple Decorators to a Single Function

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())



# Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1,para2,para3):
        function(para1,para2,para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name,last_name,country):
    print("I am {} {}. I love to teach.".format(first_name,last_name))    

print_full_name('Sneha','Nair','NewYork')    


# Built-in Higher Order Functions
# Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce.
# Lambda function can be passed as a parameter and the best use case of lambda functions is in functions like map, filter and reduce.

# Python - Map Function
# The map() function is a built-in function that takes a function and iterable as parameters.
# map(function,iterable)
numbers=[1,2,3,4,5]
def square(x):
    return x**2
numbers_squared=map(square,numbers)
print(list(numbers_squared))

# Lets apply it with a lambda function
numbers_squared2=map(lambda x : x**2,numbers)
print(list(numbers_squared2))

numbers_str=['1','2','3','4','5']
numbers_int=map(int,numbers_str)
print(list(numbers_int))


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def change_to_upper(name):
    return name.upper()

names_upper_cased=map(change_to_upper,names)
print(list(names_upper_cased))    

# Let us apply it with a lambda function
names_upper=map(lambda name:name.upper(),names)
print(list(names_upper))