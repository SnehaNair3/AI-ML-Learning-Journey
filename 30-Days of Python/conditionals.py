
# if condition
a=3
if a > 0 :
    print('A is a positive number.')


# if-else condition
a=3
if a > 0:
    print('a is a positive number.')
else:
    print('a is a negative number.')


# If Elif Else
a=0
if a <0 :
    print('a is a negative number')
elif a > 0:
    print('a is a positive number')
else:
    print('a is zero.') 



# Short Hand
# code if condtion else code 
a=-3
print('a is positive') if a >0 else print('a is negative')


# Nested Conditions
a=0
if a > 0 :
    if a % 2 ==0:
        print('A is  a positive and even number')
    else:
        print('A is a positive and odd number')
elif a < 0 :
    print('A is a negative number')
else:
    print('A is zero')                


# If Condition and Logical Operators
a=0
if a > 0 and a%2 ==0 :
    print('a is an even an positive integer.')
elif a > 0 and a%2 !=0:
    print('a is an odd and positve integer.')
elif a ==0:
    print('a is zero.')
else:
    print('a is a negative integer.')            



# If and Or Logical Operators
user='James'
access_level=3
if user=='admin' or access_level >=4 :
    print('Access granted!')
else:
    print('Access denied!')    

