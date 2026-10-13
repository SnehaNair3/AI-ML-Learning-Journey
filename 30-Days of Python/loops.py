
# while loop 

count=0
while count < 5 :
    print(count)
    count=count+1

count=0
while count < 5 :
    print(count)
    count=count+1
else:
    print(count)


# Break and Continue
# Break: We use break when we like to get out of or stop the loop.
count=0
while count <5:
    print(count)
    count=count+1
    if count ==3:
        break           
# The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.


# Continue: With the continue statement we can skip the current iteration, and continue with the next:
count=0
while count <5:
    if count ==3:
        count+=1
        continue
    print(count)
    count+=1
# The above while loop only prints 0, 1, 2 and 4 (skips 3).


# For Loop

# -Using For loop on list
numbers=[0,1,2,3,4,5]
for number in numbers:
    print(number)

# -Using For loop on string
language='python'
for letter in language:
    print(letter)    

for i in range(len(language)):
    print(language[i])    


# -Using For loop on tuple
nums=(1,2,3,4,5)
for num in nums:
    print(num)  

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}  

for key in person:
    print(key)

for key,value in person.items():
    print(key,value)    


# -Using For Loop in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)    


#  Break: We use break when we want to stop our loop before it is completed.
numbers=(0,1,2,3,4,5)
for num in numbers:
    print(num)
    if num==3:
        break    


# Continue: We use continue when we want to skip some of the steps in the iteration of the loop.
numbers = (0,1,2,3,4,5)
for num in numbers:
    print(num)
    if num ==3:
        continue
    print('Next number should be ',num+1) if num !=5 else print('loop ends!')
print('outside the loop')


# The Range Function
lst=list(range(11))
print(lst)
st=set((range(1,11)))
print(st)

lst2=list(range(0,11,2))
print(lst2)
st2=set(range(0,11,2))
print(st2)

lst3=list(range(11,0,-2))
print(lst3)


for number in range(11):
    print(number)


# Nested For Loop
# We can write loops inside a loop.
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}    

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



# For Else
# If we want to execute some message when the loop ends, we use else
for num in range(11):
    print(num)
else:
    print('The loop stops at ',num) 


# Pass
# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors.
for num in range(6):
    pass  


