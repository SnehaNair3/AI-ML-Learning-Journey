# Example:1
# change a string to a list of characters

language='Python'
lst=list(language)
print(type(lst))
print(lst)

lst2=[i for i in language]
print(type(lst2))
print(lst2)


# Example:2
# For instance if you want to generate a list of numbers

# Generating numbers
numbers=[i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration
squares=[i*i for i in range(11)]
print(squares)

# It is also possible to make a list of tuples
nums=[(i,i*i) for i in range(11)]
print(nums)


# Example:2
# List comprehension can be combined with if expression

# Generating even numbers
even_nums=[i for i in range(21) if i%2 ==0]
print(even_nums)

# Generating odd numbers
odd_nums=[i for i in range(21) if i%2 !=0]
print(odd_nums)

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers=[i for i in numbers if i%2==0 and i>0]
print(positive_even_numbers)


# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list=[number for row in list_of_lists for number in row]
print(flattened_list)


# Lambda Function
# Lambda function is  a small anonymous function without a name.
x = lambda param1, param2, param3: param1 + param2+param3
# print(x(arg1,arg2,arg3))

# Named function 
def add_two_nums(a,b):
    return a+b
print(add_two_nums(2,3))

add_two_nums2=lambda a,b:a+b
print(add_two_nums2(1,5))

# Self invoking lambda function 
print((lambda a,b: a+b)(1,3))

square=lambda x:x**2
print(square(4))

cube=lambda x: x**3
print(cube(4))

# Multiple variables 
multiple_variable=lambda a,b,c:a**2-3*b+4*c
print(multiple_variable(5,5,3))


# Lambda Function Inside Another Function
def power(x):
    return lambda n:x**n

cube=power(2)(3)
print(cube)
two_power_of_five =power(2)(5)
print(two_power_of_five)