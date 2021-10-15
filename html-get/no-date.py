from bs4 import BeautifulSoup
import requests
import re
import sys
from datetime import datetime
#from loop_list import *

#does the same of the other html parser but is used in the case that the last string
#is not in proper date format. 

fileName = 1
loop_list = open("loop_list.txt" , "r")

i = 1
for line in loop_list:
   #define where input comes from and make a soup
    source = requests.get(line).text

    soup = BeautifulSoup(source, 'lxml')

    #remove all href and img tags
    for a in soup.findAll('a'):
        del a['href']

    for tag in soup("img"):
        tag.decompose()

    #extract just the desired div from the soup
    match = soup.find('div', id='content')

    #remove all the extraneous \n characters
    clean = match.find_all(text = re.compile('\n'))
    for comment in clean:
        fixed_text = comment.replace('\n', '')
        comment.replace_with(fixed_text)

    

    #print(match)

    #date = soup.find_all("p")[-1].get_text()

    #print(date)

    #extract date of update from footer
    #date = soup.find_all("p")[-1].get_text()
    
    #cleanDate = date[8:]
    #print(cleanDate)
    #date_object =  datetime.strptime(cleanDate, "%B %d, %Y")
    #semiFinal = str(date_object)[:10]
    #fileName = semiFinal + ".html"
    
    
    
    #print(date)
    #fileName = str(date) + str(".html")
    #fileName = (re.sub(r"\s+", "", fileName))
    #fileName = (re.sub(r",","", fileName))

    # print output to terminal for viewing purposes
    #print(fileName)
    #print(clean)
    #print(match)
    outputName = str(fileName) + '.html'
    #copy output of cleaned version in html to file named for update date
    sys.stdout = open(outputName, 'w+')
    #names = open("names.txt" , "a+")
    f = open(outputName, "w+")
    print(match.encode("utf-8"))
    fileName += 1
    #print(fileName, file=names)

 


loop_list.close()








