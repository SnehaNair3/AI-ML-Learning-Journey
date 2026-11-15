
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

