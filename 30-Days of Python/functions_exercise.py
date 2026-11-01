
# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1,num2):
    return num1+num2
print(add_two_numbers(100,500))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14*r**2
print('Area : ', area_of_circle(10))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print('Sum of all nums : ', add_all_nums(1,3,5,8,10)) 


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
   f=(c*9/5)+32
   return f
print('Celcius to fahrenheit : ', convert_celsius_to_fahrenheit(10))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month=='June' or month=="July" or month == "August":
        return "Summer"
    elif month == "September" or month=="October" or month=="November":
        return "Autumn"
    elif month=="December" or month=="January" or month=="February":
        return "Winter"
    else:
        return "Spring"
print("Season : ", check_season('October'))    
print("Season : ", check_season('January'))    
print("Season : ", check_season('April'))    
print("Season : ", check_season('June'))   

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1,y1,x2,y2):
    if x1==x2:
        return "Slope is not defined."
    return (y2-y1)/(x2-x1)
print(calculate_slope(2,3,4,7))


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math

def solve_quadratic_eqn(a, b, c):
    d=b**2-4*a*c

    if d >0:
        x1=(-b + math.sqrt(d))/(2*a)
        x2=(-b - math.sqrt(d))/(2*a)
        return x1,x2
    elif d==0:
        x=-b/(2*a)
        return x
    else:
        return "No real solutions."

print(solve_quadratic_eqn(1, -5, 6))    


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(li):
    for i in li:
        print(i)
print(print_list([1,2,3,4,5]))
# You don't need return here because the question specifically asks you to print each element, not return a value.


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(my_list):
    reversed_list=[]
    for i in range(len(my_list)-1,-1,-1):
        reversed_list.append(my_list[i])
    return reversed_list    

print(reverse_list([1,2,3,4,5]))


def reverse_list2(my_list):
    reversed_list2=[]
    i=len(my_list)-1

    while i >=0:
        reversed_list2.append(my_list[i])
        i-=1
    return reversed_list2    
print(reverse_list2([9,8,7,6,5]))