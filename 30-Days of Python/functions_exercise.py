
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



# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(list1):
    capital_list=[]
    for i in range(0,len(list1)):
        capital_list.append(list1[i].upper())
    return capital_list
print(capitalize_list_items(['Apple','mango','banana','orange','kiwi']))        
print(capitalize_list_items(['sneha','neha','malu','vigu','Alice']))        




# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(my_list,item):
    my_list.append(item)
    return my_list
print(add_item(['Potato', 'Tomato', 'Mango', 'Milk'],'Meat'))   
print(add_item([2, 3, 7, 9],5))   



# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(my_list,item):
    my_list.remove(item)
    return my_list
print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'],'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers,3))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    return num*(num+1)/2
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum_odds=0
    for i in range(1,num+1,2):
        sum_odds+=i
    return sum_odds    
print(sum_of_odds(5))
print(sum_of_odds(10))
print(sum_of_odds(15))



# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    sum_even=0
    for i in range(0,num+1,2):
        sum_even+=i
    return sum_even
print(sum_of_even(5))    
print(sum_of_even(10))    
print(sum_of_even(15))    


# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    evens=0
    odds=0
    for i in range(num+1):
        if i % 2 ==0:
            evens+=1
        else:
            odds+=1  
    print(f"The number of odds are {odds}")        
    print(f"The number of evens are {evens}") 
evens_and_odds(100)
evens_and_odds(10)
evens_and_odds(20)


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(4))    
print(factorial(3))    
print(factorial(5))    
print(factorial(6))   


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    if len(value) ==0:
        return True
    else:
        return False
print(is_empty([1,2,4]))
print(is_empty(['apple','banana']))
print(is_empty([]))



# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
