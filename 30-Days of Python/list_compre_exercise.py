
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero=[x for x in numbers if x<0 or x==0]
print(neg_zero)


# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list=[num for row in list_of_lists for num in row]
print(flattened_list)

# Using list comprehension create the following list of tuples:
res=[(i,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(res)


# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries=[[country.upper(),country[:3].upper(),capital.upper()] for items in countries for country,capital in items]
print(flattened_countries)


# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list=[{'country': c.upper(), 'city': d.upper()} for items in countries for c,d in items]
print(dict_list)



# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full=[first+' '+last for name in names for first,last in name]
print(full)


# Write a lambda function which can solve a slope or y-intercept of linear functions.
# Linear equation : y=mx+b m=slope b=y_intercept
# calculate slope
slope=lambda x1,y1,x2,y2: (y2-y1)/(x2-x1)

# Calculate y-intercept
y_intercept=lambda x,y,m: y-(m*x)

print(slope(2, 3, 4, 7))       # 2.0
print(y_intercept(2, 3, 2))   # -1