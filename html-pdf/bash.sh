#!/bin/bash

#loops through all files in working directory and prints the anames of all html files
#intended to be piped into an output file called fileNames.txt for use by other scripts

for f in *.html; 
do printf '%s\n' "${f%.html}"".html";

done


#####for i in *; do name="${i%.*}"; mv "$i" "${name}-business${i#$name}"; done
