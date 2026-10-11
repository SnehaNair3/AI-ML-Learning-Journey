
# Exercises: Level 1

age=int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive. ')
else:
    print(f"You need {18-age} more years to learn to drive.")



your_age=int(input('Enter your age: '))
my_age=24
if my_age > your_age:
    if my_age-your_age == 1:
        print('You are 1 year younger than me.')    
    else:
        print(f'You are {my_age-your_age} years younger than me.') 
elif my_age < your_age :
    if your_age-my_age == 1:
            print('You are 1 year older than me.')    
    else:
            print(f'You are {your_age-my_age} years older than me.') 
else:
     print('We both have the same age.')            



# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a=int(input('Enter number one:'))
b=int(input('Enter number two:'))
if a > b :
     print(f'{a} is greater than {b}')
elif a < b :
     print(f'{a} is smaller than {b}')
else:
     print(f'{a} is equal to {b}')     
          


# Exercises: Level 2
score=int(input('Enter your score: '))
if score >= 90 and score <= 100:
     print('A')
elif score >= 80 and score <= 89:
     print('B')
elif score>= 70 and score <= 79:
     print('C')
elif score >=60 and score <=69:
     print('D')
elif score >0 and score <=59:
     print('F')
else:
     print('FAIL')    



month=str(input('Enter month : '))
if month ==  'September' or month == 'October' or month == 'November':
    print('Autumn')
elif month == 'December' or   month =='January' or month == 'February':
     print('Winter')
elif month == 'March' or month==  'April' or month == 'May':
     print('Spring')
elif month== 'June' or month== 'July' or month == 'August':
    print('Summer')
else:
     print('Invalid month')    

# Method 2: Use the in operator (recommended)
month=input('Enter month : ')

if month in ['September', 'October','November'] :
             print('Autumn')
elif month in ['December','January','February'] :
     print('Winter')
elif month in ['March', 'April', 'May'] :
     print('Spring')
elif month in  ['June', 'July', 'August']:
     print('Summer')
else:
     print('Invalid Month')  


# Handle lowercase and uppercase inputs
month=input('Enter month : ').strip().capitalize()

if month in ['September', 'October', 'November']:
    print('Autumn')

elif month in ['December', 'January', 'February']:
    print('Winter')

elif month in ['March', 'April', 'May']:
    print('Spring')

elif month in ['June', 'July', 'August']:
    print('Summer')

else:
    print('Invalid month')

# .strip() removes leading and trailing spaces.
#  .capitalize() converts the first character to uppercase and the remaining characters to lowercase.   


fruits = ['banana', 'orange', 'mango', 'lemon']

fru=input('Enter fruit : ')
if fru in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fru)
    print(fruits)   

#  Exercises: Level 3  

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    } 

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys() :
     middle=len(person['skills'])//2
     print(person['skills'][middle])


# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
     if 'Python' in person['skills']:
          print('Yes')


# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') 
# - for more accurate results more conditions can be nested!
if person['skills'] == ['JavaScript','React']:
     print('He is a front end developer')
elif person['skills'] == ['Node','Python','MongoDB']:
     print('He is a backend developer')    
elif person['skills'] == ['React','Node','MongoDB']:
        print('He is a fullstack developer')   
else:
        print('unknown title')


# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] == True and person['country'] == 'Finland':
       print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")           
          