
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
