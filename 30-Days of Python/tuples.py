
# tuples - ordered and unchangeable

# Creating a Tuple

# Empty tuple: Creating an empty tuple
empty_tuple=()
empt_tuple=tuple()

# Tuple with initial values
tpl=('item1','item2','item3')
fruits=('banana','apple','mango','orange')
print(len(fruits))


# Accessing Tuple Items

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit=fruits[0]
print(first_fruit)
sec_fruit=fruits[1]
print(sec_fruit)
last_index=len(fruits)-1
last_fruit=fruits[last_index]
print(last_fruit)
# Negative indexing
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fru=fruits[-4]
print(first_fru)
sec_fru=fruits[-3]
print(sec_fru)
last_fru=fruits[-1]
print(last_fru)

# Slicing tuples
# Range of Positive Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
# all items
all_fruits=fruits[-4:]
print(all_fruits)
all_fru=fruits[0:]
print(all_fru)
orange_mango=fruits[1:3]
print(orange_mango)
orange_to_the_rest=fruits[1:]
print(orange_to_the_rest)
# Range of Negative Indexes
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits =fruits[-4:]
print(all_fruits)
orange_mango=fruits[-3:-1]
print(orange_mango)
orange_to_the_rest=fruits[-3:]
print(orange_to_the_rest)

# Changing Tuples to Lists
# We can change tuples to lists and lists to tuples
# Tuple is immutable if we want to modify a tuple we should change it to a list.
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits=list(fruits)
print(fruits)
fruits[0]='apple'
print(fruits)
fruits=tuple(fruits)
print(fruits)

# Checking an Item in a Tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)
# fruits[0]='apple'  TypeError : 'tuple' does not support item assignment


# Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_vegetables=fruits+vegetables
print(fruits_vegetables)

# Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

