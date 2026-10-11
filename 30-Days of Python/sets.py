
# unordered, no duplicates 

# Creating a Set

# Creating an empty set
st=set()

# Creating a set with initial items
st2={'item1','item2','item3','item4'}
print(st2)

fruits={'banana','apple','orange','kiwi'}
print(fruits)
print(len(fruits))

# Accessing Items in a Set
# We use loops to access items. 

# Checking an Item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits)
print('cherry' in fruits)

# Adding Items to a Set
# Once a set is created we cannot change any items and we can  add additional items.
# Add one item using add()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('cherry')
print(fruits)

# Add multiple items using update() 
# The update() allows to add multiple items to a set. 
# The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)


# Removing Items from a Set
# We can remove an item from a set using remove() method. 
# If the item is not found remove() method will raise errors,
#  so it is good to check if the item exist in the given set. 
# However, discard() method doesn't raise any errors.
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item1')
print(st)
# The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
# If we are interested in the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item=fruits.pop()
print(removed_item)

fruits.discard('kiwi')
print(fruits)
fruits.discard('mango')
print(fruits)

# Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)

# Deleting a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits


# Converting List to Set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits=set(fruits)
print(fruits)

# Joining Sets
# We can join two sets using the union() or update() method or | symbol .

# Union This method returns a new set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables))
print(fruits | vegetables)

# Update This method inserts a set into a given set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# Finding Intersection Items
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python & dragon
python.intersection(dragon)

# Checking Subset and Super Set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)
whole_numbers.issuperset(even_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)

# Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers-even_numbers
whole_numbers.difference(even_numbers)

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)
python-dragon
dragon.difference(python)
dragon - python

# Finding Symmetric Difference Between Two Sets
# It means that it returns a set that contains all items from both sets, except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)
some_numbers.symmetric_difference(whole_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)
python ^ dragon

# Joining Sets
# If two sets do not have a common item or items we call them disjoint sets.
# We can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)