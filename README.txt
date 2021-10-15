Collection of scripts used for parsing wayback machine archived webpages for
main content divs and printing the output to a pdf.

Collect raw data from the wayback machine search function using the link:

http://web.archive.org/cdx/search/cdx?url=example.com*&output=txt&from=2010&to=2018

Copy all desired data, copy into file called 'raw.txt'
you will also need to input an example link in the report script with the date numbers removed. 
Run report script to get links for the main script to parse in file called 'link-list.txt'

Now you can run 'html-parse.py' which will parse the webpages and grab the content div
and print it to a file that is named for the last paragraph field in the div (needs to be in date form)

If the last paragraph is not in the date form then you should use 'no-date.py' unforunately
this means that you need to name the files manually.

