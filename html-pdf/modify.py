#script to 

from bs4 import BeautifulSoup
import requests
import re
import sys


loop_list = open("fileNames.txt" , "r")


for line in loop_list:        #try:

    #define where input comes from and make a soup
    
    #print(line)
    f = open(line.rstrip('\n'), "r")

    #strip all line break characters as they interfere with soup working

    content = f.read()

    #print(content)

    #print(content)

    soup = BeautifulSoup(content, 'lxml')

    #find the last paragraph tag in the text which in most cases is the updated field

    date = soup.find_all("p")[-1].get_text()
    
        #remove all href and img tags
    for a in soup.findAll('a'):
        del a['href']

    for tag in soup("img"):
        tag.decompose()


    #print the last line of the file again at the beginning

    sys.stdout = open(line.rstrip('\n'), 'w+')
            #names = open("names.txt" , "a+")
    f = open(line.rstrip('\n'), 'w+')
    print(date)
    print(soup.encode("utf-8"))

        #print(fileName, file=names)

    


#loop_list.close()