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
