import requests
from bs4 import BeautifulSoup
import pandas as pd

#Send HTTP request to the webpage
url = 'https://en.wikipedia.org/wiki/Cloud-computing_comparison'
response = requests.get(url)

#Check that request was successful
if response.status_code == 200:
    print('Request successful')
else:
    print('Failed to retrieve the webpage')
    
#Parse HTML content
soup = BeautifulSoup(response.content,'html.parser')

#Print web title to verify
print("Title: " + soup.title.text)

#Find the table containing the data (select first table by default)
table = soup.find('table')

#Extract table rows
rows = table.find_all('tr')

#Extract headers from the first row using <th> tags
headers = [header.text.strip() for header in rows[0].find_all('th')]

#Extract data and generate dataframe
data = []
for row in rows[1:]: #start from 2nd row
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)
    
df = pd.DataFrame(data, columns = headers)

#Print first rows
print(df.head())

#Save dataframe to .csv file
df.to_csv('scraped_data.csv', index = False)





