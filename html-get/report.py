import re
import sys


#takes input from wayback machine search function (http://web.archive.org/cdx/search/cdx?url=example.com*&output=txt&from=2010&to=2018) copy directly into 
#raw.txt file

loop_list = open("raw.txt" , "r")

sys.stdout = open('numbers.txt', 'w+')

#loops through the raw data file and grabs all of the date url info and saves it to the numbers.txt file which is used for later
for line in loop_list:
    
    print(line.split(' ', )[1])

#not really used but a function call to do the same as a loop
def insert_date(string, index):
    return string[:index] + 'number' + string[index:]

#unfortunately need to manually input archive url for the site that you are looking for in order to properly build the url
#also need to remove the date number section of the url when inserting in the field so that it can be replaced with the one from
#the numbers file

base_url = 'https://web.archive.org/web/https://www2.viu.ca/calendar/Business/abt.asp'

loop_list = open("numbers.txt" , "r")

sys.stdout = open('loop_list.txt', 'w+')


#loop through list of numbers and input them into your provided url so that it can be routable with the scraping script
for line in loop_list:
    
    new_url = base_url[:28] + line + base_url[27:] 
    print(new_url)


