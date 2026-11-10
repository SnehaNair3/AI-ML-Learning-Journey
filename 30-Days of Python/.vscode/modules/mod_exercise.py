
# Exercises: Level 1

# Write a function which generates a six digit/character random_user_id
from random import random
def random_user_id():
    return random()
print(random_user_id())


# Generate a six-character random user ID
import random
import string
def random_user_id2():
    characters=string.ascii_letters+string.digits
    user_id=''.join(random.choices(characters,k=6))
    return user_id
print(random_user_id2())    

# string.ascii_letters → Contains A-Z and a-z.
# string.digits → Contains 0-9.
# random.choices() → Randomly selects characters.
# k=6 → Selects 6 characters.
# ''.join() → Combines the selected characters into a string.



# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

import random
def rgb_color_gen():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())
print(rgb_color_gen())


# Exercises: Level 2

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string

def list_of_hexa_colors(n):
    hexa=string.digits + 'abcdef'

    colors=[]

    for i in range(n):
        color = '#' + ''.join(random.choices(hexa,k=6))
        colors.append(color)

    return colors

print(list_of_hexa_colors(6))    
print(list_of_hexa_colors(3))   


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
import random

def list_of_rgb_colors(n):
    rgb_colors=[]

    for i in range(n):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        rgb_color=(r,g,b)

        rgb_colors.append(rgb_color)
    return rgb_colors
print(list_of_rgb_colors(3))    
print(list_of_rgb_colors(5))    


# Write a function generate_colors which can generate any number of hexa or rgb colors.
import random
import string

def generate_colors(color_type,n):
    colors=[]

    if color_type == 'hexa':
        hexa=string.digits + 'abcdef'

        for i in range(n):
            color=''.join(random.choices(hexa, k=6))
            colors.append(color)

    if color_type =='rgb':
        for i in range(n):
            r=random.randint(0,255)        
            g=random.randint(0,255)        
            b=random.randint(0,255)  

            color=f'rgb({r},{g},{b})'
            colors.append(color)   

    return colors

print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))

print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))           



# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random
def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list
print(shuffle_list([1,2,3,4,5]))


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def random_array():
    arr=[]
    for i in range(7):
        arr.append(random.randint(0,9))
    return arr
print(random_array())    
print(random_array())    