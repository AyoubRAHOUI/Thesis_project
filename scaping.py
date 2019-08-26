# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://www.advfn.com/nasdaq/nasdaq.asp?companies=A'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
#for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
    #one_a_tag = soup.findAll('a')[i]
    #link = one_a_tag['href']
    #download_url = 'http://web.mta.info/developers/'+ link
    #urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
    #time.sleep(1) #pause the code for a sec
#s = str(soup.find_all('td')[29])
#print(s)
#indices_start = [i for i, x in enumerate(s) if x == ">"]
#print(indices_start[1])
#indices_end = [i for i, x in enumerate(s) if x == "<"]
#print(indices_end[2])
#res=""
#for i in range(indices_start[1]+1,indices_end[2]):
#    res=res+s[i]
#print(res)
#########################
#list_companies = [] (11) 12 13 (14) 15 16 (17) ... (878)//  ((881))

s = str(soup.find_all('td')[882])
print(s)
