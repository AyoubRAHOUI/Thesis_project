# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#returns index of the start of > in the html
def index_of_start(s):
    return [i for i, x in enumerate(s) if x == ">"]

#returns index of the end of < in the html
def index_of_end(s):
    return [i for i, x in enumerate(s) if x == "<"]
#deletes space in company name
def delete_space(s):
    i = len(s)
    if s[i-1] == ' ':
        return s[:i-1]
    else: return s

#create file containing list of companies
file_list = open("list_companies.txt","w+")

#all the url pages last letter matched with its last soup line index in html
url_pages = {'A':882, 'B':381, 'C':1029, 'D':285, 'E':396, 'F':390, 'G':306, 'H':327, 'I':447, 'J':108, 'K':129, 
'L':303, 'M':609, 'N':426, 'O':279, 'P':576, 'Q':78, 'R':312, 'S':807, 'T':543, 'U':195, 'V':219, 'W':219, 'X':45, 
'Y':33, 'Z':69, '0':48 }

for x in url_pages:
    # Set the URL you want to webscrape from
    url = 'https://www.advfn.com/nasdaq/nasdaq.asp?companies='+x
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object¶
    soup = BeautifulSoup(response.text, "html.parser")

    last_soup_phrase = url_pages[x]
    i = 11

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
            file_list.write(delete_space(name)+'\r\n')
            i +=3

file_list.close()
