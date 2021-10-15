#bash script for appending css modification to the beginning of html files

#!/bin/bash

#loop through all files in working directory
for i in *.html; do

    { echo '<style>
        table, tr, td, th, tbody, thead, tfoot {
                page-break-inside: avoid !important;
        }
        
        table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 30px;
        }

        table,
        th,
        td {
                border: 1px solid #999;
                padding: 2px 5px 2px 5px;
        }
</style>'; cat "$i"; } > /tmp/_$$file &&
    mv /tmp/_$$file "$i"

#output the contents of a file, echo your string into it then rename the tmp file to the same
#as the original

done