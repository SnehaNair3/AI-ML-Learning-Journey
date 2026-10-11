
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

# Creating a Dictionary

empty_dict={}
emp_dict=dict()
print(emp_dict)

person={
    'first_name' : 'Alice',
    'last_name' : 'Thomas',
    'age': 50,
    'country' : 'Finland',
    'is_married': True,
    'skills' : ['Java','Pyhton','HTML','CSS'],
    'address' : {
        'street' : '101 Space Street',
        'zipcode' : '2090'
    }
}

print(person)

# Dictionary Length
# It checks the number of 'key: value' pairs in the dictionary.
print(len(person))

# Accessing Dictionary Items
# We can access Dictionary items by referring to its key name.


person2 = {
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

print(person2['first_name'])
print(person2['last_name'])
print(person2['skills'])
print(person2['skills'][0])
print(person2['country'])
print(person2['address']['street'])
print(person2['age'])

# Accessing an item by key name raises an error if the key does not exist. 
# To avoid this error first we have to check if a key exist or we can use the get method.
# The get method returns None, which is a NoneType object data type, if the key does not exist.
person3 = {
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

print(person3.get('first_name'))
print(person3.get('country'))
print(person3.get('skills'))
print(person3.get('city'))
print(person3.get('address'))


# Adding Items to a Dictionary
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

person['job_title']='Instructor'
person['skills'].append('HTML')
print(person)


# Modifying Items in a Dictionary
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

person['first_name']='Eyob'
person['age']=30
print(person)

# Checking Keys in a Dictionary
# We use the in operator to check if a key exist in a dictionary
print('age' in person)
print('city' in person)
print('address' in person)

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name
# popitem(): removes the last item
# del: removes an item with specified key name
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

person.pop('first_name')
print(person)
person.popitem()
print(person)
del person['age']
print(person)

# Changing Dictionary to a List of Items
# The items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items())

print(person.items())

# Clearing a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear())

# Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# Copy a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy=dct.copy()
print(dct_copy)

# Getting Dictionary Keys as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys=dct.keys()
print(keys)

person_keys=person.keys()
print(person_keys)

# Getting Dictionary Values as a List
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values=dct.values()
print(values)

person_values=person.values()
print(person_values)






