# even or odd
def even_odd(num):
    if num%2 ==0:
        print("Even")
    else:
        print("Odd")    
even_odd(31)        
even_odd(90)

# factorial
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact   
factorial(3)     
factorial(5)    

# Sum of all natural numbers till the number provided
def sum_natural(n):
    return n*(n+1)/2
sum_natural(5)
sum_natural(6)
# Or
def sum_natural2(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum
sum_natural2(5)    
sum_natural2(6)    


def func_1(name,age=30):
    print("name : ",name)
    print("age : ",age)
func_1("Ravi",25)    
func_1("Bob") 

# Lambda Functions
sum=lambda a,b:a+b
print(sum(4,5))

x=lambda a: "even" if a%2==0 else "odd"
print(x(101))
print(x(10))
print(x(13))

x=lambda a:a+10
print(x(10))

# Map, Reduce, Filter

# Map Function 
# Area of the circle
# Method 1
import math
def area(r):
    return math.pi*(r**2)
radii=[1,2,3,4,5]
areas=[]
for r in radii:
    a=area(r)
    areas.append(a) 
print(areas)  

# Method 2 - using map function
import math
def find_area(r):
    return math.pi*(r**2)
radiis=[1,2,3,4,5]
list(map(find_area,radiis))

# Convert celcius to Fahrenheit
temps=[("Mumbai",35),("Berlin",12),("Tokyo",25),("Sydney",30)]
type(temps)
print(len(temps))

# traditional using for loops
res=[]
for city,temp in temps:
    fahrenheit=(9/5)*temp+32
    res.append((city,fahrenheit))  
print(res)

# using map function
cel_to_f=lambda data:(data[0],(9/5)*data[1]+32)
# map(f,iterable)
map(cel_to_f,temps)
list(map(cel_to_f,temps))

# Filter function - filters the data
# create a list that contains only the numbers greater than avg
import statistics
data=[1,2,3,6,7,9,11,15]
avg=statistics.mean(data)
print(avg)
filter(lambda x : x>avg,data)
list(filter(lambda x : x>avg,data))

# Getting rid of the null/NaN  values
item=["Neha","Sathya",9,0,"",0.0,12]
filter(None,item)
list(filter(None,item))

# Reduce Function - not built-in in python from python3
# moved to python library called functools - reduce
# reduce(f,data)
from functools import reduce
# Multiply all the items in a list
data=[1,2,3,4,5]
multiply=lambda x,y : x*y
reduce(multiply,data)

# traditional method
res=1
for i in data:
    res=res*i
print(res)   


# sum all items in the list
sum=lambda x,y:x+y
reduce(sum,data)


