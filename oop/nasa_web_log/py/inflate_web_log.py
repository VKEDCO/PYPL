#!/usr/bin/python

## @author: vladimir kulyukin

import sys
import re

## change this path to where you have saved your Py classes
load_path = 'C:\\users\\vladimir\\programming\\nasa_wlog\\py_nasa_log\\'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from WebLogEntry import WebLogEntry

## 1. get the command line arguments
lower = int(sys.argv[1]) ## lower bound
upper = int(sys.argv[2]) ## upper bound
top_n = int(sys.argv[3]) ## top_n
html_fp = sys.argv[4]    ## output html file path

## 2. Read in all text entries, convert them into WebLogEntry objects,
##    and place them into web_log_entries.
web_log_entries = []
for line in [line for line in sys.stdin.readlines()
             if re.match(r'\S+', line)]:
    wle = WebLogEntry()
    if wle.toWebLogEntry(line):
        web_log_entries.append(wle)
    else:
        print 'FAILURE: ' + line

## this is a debug print to show how many objects we have constructed        
print len(web_log_entries)

## 3. grep all entries whose transferred bytes are in [lower, upper]
web_log_entries = filter(lambda x: x.getTransBytes() >= lower and x.getTransBytes() <= upper, web_log_entries)
## 4. sort all entries in the range from highest to lowest
web_log_entries.sort(key=lambda x: x.getTransBytes(), reverse=True)


with open(html_fp, 'w') as outstream:
    ## 5. open an HTML file and write an HTML header into it
    outstream.write("<html>\n")
    outstream.write("<head>\n")
    outstream.write("<title>Nasa Web Log Entries</title>\n")
    outstream.write("</head>\n")
    outstream.write("<body>\n")
    outstream.write("<h1>Found Nasa Web Log Entries</h1>\n")

    ## 6. convert each WebLogEntry object into an html ul and write it out into an html file
    for i in xrange(top_n):
        if i < len(web_log_entries):
	    outstream.write(web_log_entries[i].toHtmlUL())
	    outstream.write("<hr><br>\n")

    ## 7. match the body and html tags.            
    outstream.write("</body>\n")
    outstream.write("</head>\n")
    outstream.write("</html>\n")

