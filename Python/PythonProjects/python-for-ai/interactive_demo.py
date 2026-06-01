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

list2=["Sneha",25,"Bangalore",22000, ["Kerala","Karnataka"]]
len(list2)
list2[0]
list2[4]
list2[4][0]
list2[4][1]
list2[-1]
list2[-1][-1]
list2[-1][-2]

list3=[1,2,3,4]
list4=list3 + [5,6]
list4

# Membership in lists
list5=[1,2,3,4,5,6]
print(1 in list5)
print(8 in list5)

# extend() function in list- it extends the list
list6=[1,2,3,4,5]
list6.extend([9,10])
list6
len(list6)
# append() function
list6.append([11,12])
list6
len(list6)

# del command
list7=[1,2,3,4]
del list7[2]
list7

# pop() - removes the specified index element
# default- removes the last element 
# pop operation works on indexes
list8=[1,2,3,4,5,6,7,8,9]
list8.pop(-1)
list8
list8.pop()
list8

# remove()
# remove operation works on values
list8.remove(3)
list8

# sort
list9=[1,2,3,6,7,8,9]
list9.sort()
list9
list9.sort(reverse=True)
list9

# Difference between sort and sorted
A=['Carrot','Tomato','Potato','Pea']
B=A.sort()
print(A)
print(B)
# assignment doesnt work in sorted

C=['Mango','Plum','Kiwi','Apple']
D=sorted(C)
print(C)
print(D)
# assignment operation works for sorted 
# use sorted method to store the sorted list into another list (creates another object)


# Shallow copy
P=['Pen','Pencil','Eraser','Scale']
Q=P
print(P)
print(Q)
P.pop()
print(P)
print(Q)

M=['Book','Table','Chair','Box']
N=M[1:4]
print(M)
print(N)
M.pop()
print(M)
print(N)
# changes made to M not affetced to M
# new reference object created in the memory.

# Question?
customer='Kumar_Ravi_003'
first_name=customer[6:10]
second_name=customer[0:5]
customer_code=customer[11:]
customer_code=customer[-3:]
#OR
res=customer.split('_')
res
print('second_name: ' ,res[0])
print('first_name: ' ,res[1])
print('customer_code: ' ,res[2])



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

nums=1,2,3,4
type(nums)

nested_tuple=(1,2,3,4,(5,6))
len(nested_tuple)

mixed_tuple=(1,2,3,4,[5,6,7])
len(mixed_tuple)
type(mixed_tuple[4])
type(mixed_tuple[0])
print(mixed_tuple[1])
print(mixed_tuple[4][1])
print(len(mixed_tuple[4]))

t1=1.2,
type(t1)
t2=3.4 # not a tuple
type(t2)
t3=(2,)
type(t3)
t4=(2) # not a tuple
type(t4)

# concatenation
tuple1=('Hello','nice','to')
tuple2=('meet','you!')
tuple3=tuple1+tuple2
print(tuple3)

# min , max and sum functions
odd=(1,3,5,7)
sum(odd)

even=(2,8,4,6)
max(even)
min(even)
sum(even)

t=(1,2.5,4.8,5,6.1)
max(t)
sum(t)
min(t)

s=('hello',4,6,7,'hi')
# max(s) # not possible ERROR

greet=('Hello','welcome',5,6,'land','of','coconuts')
greet[0:2]
join=('to','the')
greet[4:7]
res_tuple=greet[0:2]+join+greet[4:7]
res_tuple

# sorting a tuple
v=(1,4,5,3,7,9,5,6)
w=sorted(v)
print(v)
print(w)
type(w)

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















