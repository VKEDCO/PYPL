#!/usr/bin/python

import sys

## change this path to where WebLogEntry.py
load_path = 'C:\\users\\vladimir\\programming\\nasa_wlog\\py_nasa_log\\'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from WebLogEntry import WebLogEntry

txt1  = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245'
wle1 = WebLogEntry();
if wle1.toWebLogEntry(txt1):
    print 'IP:      ' + wle1.getIP() + "\n",
    print 'TS:      ' + wle1.getTimestamp().toString() + "\n",
    print 'METHOD:  ' + wle1.getMethod() + "\n",
    print 'URL:     ' + wle1.getURL() + "\n",
    print 'PROTOCOL ' + wle1.getProtocol() + "\n",
    print 'STATUS   ' + str(wle1.getStatusCode()) + "\n",
    print 'TRBYTES  ' + str(wle1.getTransBytes()) + "\n",

    print "\n\nGENERATED HTML\n"
    print wle1.toHtmlUL()
else:
    print 'no WebLogEntry object created' + "\n",
