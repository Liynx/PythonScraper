from bs4 import BeautifulSoup
import requests
import re
import sys
from datetime import datetime
#from loop_list import *



loop_list = open("loop_list.txt" , "r")

#loop through the list of links created by the reporting script
for line in loop_list:

    #try:

   #define where input comes from and make a soup
        source = requests.get(line).text

        soup = BeautifulSoup(source, 'lxml')

    #remove all href and img tags
        for a in soup.findAll('a'):
            del a['href']

        for tag in soup("img"):
            tag.decompose()

    #extract just the desired div or html element from the soup
        match = soup.find('div', id='content')

    #remove all the extraneous \n characters
        clean = match.find_all(text = re.compile('\n'))
        for comment in clean:
            fixed_text = comment.replace('\n', '')
            comment.replace_with(fixed_text)


    #extract date of update from footer
        date = soup.find_all("p")[-1].get_text()
        spacelessDate = (re.sub(r" ", "", date))
        colonGone = (re.sub(r":", "", spacelessDate))
        cleanDate = colonGone[7:]

        #monthSplit = cleanDate[:-7]
        #dateSplit = cleanDate[-7:]
       
        #finalDate = (monthSplit + " " + dateSplit)
        date_object =  datetime.strptime(cleanDate, "%B%d,%Y")
        semiFinal = str(date_object)[:10]
        fileName = semiFinal + ".html"
        

    #except ValueError:
        #continue
    
    
    #print(date)
    #fileName = str(date) + str(".html")
    #fileName = (re.sub(r"\s+", "", fileName))
    #fileName = (re.sub(r",","", fileName))

    # print output to terminal for viewing purposes
    #print(fileName)
    #print(clean)
    #print(match)

    #copy output of cleaned version in html to file named for update date
        sys.stdout = open(fileName, 'w+')
        #names = open("names.txt" , "a+")
        f = open(fileName, "w+")
        print(match.encode("utf-8"))

    #print(fileName, file=names)

 


loop_list.close()



