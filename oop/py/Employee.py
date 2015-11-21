__metaclass__ = type

class Employee:
    
    def __init__(self, fn='', ln='', hd=None):
        self.mFirstName = fn
        self.mLastName = ln
        self.mHireDate = hd

    def getFirstName(self):
        return self.mFirstName

    def getLastName(self):
        return self.mLastName

    def getHireDate(self):
        return self.mHireDate

    def setFirstName(self, fn):
        self.mFirstName = fn

    def setLastName(self, ln):
        self.mLastName = ln

    def setHireDate(self, hd):
        self.mHireDate = hd

