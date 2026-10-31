# Function without Parameters
def generate_full_name():
    first_name='Sneha'
    last_name='Nair'
    space=' '
    full_name=first_name + space+last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num1=10
    num2=20
    total=num1+num2
    print(total)
add_two_numbers()

# Function Returning a Value 
def generate_full_name2():
    first_name='Sneha'
    last_name='Nair'
    space=' '
    full_name=first_name+space+last_name
    return full_name
print(generate_full_name2())


def add_two_numbers2():
    num1=10
    num2=50
    total=num1+num2
    return total
print(add_two_numbers2())

# Function with Parameters
name=input('Enter name :')
def greetings(name):
    message=name + ', welcome to Python for Everyone!'
    return message
print(greetings(name))

def add_ten(num):
    return num+10
print(add_ten(90))


def square_number(x):
    return x*x
print(square_number(10))

def area_circle(r):
    return 3.14*r**2
print(area_circle(10))


def sum_of_numbers(n):
    total=0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10))    
print(sum_of_numbers(100))    

# Two Parameter
def generate_full_name3(first_name,last_name):
    space=' '
    return first_name+space+last_name
print('Full name : ', generate_full_name3('Bindu','Krishna'))


def sum_two_numbers2(num1,num2):
    return num1+num2
print('Sum : ',sum_two_numbers2(100,200) )

def calculate_age(current_year, birth_year):
    age=current_year-birth_year
    return age
print('Age : ',calculate_age(2026,2002))

def weight_of_object(mass,gravity):
    weight=str(mass*gravity) + 'N'
    return weight
print('Weight of an object in Newtons: ',weight_of_object(100,9.81))


# Passing Arguments with Key and Value
# If we pass the arguments with key and value, the order of the arguments does not matter.
def print_fullname(first_name,last_name):
    return first_name+' '+last_name
print(print_fullname(first_name='Alice',last_name='Bob'))

def add_numbers(num1,num2):
    return num1+num2
print(add_numbers(num2=30,num1=20))


# Function Returning a Value 
# Returning a string
def print_name(name):
    return name
print_name('Barbey')

def print_fullname2(firstname,lastname):
    fullname=firstname+' '+lastname
    return fullname
print_fullname2('Elina','Philip')


# Returning a number
def add_two_nums(num1,num2):
    return num1+num2
add_two_nums(10,20)

def calculate_age(curr_year, birth_year):
    age=curr_year-birth_year
    return age
print('Age: ',calculate_age(2026,2007))

# Returning a boolean
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(5))
print(is_even(8))

# Returning a list
def find_even_nums(n):
    evens=[]
    for i in  range(n+1):
        if i%2==0:
            evens.append(i)
    return evens
print('Even numbers : ',find_even_nums(12))        


# Function with Default Parameters
def cal_age(birth_year,curr_year=2026):
    age =curr_year-birth_year
    return age
print('Age: ',cal_age(2007))   
print('Age: ',cal_age(2007,2027))   

def weight_obj(mass,gravity=9.81):
    weight=str(mass*gravity)+'N'
    return weight
print('Weight: ', weight_obj(100))
print('Weight: ', weight_obj(100,1.62))


# Arbitrary Number of Arguments
# if we do not know the number of argumenst we pass to a function, then we can create a fun which can take arbitrary number of arguments by adding a * before the parametr name
def sum_all_nums(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print('Sum : ', sum_all_nums(2,3,5))  


# Default and Arbitrary Number of Parameters in Functions
def generate_groups(team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Alice','Bob','Maria','Diya','Anne')        


# Dictionary unpacking
def greet(name,location):
    print("Hi there, ",name," how is the weather in ",location," ?")

# Call the function using keyword arguments
greet(name="Alice",location="New York")  

# Create a dictionary with keys matching the function's parameter names
my_dict= {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)

# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.


# Function as a Parameter of Another Function
def square_num(x):
    return x*x
def do_something(f,x):
    return f(x)
print(do_something(square_num,12))
