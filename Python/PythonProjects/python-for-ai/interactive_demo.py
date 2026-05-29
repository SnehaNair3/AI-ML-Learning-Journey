# Let's explore interactive mode
name = "Python Learner"
print(f"Hello, {name}!")

# Some data to work with
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Calculate something
total = sum(numbers)
print(f"Total: {total}")


# First, create a variable
message = "Hello"

# Later, use it (even in a different cell)
print(message + " World!")

# Modify it
message = message.upper()
print(message)

num=10
result=f"The number is {num}"

place="Singapore"
place.lower()
place.upper()
place.startswith("s")

sentence="My name is Dave"
sentence.title()

temp=38
if temp > 30:
    print("Its very hot")
else:
    print("Normal weather")    


has_ticket=True
age=20
if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Needs supervision")
else:
    print("Please buy the ticket.")  


#List
#allows duplicates
# indexed
# mutable
age=25
has_license=False
my_list=["Alice",25,age,has_license,True]  
len(my_list)

numbers=[1,6,4,1,3,7]
len(numbers)
numbers.count(1)
numbers.index(4)
numbers.append(5)
numbers.insert(1,8)
numbers
numbers.remove(3)
numbers
num2=numbers.copy()
num2
numbers.sort()
numbers
numbers.reverse()
numbers

# Dictionaries
# key-value pairs
# keys cannot be duplicate, but values can have duplicate values
# ordered
# mutable
person_info={
    "name":"Alice",
    "age":25,
    "city":"Mumbai"
}
person_info["age"]
person_info["name"]
person_info["city"]="Seoul"
person_info["city"]
person_info["country"]="South Korea"
person_info
person_info["race"]="Asian"
person_info
del person_info["race"]
person_info

#Dictionary Methods
print(person_info.keys())
print(person_info.values())
print(person_info.items())

if "name" in person_info:
    print("Name found!")

person_info.update({"age":30,"job":"Engineer"})
person_info  

# Tuples
# cannot be changed
# ordered,non-mutable,indexed,allow duplicates
colors=("red","green","blue","red")
colors
colors[0]


#Set
# no duplicates
# not ordered
# no indexing
#Empty set
empty_set=set()
# not {}-  thatsa dictionary
real={1,2,3,4,5}
fruits=set(["Apple","Banana","Orange"])
# From a list, remove duplicates
marks=[20,56,45,70,45]
unique_marks=set(marks)

# operations
fruits.add("kiwi")
fruits
fruits.remove("Orange") # error if not found
fruits
fruits.discard("banana") # no error if not found
fruits
# fruits.remove("lichi") # gives error















