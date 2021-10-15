#program for parsing html links to find all references to a specific string in the source
#this case looking for form entries on VIU webpages

from bs4 import BeautifulSoup
import requests
import re
import sys

#set default output to an empty text file
sys.stdout = open('link-list-clean.txt', 'w+')

#open the list of links that you are aiming to parse
loop_list = open("working-list.txt" , "r")

#loop through the list of links
for line in loop_list:

    source = requests.get(line).text
#turn html into object
    soup = BeautifulSoup(source, 'lxml')

    print(line + 'v')
#search the object for the specific string you want
    link = soup.select("a[href*=viu.ca/forms]")
    #link = soup.select_one("a[href*=viu.ca/forms]")

#print the output of your search with is an array but force to display as a string
    print(str(link) + '\n')








#links = soup.find_all('a', href=True)

#print(links)



#for link in links:
#    if link.find(text=re.compile("viu.ca/forms")):
#        thelink = link
#        break

#print(thelink)
#print(soup.prettify)