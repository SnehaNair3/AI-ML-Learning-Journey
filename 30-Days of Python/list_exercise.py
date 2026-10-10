
# Declare an empty list
empty_list=list()

# Declare a list with more than 5 items
numbers=['one','two','three','four','five']

# Find the length of your list
print(len(numbers))

# Get the first item, the middle item and the last item of the list
print(numbers[0])
middle=len(numbers)//2
last_index=len(numbers)-1
print(numbers[middle])
print(numbers[last_index])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Sneha',24,165,'Single','Bangalore']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
first_company=it_companies[0]
print(first_company)
middle=len(it_companies)//2
print('Middle company : ', it_companies[middle])
last=len(it_companies)-1
print('Last company : ', it_companies[last])

# Print the list after modifying one of the companies
it_companies[0]='Nvidia'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Anthropic')
print(it_companies)

# Insert an IT company in the middle of the companies list
middle=len(it_companies)//2
it_companies.insert(middle,'Swiggy')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
print(it_companies)
it_companies[0]=it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
print('#;  '.join(it_companies))

# Check if a certain company exists in the it_companies list.
does_exist='IBM' in it_companies
print(does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)


# Slice out the first 3 companies from the list
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_three=it_companies[0:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three=it_companies[-3:]
print(last_three)

# Slice out the middle IT company or companies from the list
middle=len(it_companies)//2
middle_comp=it_companies[middle]
print(middle_comp)

# Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.remove(middle_comp)
print(it_companies)

# Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back=front_end+back_end
print(front_back)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=front_back.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)



# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages=ages.sort()
min_age=ages[0]
print(min_age)
max_age=ages[-1]
print(max_age)

# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)

print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
n=len(ages)
if n % 2 ==0 :
    median=(ages[n//2-1] + ages[n//2])/2
else:
    median=ages[n//2]  

print("median age : ", median)      


# Find the average age (sum of all items divided by their number )
avg_age=sum(ages)/len(ages)
print('Average age : ', avg_age)

# Find the range of the ages (max minus min)
ages.sort()
range=ages[-1]-ages[0]
print(range)

age_range=max(ages) - min(ages)
print(age_range)

# Compare the value of (min - average) and (max - average), use abs() method
min_age=min(ages)
max_ages=max(ages)
average_age=sum(ages)/len(ages)

print(abs(min_age-average_age))
print(abs(max_ages-average_age))


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]


# Find the middle country(ies) in the countries list
n=len(countries)

if n % 2 ==0 :
    middle_countries=countries[n//2-1 : n//2+1]
else:
    middle_countries=countries[n//2]    

print("Middle country : ", middle_countries)



# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# If the number of countries is even, divide the list into two equal halves.
# If the number is odd, the first half should contain one more country than the second half.
n=len(countries)
middle=(n+1)//2

first_half=countries[:middle]
second_half=countries[middle:]

print(first_half)
print(second_half)


# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch,ru,usa,*scandic=country

print(ch)
print(ru)
print(usa)
print(scandic)