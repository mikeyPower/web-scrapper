# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://www.brainyquote.com/quote_of_the_day'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

#quote is in meta tag
quote = soup.findAll('meta')
quote_of_the_day = ""


#find the twtter description as the quote lies in that reference
for i in quote:
    try:
        if(i.attrs['name']=='twitter:description'):
        #print(i.attrs['content'])
            quote_of_the_day = i.attrs['content']
    except:
        a = "Not everything that is faced can be changed, but nothing can be changed until it is faced.-James Baldwin"


#check if quote of the day string is empty
if not quote_of_the_day:
    quote_of_the_day = a

#remove quotes
newstr = quote_of_the_day.replace('"', "")

print(newstr)
#split string into quote and author
spit = newstr.rsplit('-',1)
#print(spit)
