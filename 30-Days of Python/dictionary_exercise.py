
# Exercises: 

# Create an empty dictionary called dog
dog=dict()

# Add name, color, breed, legs, age to the dog dictionary
dog['name']='Tobby'
dog['breed']='Golden Retriever'
dog['legs']=4
dog['age']=4
print(dog)


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'firts_name': 'Sneha',
    'last_name': 'Nair',
    'gender': 'Female',
    'age': 24,
    'marital_status': 'Single',
    'skills': ['Python','Java','HTML','CSS'],
    'country': 'India',
    'city': 'Bangalore',
    'address': {
        'street' : '101, AB Street',
        'pincode': '2389'
    }
}
print(student)

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))


# Modify the skills values by adding one or two skills
student['skills'].append('Javascript')
student['skills'].append('React')
print(student['skills'])

# Get the dictionary keys as a list
print(student.keys())

# Get the dictionary values as a list
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())


# Delete one of the items in the dictionary
student.popitem()

# Delete one of the dictionaries
del student
