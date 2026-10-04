
# Creating a String

letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)



# Multiline strings

multiline_string1 = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string1)

# Another way of doing the same thing
multiline_string2 = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string2)


# String concatenation
first_name="Sneha"
last_name="Nair"
space=" "
full_name=first_name+space+last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(first_name) > len(full_name))



# Escape sequences
print('Hello, Good morning! \nHow are you?\nHope you are doing fine.')

print('Days\tTopic\tHours')
print('1\tPython\t2')
print('2\tFile Handling\t4')
print('3\tVariables\t1')

print('This is  a backslash \\')

print('There is a saying \"Practice makes a man perfect!!."')



# String formatting

# Strings only
first_name='Sneha'
last_name='Nair'
language='Python'
formatted_string='Iam %s %s. I teach %s ' %(first_name,last_name,language)
print(formatted_string)


#Strings and numbers
radius=10
pi=3.14
area=pi*radius**2
formatted_string2='The area of the circle with a radius %d is %.2f .' %(radius,area)
print(formatted_string2)

python_libraries=['Django','Flask','NumPy','Matplotlib','Pandas']
formatted_string3='The following are python libraries: %s' %(python_libraries)
print(formatted_string3)


# New Style String Formatting (str.format)
# This format was introduced in Python version 3.
first_name='Sneha'
last_name='Nair'
language='Python'
formatted_string1='Iam {} {}. I teach {}'.format(first_name,last_name,language)
print(formatted_string1)


a=4
b=3
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b,a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))


# Strings  and numbers
radius=10
pi=3.14
area=pi*radius**2
output='The area of the circle with radius {} is {:.2f}'.format(radius,area)
print(output)



# String Interpolation / f-Strings (Python 3.6+)
a=4
b=3
print(f'{a} +{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}%{b}={a%b}')
print(f'{a}//{b}={a//b}')
print(f'{a}**{b}={a**b}')


# Python Strings as Sequences of Characters

# Unpacking Characters
language='Python'
a,b,c,d,e,f=language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Accessing Characters in Strings by Index
language='Python'
first_letter=language[0]
print(first_letter)
second_letter=language[1]
print(second_letter)
last_index=len(language)-1
last_letter=language[last_index]
print(last_letter)


# start from right end we can use negative indexing. -1 is the last index.
last_letter2=language[-1]
print(last_letter2)
second_last=language[-2]
print(second_last)



# Slicing Python Strings
# In python we can slice strings into substrings.
language='Python'
first_three=language[0:3] # starts at 0 index and up to 3, 3 not included.
print(first_three)

last_three1=language[3:6]
print(last_three1)
last_three2=language[-3:]
print(last_three2)
last_three3=language[3:]
print(last_three3)



# Reversing a String
greeting='Hello, World!'
print(greeting[::-1])


# Skipping Characters While Slicing
# It is possible to skip characters while slicing by passing step argument to slice method.
language='Python'
pto=language[0:6:2]
print(pto)


# String Methods
# capitalize(): Converts the first character of the string to capital letter
challenge='thirty days of python'
print(challenge.capitalize())


# count(): returns occurrences of substring in string, count(substring, start=.., end=..).
#  The start is a starting indexing for counting and end is the last index to count.
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y',7,14))
print(challenge.count('th'))


# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))


# expandtabs(): 
# Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))


# find(): 
# Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))


# rfind(): 
# Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))


# format(): 
# formats string into a nicer output
first='Neha'
last="Nair"
age=20
country='Finland'
sentence='Hi, Iam {} {}. Iam {} years old. I live in {}.'.format(first,last,age,country)
print(sentence)


# index()
# Returns the lowest index of a substring, 
# additional arguments indicate starting and ending index (default 0 and string length - 1). 
# If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))
# print(challenge.index(sub_string,9)) # valueError
# If the substring is not found it raises a valueError.


# rindex():
#  Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
# print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on',8))



# isalnum():
#  Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False


# isalpha():
#  Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False


# isdecimal():
#  Checks if all characters in a string are decimal (0-9)
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True 
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed


# isdigit(): 
# Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True


# isnumeric():
#  Checks if all characters in a string are numbers or number related 
# (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

num='10.5'
print(num.isdigit())


# isidentifier():
#  Checks for a valid identifier - it checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower():
#  Checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper():
#  Checks if all alphabet characters in the string are uppercase
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True




# join(): 
# Returns a concatenated string
web_tech=['HTML','CSS','JavaScript','React']
result=' '.join(web_tech)
print(result)

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


# strip(): 
# Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))


# replace(): 
# Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python','coding'))


# split(): 
# Splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split())

challenge = 'thirty, days, of, python'
print(challenge.split(', '))



# title():
#  Returns a title cased string
challenge = 'thirty days of python'
print(challenge.title())


# swapcase():
#  Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


# startswith():
#  Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
print(challenge.startswith('Thirty'))

