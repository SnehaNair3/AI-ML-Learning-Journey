
# Exercises: Level 1

# Create an empty tuple
empty_tuple=tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sis=('Neha','Sneha','Alice','Malu','Navya')
bro=('Vigu','Tom','Ram','Jerry')
# Join brothers and sisters tuples and assign it to siblings
sibling=sis + bro
print(sibling)

# How many siblings do you have?
print(len(sibling))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
sibling=list(sibling)
sibling.append('Bindu')
sibling.append('Kunhambu')
family_members=tuple(sibling)
print(family_members)


# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings=family_members[:9]
parents=family_members[9:]
print(siblings)
print(parents)


# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('apple','mango','banana','cherry')
vegetables=('carrot','tomato','potato','cabbage')
animal_products=('cheese','butter','milk','curd')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt =list(food_stuff_tp)
print(food_stuff_lt)


# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
n=len(food_stuff_tp)
if n % 2==0:
    middle_items= (food_stuff_tp[n//2-1] ,  food_stuff_tp[n//2])
else:
    middle_items=(food_stuff_tp[n//2])

print(middle_items)  


# Slice out the first three items and the last three items from food_stuff_lt list
first_three=food_stuff_lt[:3]
print(first_three)
last_three=food_stuff_lt[-3:]
print(last_three)

# Delete the food_stuff_tp tuple completely
del food_stuff_tp 


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if an item exists in tuple:

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)