__metaclass__ = type

## @author: vladimir kulyukin

import re
from Timestamp import Timestamp

class WebLogEntry:

    WEB_LOG_ENTRY_PAT  = '^([\d\.\W\w-]+)\s+(- -)\s+\[(.+)\]\s+\"(.+)\s+(.+)\s+(.+)\"\s+(\d+)\s+((\d+)|(-))$'
    WEB_LOG_ENTRY_PAT2 = '^([\d\.\W\w-]+)\s+(- -)\s+\[(.+)\]\s+\"(.+)\s+(.+)"\s+(\d+)\s+((\d+)|(-))$'
    
    def __init__(self, ip='', timestamp='', method='', url='', protocol='', status=0, trans_bytes=0):
        self.mIP = ip
        self.mTimestamp = timestamp
        self.mMethod = method
        self.mURL = url
        self.mProtocol = protocol
        self.mStatusCode = status
        self.mTransBytes = trans_bytes

    def toWebLogEntry(self, txt):
        match = re.match(WebLogEntry.WEB_LOG_ENTRY_PAT, txt)
        if match != None:
            trbytes  =  0
            if match.group(8) == '-':
                trbytes = 0
            else:
                trbytes = int(match.group(8))
            self.mIP = match.group(1)
            tm = Timestamp()
            self.mTimestamp = tm.toTimestamp(match.group(3))
            self.mMethod = match.group(4)
            self.mURL = match.group(5)
            self.mProtocol = match.group(6)
            self.mStatusCode = int(match.group(7))
            self.mTransBytes = trbytes
            return True
        else:
            match = re.match(WebLogEntry.WEB_LOG_ENTRY_PAT2, txt)
            if match != None:
                trbytes = 0
                if match.group(7) == '-':
                    trbytes = 0
                else:
                    trbytes = int(match.group(7))
                self.mIP = match.group(1)
                tm = Timestamp()
                self.mTimestamp = tm.toTimestamp(match.group(3))
                self.mMethod = match.group(4)
                self.mURL = match.group(5)
                self.mProtocol = 'UNKNOWN'
                self.mStatusCode = int(match.group(6))
                self.mTransBytes = trbytes
                return True
            else:
                return False

    ## ========== Getters & Setters ===============
    def getIP(self): return self.mIP
    def setIP(self, ip): self.mIP = ip

    def getMethod(self): return self.mMethod
    def setMethod(self, m): self.mMethod = m

    def getTimestamp(self): return self.mTimestamp
    def setTimestamp(self, tm): self.mTimestamp = tm

    def getURL(self): return self.mURL
    def setURL(self, url): self.mURL = url

    def getProtocol(self): return self.mProtocol
    def setProtocol(self, p): self.mProtocol = p

    def getStatusCode(self): return self.mStatusCode
    def setStatusCode(self, sc): self.mStatusCode = sc
    
    def getTransBytes(self): return self.mTransBytes
    def setTransBytes(self, tb): self.mTransBytes = tb

    ## convert a WebLogEntry object and convert it into an HTML text.
    def toHtmlUL (self):
        html_ul = "<UL>\n"
        html_ul += '<li>' + 'IP:       ' + self.getIP() + '</li>' + "\n"
        html_ul += '<li>' + 'TIME:     ' + self.getTimestamp().toString() + '</li>' + "\n"
        html_ul += '<li>' + 'METHOD:   ' + self.getMethod() + '</li>' + "\n"
        html_ul += '<li>' + 'URL:      ' + self.getURL() + '</li>' + "\n"
        html_ul += '<li>' + 'PROTOCOL: ' + self.getProtocol() + '</li>' + "\n"
        html_ul += '<li>' + 'STATUS:   ' + str(self.getStatusCode()) + '</li>' + "\n"
        html_ul += '<li>' + 'BYTES:    ' + str(self.getTransBytes()) + '</li>' + "\n"
        html_ul += '</UL>' + "\n"
        return html_ul

    
