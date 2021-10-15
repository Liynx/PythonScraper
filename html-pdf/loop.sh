#!/bin/bash

#bash script to print all html files in folder to pdfs
#takes filenames from the other scripts output file and modifies them to remove the .html
#then appends the .pdf to the output name 

cat fileNames.txt | while read -r fileName
do

    fileName=$fileName
    changed=${fileName::-5}
    ext1=".html"
    ext2=".pdf"

    sudo wkhtmltopdf  --disable-smart-shrinking  --lowquality --enable-external-links --enable-internal-links --load-error-handling ignore $fileName $changed$ext2

done

    