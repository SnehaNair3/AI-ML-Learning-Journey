
# There are four collection data types in Python :
# 1 - List  -  ordered, can be changed, allows duplicates
# 2 - Tuple - ordered, unchangeable (immutable) , allows duplicates.
# 3 - Set - unordered, unmodifiable (but can add new elements), no duplicates
# 4 - Dictionary - unordered, modifiable, no duplicates


# How to Create a List
# In Python we can create lists in two ways:

# Using list built-in function
lst=list()
empty_list=list()
print(len(empty_list))

# Using square brackets, []
lst=[]
empty_list2=[]
print(len(empty_list2))


fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway'] 

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))


# Lists can have items of different data types
lst=['Sneha','Nair',250,True,{'country':'India','city':'Bangalore'},'Doctor']
print(lst)


# Accessing List Items Using Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit=fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit) 
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing List Items Using Negative Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango


# Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item,second_item,third_item,*rest=lst
print(first_item)
print(second_item)
print(third_item)
print(rest)



# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) 
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)



# Slicing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits=fruits[0:4]
all_fruits2=fruits[0:]
orange_mango=fruits[1:3]
orange_mango_lemon=fruits[1:]
banana_mango=fruits[::2]
print(banana_mango)
orange_lemon=fruits[1::2]
print(orange_lemon)



# Negative Indexing
fruits=['banana','orange','mango', 'lemon']
all_fruits=fruits[-4:]
orange_mango=fruits[-3:-1]
oramge_mango_lemon=fruits[-3:]
reverse_fruits=fruits[::-1]


# Modifying Lists
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0]='avocado'
print(fruits)
fruits[1]='apple'
print(fruits)
last_index=len(fruits)-1
fruits[last_index]='cherry'
print(fruits)



# Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist='banana' in fruits
print(does_exist)
does_exist2='lime' in fruits
print(does_exist2)



# Adding Items to a List
flowers=list()
flowers.append('Lily')
flowers.append('Rose')
flowers.append('Lotus')
flowers.append('Sunflower')
print(flowers)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)


# Inserting Items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
# insert apple between orange and mango
fruits.insert(2,'apple')
print(fruits)

fruits.insert(3,'lime')
print(fruits)


# Removing Items from a List
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

# Removing Items Using Pop
# The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# Removing Items Using Del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1]
print(fruits)
del fruits[1:2]
print(fruits)
del fruits
print(fruits)  #Error


# Clearing List Items
# The clear() method empties the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)



# Copying a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy=fruits.copy()
print(fruits_copy)
fruits_copy[1]='kiwi'
print(fruits_copy)
print(fruits)


# Joining Lists

# list3 = list1 + list2
positive_numbers = [1, 2, 3, 4, 5]
zero=[0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_vegetables=fruits+vegetables
print(fruits_vegetables)

# Joining using extend() method 
# The extend() method allows to append list in a list
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print(num1)

negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
print(negative_numbers)

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )


# Counting Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('banana'))
ages=[22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  # first occurence 


# Reversing a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)


# Sorting List Items
# sort(): this method modifies the original list

# lst = ['item1', 'item2']
# lst.sort()                # ascending
# lst.sort(reverse=True)    # descending
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# sorted(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits,reverse=True))
print(fruits)


