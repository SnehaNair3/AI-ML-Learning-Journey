
# Import Functions from a Module and Renaming
# During importing we can rename the name of the module.
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p,gravity as g

print(total(11,9))

mass=100
weight=mass*g
print('weight: ', weight)

print(p['firstname'])


# Import Built-in Modules

# OS Module

# import the module
import os
# Creating a directory
os.mkdir('directory_name')
os.mkdir('trail_name')
# Changing the current directory
os.chdir('C:\Users\sneha\OneDrive\Documents\AI-ML LEARNING\30-Days of Python\.vscode\modules')
# Getting current working directory
os.getcwd()
# Removing directory
# os.rmdir('C:\Users\sneha\OneDrive\Documents\AI-ML LEARNING\30-Days of Python\trail_name')


# Sys Module
import sys

# print(sys.argv[0],sys.argv[1],sys.argv[2])
print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1],sys.argv[2]))

# sys.exit()

# To know the largest integer variable it takes
sys.maxsize

# To know environmant path
sys.path

# To know the version of pythn you are using
sys.version


# Statistics Module

from statistics import *

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))


# Math Module
import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))


from math import pi
print(pi)

from math import pi,sqrt,floor,ceil,log10
print(pi)
print(sqrt(100))


from math import *

from math import pi as PI
print(PI)



# String Module
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)


# Random Module
# random module which gives us a random number between 0 and 0.9999....
from random import random,randint
print(random())
print(randint(5,20))