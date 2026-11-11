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
