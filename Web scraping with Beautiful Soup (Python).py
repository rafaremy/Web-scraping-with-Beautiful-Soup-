#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install the necessary libraries.
get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')
get_ipython().system('pip install lxml')


# In[2]:


import pandas as pd
import requests

from bs4 import BeautifulSoup


# In[3]:


# Import the url.
# Create a variable to store the URL.
url = 'https://www.worldometers.info/world-population/population-by-country/'

# Create a vairable to store the information.
page = requests.get(url)

# Make contact with the website.
page


# In[5]:


# Get the information from the website.
if page.status_code == 200:
    html_doc = page.text

# Look at the html code.
# Create a variable to store the HTML info.
soup = BeautifulSoup(html_doc)

# Print the output in a readable format.
print(soup.prettify())


# In[6]:


# Navigate to the website and determine the table ID.
# Extract the contents of the table with the table ID.
table = soup.find('table', attrs={'id': 'example2'})

# View the information in a readable format.
print(table.prettify())


# In[7]:


# All of the rows of the table.
rows = table.find_all('tr')

# View the rows.
rows


# In[8]:


# Store the extracted data.
# Create an empty list.
output = []

# Specify the column names.
column_names = ['ID', 'Country (or dependency)', 'Population (2020)',
                'Yearly Change', 'Net Change', 'Density (P/Km2)',
                'Land Area (Km2)', 'Migrants (net)', 'Fert. Rate',
                'Med. Age', 'Urbn Pop', 'World Share']

# Create a for loop statement.
for country in rows:
    country_data = country.find_all('td')
    if country_data:
        # Extract the text within each element.
        country_text = [td.text for td in country_data]
        # Store data in a zip format for easy access.
        output.append(dict(zip(column_names, country_text)))
        
# View the result.
output


# In[9]:


# Create a DataFrame directly from the output.
data = pd.DataFrame(output)

# View the DataFrame.
data.head()


# In[10]:


# Save the DataFrame as a CSV file without index.
data.to_csv('countries.csv', index=False)


# In[11]:


# Create a JSON file.
import json

# Create a JSON file.
output_json = json.dumps(output)

# View the output.
output_json


# In[12]:


# Save the JSON file to .json.
with open('countries.json', 'w') as f:
    json.dump(output, f)


# In[13]:


# Read JSON using Pandas, output to .csv.
pd.read_json(output_json).to_csv('countries.csv', index=False)


# In[14]:


# Import the CSV file with Pandas.
# Data = pd.read_json('countries.json').
data = pd.read_csv('countries.csv')

# View.
data.head()


# In[15]:


# Open the JSON file with Pandas.
data = pd.read_json('countries.json')

# View the DataFrame.
data.head()


# In[ ]:




