
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



    