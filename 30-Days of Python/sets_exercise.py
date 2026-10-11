
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercises: Level 1

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

del it_companies

# Insert multiple IT companies at once to the set it_companies
add_companies=('Swiggy','Anthropic','Volvo')
it_companies.update(add_companies)
print(it_companies)

it_companies.update(('Adobe','TCS'))
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop()

# What is the difference between remove and discard
# remove throws error if element to be removed is missing, discard doesnt throw any error.



# Exercises: Level 2

# Join A and B
AB=A.union(B)
print(AB)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
AwithB=A | B
print(AwithB)
BwithA=B.union(A)
print(BwithA)

# What is the symmetric difference between A and B
print(A ^ B)
print(A.symmetric_difference(B))

# Delete the sets completely
del A
del B 

# Exercises: Level 3

age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set=set(age)
print(age_set)

len_list=len(age)
print(len_list)
len_set=len(age_set)
print(len_set)
print(len_list - len_set)


# Explain the difference between the following data types: string, list, tuple and set
# string- a data type for text
# list - collection of diff data types , ordered, chnageable, indexed
# tuple - ordered, immutable, indexed
# set - unorderd, unindexed, changeable 


# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence='I am a teacher and I love to inspire and teach people'
words=sentence.split()
print(words)
unique_words=set(words)
print(unique_words)
print(len(unique_words))

# split() separates the sentence into a list of words using spaces.
# set() removes duplicate words. For example, I and and each appear twice, but are counted only once.
