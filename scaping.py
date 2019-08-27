# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#file_list = open("list_companies.txt","w+")







# Set the URL you want to webscrape from
url = 'https://www.advfn.com/nasdaq/nasdaq.asp?companies=A'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")


#########################
#list_companies = [] (11) 12 13 (14) 15 16 (17).....(23)
#                    (29) 30 31 (32)...... .........(68)
#                    (74)...........................(83)
#                    (89) ..........................(89)
#                    (95)...........................(128)
#                    ()
#                    
#  ... (878)//  ((881))

 
def index_of_start(s):
    return [i for i, x in enumerate(s) if x == ">"]

def index_of_end(s):
    return [i for i, x in enumerate(s) if x == "<"]

def delete_space(s):
    i = len(s)
    if s[i-1] == ' ':
        return s[:i-1]
    else: return s


last_soup_phrase = 882
first_soup_phrase = 11
list_companies = []
i = first_soup_phrase
#scrapping line by line the exact name of the company in the web page.
while i < last_soup_phrase :
    #phrase contains the hole line of html of one company
    phrase = str(soup.find_all('td')[i])
    if phrase[18] != 'a':
        i +=3
    else:
        #location of the name inside phrase
        name = ""
        for j in range( index_of_start(phrase)[1]+1 , index_of_end(phrase)[2] ):
            name =name + phrase[j]
        list_companies.append(delete_space(name))
        i +=3
print(list_companies)





