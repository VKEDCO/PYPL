__metaclass__ = type

## @author: vladimir kulyukin

import re
import sys

class Timestamp:
    
    TIMESTAMP_PAT = r'(\d{2})\/(\w{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2})\s+(-\d+)'
    
    def __init__(self, month=1, day=1, year=0, hour=0, mins=0, secs=0):
        self.mMonth = month
        self.mDay = day
        self.mYear = year
        self.mHour = hour
        self.mMins = mins
        self.mSecs = secs

    def toTimestamp(self, txt):
        match = re.match(Timestamp.TIMESTAMP_PAT, txt)
        if match != None:
            self.mDay   = match.group(1)
            self.mMonth = match.group(2)
            self.mYear  = match.group(3)
            self.mHour  = match.group(4)
            self.mMins  = match.group(5)
            self.mSecs  = match.group(6)
            return self
        else:
            return None

    def getYear(self): return self.mYear
    def setYear(self, year): self.mYear = year

    def getMonth(self): return self.mMonth
    def setMonth(self, month): self.mMonth = month

    def getDay(self): return self.mDay
    def setDay(self, day): self.mDay = day

    def getHour(self): return self.mHour
    def setHour(self, hour): self.mHour = hour

    def getMins(self): return self.mMins
    def setMins(self, mins): self.mMins = mins

    def getSecs(self): return self.mSecs
    def setSecs(self, secs): self.mSecs = secs

    def toString(self):
        return str(self.getDay())+'/'+str(self.getMonth())+'/'+str(self.getYear())+' '+\
            str(self.getHour())+':'+str(self.getMins())+':'+str(self.getSecs())

