__metaclass__ = type

class Date:

    def __init__(self, m=1, d=1, y=0):
        self.mMonth = m
        self.mDay   = d
        self.mYear  = y

    def getYear(self):
        return self.mYear

    def setYear(self, y):
        self.mYear = y

    def getMonth(self):
        return self.mMonth

    def setMonth(self, m):
        self.mMonth = m

    def getDay(self):
        return self.mDay
        
    def setDay(self, d):
        self.mDay = d

    def toMDYString(self):
        return str(self.mMonth) + '/' + str(self.mDay) + '/' + str(self.mYear)

    def toYMDString(self):
        return str(self.mYear) + '/' + str(self.mMonth) + '/' + str(self.mDay)

