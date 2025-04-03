import requests
from bs4 import BeautifulSoup
import pandas as pd
#import os
from urllib.parse import urljoin

#Send HTTP request to the webpage
url = 'https://arxiv.org/list/astro-ph/new'
response = requests.get(url)

#Check that request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    print('Request successful')
else:
    print('Failed to retrieve the webpage. Status code: ', response.status_code)
    exit()
    
#Find the document link
document_link = soup.find('a', {'title': 'Download PDF'})['href']
print('Document link found: ', document_link)

#Handle relative URL to full URL
base_url = 'https://arxiv.org/list/astro-ph/new'
full_url = urljoin(base_url, document_link)

print('Full URL: ', full_url)

#Download the document
document_response = requests.get(full_url)

#Check document request is successful
if document_response.status_code == 200:
    with open('report.pdf', 'wb') as file:
        file.write(document_response.content)
    print('Document loaded successfully.')
else:
    print('Failed to download document. Status code:', document_response.status_code)

