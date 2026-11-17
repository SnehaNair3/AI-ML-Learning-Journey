# numpy 
import numpy as np

lst=[1,2,3,4,5]
np_arr=np.array(lst)
print(np_arr)
print(type(np_arr))
print(len(np_arr))
print('multiplied array : ',np_arr*2)
print('Added 2 array : ',np_arr+2)


# pandas 
import pandas as pd

# webbrowser 
import webbrowser

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]
# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)


# To see the installed packages on our machine. We can use pip followed by list.
# pip list 
# pip show pandas 
# pip show --verbose pandas 

# To open a network connection, we need a package called requests 
# - it allows to open a network connection 
# and to implement CRUD(create, read, update and delete) operations. 
# pip install requests 
# get(): to open a network and fetch data from url - it returns a response object
# status_code: After we fetched data, we can check the status of the operation (success, error, etc)
# headers: To check the header types
# text: to extract the text from the fetched response object
# json: to extract json data 
import requests

url='https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a w

response=requests.get(url)  # opening a network and fetching a data
print(response)
print(response.status_code)   # status code, success:200
print(response.headers) # headers information
print(response.text)  # gives all the text from the page

# API 
# Let us read from an API. 
import requests
url='https://restcountries.eu/rest/v2/all'
response=requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
countries=response.json()
print(countries[:1])


# A package is actually a folder containing one or more module files. 
# a module can contain multiple objects, such as classes, functions, etc. 
