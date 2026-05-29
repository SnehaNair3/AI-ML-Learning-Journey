# print("Hello World!")

# packages
# requests - Download web pages and data
# pandas - Work with spreadsheets and data
# numpy - Fast mathematical operations
# openai - Connect to AI models
# beautifulsoup4 - Extract data from websites

import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200



