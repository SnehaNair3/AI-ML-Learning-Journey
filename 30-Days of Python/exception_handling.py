
try:
    print(10+'5')
except:
    print('Something went wrong.')


try:
    name=input('Enter your name:')
    year_born=input('Year of birth : ')
    age=2026-year_born
    print(f'You are {name} and your age is {age}.')
except:
    print('Something went wrong.')   


try:
    name=input('Enter name:')
    year_born=input('Enter year of birth: ')
    age=2020-year_born 
    print(f'You are {name} and your age is {age}.')   
except TypeError:
    print('Type error occurred.')
except ValueError:
    print('Value error occurred.')
except ZeroDivisionError:
    print('zero division error occurred.')    



try:
    name= input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')  
except ZeroDivisionError:
    print('zero division error occur')   
else:
    print('I usually run with the try block')
finally:
    print('I always run.')  



try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.') 
except Exception as e:
    print(e)               



# Packing and Unpacking Arguments in Python
# * for tuples
# ** for dictionaries
    
# Unpacking

# Unpacking Lists
def sum_of_five_nums(a,b,c,d,e):
    return a+b+c+d+e

lst=[1,2,3,4,5]

try:
    print(sum_of_five_nums(lst))
except Exception as e:
    print(e)    

# When we run the this code, it raises an error,
#  because this function takes numbers (not a list) as arguments.
#  Let us unpack/destructure the list.
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))

# We can also use unpacking in the range built-in function that expects a start and an end.
numbers=range(2,7)
print(list(numbers))
args=[2,7]
numbers2=range(*args)
print(numbers2)

# A list or a tuple can also be unpacked like this:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin,swe,nor,*rest=countries
print(fin, swe, nor, rest)
numbers3 = [1, 2, 3, 4, 5, 6, 7]
one,*middle,last=numbers3
print(one, middle, last)


# Unpacking Dictionaries
def unpacking_person_info(name,country,city,age):
    return f'{name} lives in {country}, {city}. He/She is {age} years old.'
dct={'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct))


# Packing
# Sometimes we never know how many arguments need to be passed to a python function.
# We can use the packing method to allow our function to take unlimited number or arbitrary number of arguments.

# Packing Lists
def sum_all(*args):
    s=0
    for i in args:
        s+=i
    return s
print(sum_all(1,2,3))    
print(sum_all(1,2,3,4,5,6,7))  


# Packing Dictionaries
def packing_person_info(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print(f"{key}= {kwargs[key]}")
    return kwargs   

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250)) 


# Spreading in Python
lst_one=[1,2,3]
lst_two=[4,5,6,7]
lst=[0,*lst_one,*lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries =[*country_lst_one,*country_lst_two]
print(nordic_countries)


# Enumerate
# If we are interested in an index of a list,
#  we use enumerate built-in function to get the index of each item in the list.
for index,item in enumerate([20,30,40]):
    print(index,item)


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index,i in enumerate(countries):
    if i =='Finland':
        print(f'The country {i} has been found at index {index}.')


#  Zip
# Sometimes we would like to combine lists when looping through them.
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime','kiwi']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f,v in zip(fruits,vegetables):
    fruits_and_veges.append({'fruit':f,'veg':v})
print(fruits_and_veges)           



# Exercises
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries,es,ru=names
print(nordic_countries)
print(es)
print(ru)
