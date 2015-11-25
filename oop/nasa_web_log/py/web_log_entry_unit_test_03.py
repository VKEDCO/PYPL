#!/usr/bin/python

## @author: vladimir kulyukin

import sys

## change this path to where WebLogEntry.py
load_path = 'C:\\users\\vladimir\\programming\\nasa_wlog\\py_nasa_log\\'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from WebLogEntry import WebLogEntry

txt3 = 'pipe2.nyc.pipeline.com - - [01/Jul/1995:22:41:11 -0400] "GET /shuttle/missions/sts-71/sts-71-patch-small.gif" 200 12054'
wle3 = WebLogEntry();

if wle3.toWebLogEntry(txt3):
    print 'IP:      ' + wle3.getIP() + "\n",
    print 'TS:      ' + wle3.getTimestamp().toString() + "\n",
    print 'METHOD:  ' + wle3.getMethod() + "\n",
    print 'URL:     ' + wle3.getURL() + "\n",
    print 'PROTOCOL ' + wle3.getProtocol() + "\n",
    print 'STATUS   ' + str(wle3.getStatusCode()) + "\n",
    print 'TRBYTES  ' + str(wle3.getTransBytes()) + "\n",

    print "\n\nGENERATED HTML\n"
    print wle3.toHtmlUL()
else:
    print 'no WebLogEntry object created' + "\n",
