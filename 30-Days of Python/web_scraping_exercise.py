# 1 -  Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').


# Step 1: Send a request and parse the HTML
import requests
from bs4 import BeautifulSoup
import json

url1 = 'http://www.bu.edu/president/boston-university-facts-stats/'

response=requests.get(url1)
print(response)
soup=BeautifulSoup(response.text,'html.parser')


# Step 2: Extract the data from the website
print(soup.prettify())

data=soup.get_text(separator='\n',strip=True)
print(data)
# Here, data contains the extracted text as a Python string.

# Step 3: Store the data in a JSON file
# Use Python's json.dump() function to write the data into a JSON file.
with open('result_json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

# w - opens the file in write mode 
# encoding='utf-8' - supports different characters
# json.dump(data, f) - writes the data into teh JSON file
# ensure_ascii=False  - preserves non-ASCII characters
# indent=4   -  Makes the JSON file readable   
# Your JSON file will be created in your current working directory.

# Step 4: Verify the JSON file
# You can read the file back into Python to verify that it was saved correctly.
with open('result_json','r',encoding='utf-8') as f:
    saved_data=json.load(f)

print(saved_data)    

# The code above stores all the extracted webpage text as a single JSON string.
# scrape the website and save its information as structured JSON, you could organize the data into a dictionary instead.

data={
    'title': soup.title.get_text(strip=True) if soup.title else '',
    'headings': [h.get_text(strip=True) for h in soup.find_all(['h1','h2','h3'])],
    'paragraphs': [p.get_text(strip=True) for p in soup.find_all('p')]
}


with open('res_json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=4)


# json.dump() → Writes Python data to a JSON file.
# json.dumps() → Converts Python data into a JSON-formatted string.
# json.load() → Reads data from a JSON file.
# json.loads() → Converts a JSON-formatted string into Python data.    

with open('res_json','r',encoding='utf-8') as f:
    sav_data=json.load(f)

print(sav_data)    

# dump → Save to a file.
# dumps → Save as a string in memory.



# 2 - Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

# Step 1: Import the libraries and request the webpage
import requests
from bs4 import BeautifulSoup
import json

url2='https://archive.ics.uci.edu/ml/datasets.php'

response=requests.get(url2)
soup=BeautifulSoup(response.text,'html.parser')

# requests.get(url) fetches the webpage.
# BeautifulSoup() parses the HTML.
# soup contains the parsed HTML, which you can search to find the table.

# Step 2: Find the HTML table
# First, check whether the webpage contains any tables.
tables=soup.find_all('table')

print(len(tables))  
# This returns the number of HTML tables found on the page.

# To inspect the first table, use:
print(tables[0].prettify())

# Step 3: Extract the table data
table=tables[0]

# Extract column headings
headers=[]

for th in table.find_all('th'):
    headers.append(th.get_text(strip=True))

print(headers)

# extract the rows:

rows=[]

for tr in table.find_all('tr'):
    cells=tr.find_all(['td','th'])
    row=[cell.get_text(strip=True) for cell in cells]

    if row:
        rows.append(row)

print(rows)
# rows contains the table data as a list of lists.



# Step 4: Convert the table into a structured format
# For JSON, it's usually helpful to represent each table row as a dictionary, using the column headings as keys.
data=[]

for row in rows[1:]:
    if len(row) == len(headers):
        record={}

        for i in range(len(headers)):
            record[headers[i]]==row[i]

            data.append(record)

# Step 5: Save the data as a JSON file
with open('uci_datasets.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

print('Table data saved to uci_datasets.json')


# Complete code
import requests
from bs4 import BeautifulSoup
import json

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables
tables = soup.find_all('table')

if not tables:
    print("No HTML tables found on the webpage.")

else:
    table = tables[0]

    # Extract headers
    header_row = table.find('tr')
    headers = [
        th.get_text(strip=True)
        for th in header_row.find_all(['th', 'td'])
    ]

    # Extract table rows
    data = []

    for tr in table.find_all('tr')[1:]:
        cells = tr.find_all(['td', 'th'])
        row = [cell.get_text(strip=True) for cell in cells]

        if len(row) == len(headers):
            record = {}

            for i in range(len(headers)):
                record[headers[i]] = row[i]

            data.append(record)

    # Save as JSON
    with open('uci_datasets.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data saved successfully!")
    print(f"Total records extracted: {len(data)}")


# <table>
#   <!-- Header Row -->
#   <tr>
#     <th>Header 1</th>
#     <th>Header 2</th>
#   </tr>
#   <!-- Data Row 1 -->
#   <tr>
#     <td>Data A</td>
#     <td>Data B</td>
#   </tr>
#   <!-- Data Row 2 -->
#   <tr>
#     <td>Data C</td>
#     <td>Data D</td>
#   </tr>
# </table>    




# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
import requests
from bs4 import BeautifulSoup
import json

url3='https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response=requests.get(url3)
print(response)
soup=BeautifulSoup(response.text,'html.parser')
print(soup.title)
print(soup.title.get_text())
print(soup.body)
print(response.status_code)


tables=soup.find_all('table')
print(len(tables))
table=tables[0]

# Extract the table headers
headers=[]

header_row=table.find('tr')

for th in header_row.find_all(['th','td']):
    headers.append(th.get_text(' ',strip=True))

print(headers)


# Extract the table rows
rows=[]

for tr in table.find_all('tr')[1:]:
    cells=tr.find_all(['th','td'])

    row=[]

    for cell in cells:
        row.append(cell.get_text(' ',strip=True))

    if row:
        rows.append(row) 

print(rows[:5])      

# find_all('tr') finds all table rows.
# [1:] skips the first row, which we are treating as the header.
# find_all(['th', 'td']) finds header cells and regular data cells.
# get_text(' ', strip=True) extracts the text and adds spaces between nested text elements.
# Each row is stored as a list inside rows.

# Convert the rows into dictionaries
data=[]

for row in rows:
    if len(row) == len(headers):
        record={}

        for i in range(len(headers)):
            record[headers[i]]=row[i]

        data.append(record)    


# Save the data as a JSON file
with open('presidents.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

print('Presidents data saved successfully!')
print('Total records:', len(data))    
