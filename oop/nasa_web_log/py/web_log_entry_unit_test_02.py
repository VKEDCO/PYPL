#!/usr/bin/python

import sys

## change this path to where WebLogEntry.py
load_path = 'C:\\users\\vladimir\\programming\\nasa_wlog\\py_nasa_log\\'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from WebLogEntry import WebLogEntry

txt2 = '199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 -'
wle2 = WebLogEntry();

if wle2.toWebLogEntry(txt2):
    print 'IP:      ' + wle2.getIP() + "\n",
    print 'TS:      ' + wle2.getTimestamp().toString() + "\n",
    print 'METHOD:  ' + wle2.getMethod() + "\n",
    print 'URL:     ' + wle2.getURL() + "\n",
    print 'PROTOCOL ' + wle2.getProtocol() + "\n",
    print 'STATUS   ' + str(wle2.getStatusCode()) + "\n",
    print 'TRBYTES  ' + str(wle2.getTransBytes()) + "\n",

    print "\n\nGENERATED HTML\n"
    print wle2.toHtmlUL()
else:
    print 'no WebLogEntry object created' + "\n",
