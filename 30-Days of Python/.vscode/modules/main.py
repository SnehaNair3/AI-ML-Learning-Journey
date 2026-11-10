
import mymodule
print(mymodule.generate_full_name('Alice','Mathew'))

from mymodule import generate_full_name,sum_two_nums,person,gravity

print(generate_full_name('Mili','Frederick'))
print(sum_two_nums(10,30))

mass=100
weight=mass*gravity
print('Weight : ', weight)

print(person['firstname'])


