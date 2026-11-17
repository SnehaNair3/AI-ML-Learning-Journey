
# open('filename',mode) 
# mode - r,a,w,x,t,b 


# Opening Files for Reading
f=open('./files/reading_file_example.txt')
print(f)
# read(): read the whole text as string
txt=f.read()
print(type(txt))
print(txt)
f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file.
f = open('./files/reading_file_example.txt')
txt=f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first line
f = open('./files/reading_file_example.txt')
line=f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('./files/reading_file_example.txt')
lines=f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('./files/reading_file_example.txt')
lines=f.read().splitlines()
print(type(lines))
print(lines)
f.close()


# There is a new way of opening files using with - closes the files by itself. 
with open('./files/reading_file_example.txt') as f:
    lines=f.read().splitlines()
    print(type(lines))
    print(lines)


# Opening Files for Writing and Updating
# "a" - append - will append to the end of the file, if the file does not exist it creates a new file.
# "w" - write - will overwrite any existing content, if the file does not exist it creates.

with open('./files/reading_file_example.txt','a'):
    f.write('This text has to be appended at the end')

# The method below creates a new file, if the file does not exist:
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')


# Deleting Files
import os
os.remove('./files/example.txt')

# If the file does not exist, teh remove method will raise an error, so it is good to use a condition:
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')


# File Types 
# File with json Extension
# dictionary
person_dict={
    "name":"Alice",
    "country":"India",
    "city":"Mumbai",
    "skills":["Python","SQL","Java"]
}

# JSON : A string form  a dictionary
person_json="{'name':'Alice','country':'India','city':'Mumbai','skills'=['Python','SQL,'Java']}"
print(person_json)
print(person_dict)

# we use three quotes and make it multiple line to make it more readable
per_json='''{
  "name":"Alice",
  "country":"India",
  "city":"Mumbai",
  "skills":["Python","SQL","Java"]
  }'''
print(per_json)


# Changing JSON to Dictionary
# To change a JSON to a dictionary,
#  first we import the json module and then we use loads method.
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# change json to dictionary
person_dictionary=json.loads(person_json)
print(type(person_dictionary))
print(type(person_json))
print(person_dictionary)
print(person_dictionary['name'])

# Changing Dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json=json.dumps(person,indent=4)
print(type(person_json))
print(person_json)

# Saving as JSON File
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json','w',encoding='utf-8') as f:
    json.dump(person,f,ensure_ascii=False,indent=4)


# File with csv Extension
# Exxample:
# "name","country","city","skills"
# "Asabeneh","Finland","Helsinki","JavaScript" 
import csv
with open('./files/csv_example.csv') as f:
    csv_reader=csv.reader(f,delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'Column names are : {", ".join(row)}')
            line_count+=1
        else:
            print(f'\t{row[0]} is a taecher. H elives in {row[1]}, {row[2]}.')
        line_count+=1
    print(f'Number of lines:  {line_count}')    


# File with xlsx Extension
#  To read excel files we need to install xlrd package.   
import xlrd
excel_book=xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)


# File with xml Extension
# <?xml version="1.0"?>
# <person gender="female">
#   <name>Asabeneh</name>
#   <country>Finland</country>
#   <city>Helsinki</city>
#   <skills>
#     <skill>JavaScrip</skill>
#     <skill>React</skill>
#     <skill>Python</skill>
#   </skills>
# </person>

import xml.etree.ElementTree as ET
tree=ET.parse('./files/xml_example.xml')
root=tree.getroot()
print('Root tag: ',root.tag)
print('Attribute: ',root.attrib)
for child in root:
    print('field: ',child.tag)

    