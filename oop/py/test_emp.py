#!/usr/bin/python

import sys

## change this path to where Date.py is defined.
load_path = '/home/vladimir/programming/py/oop/'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from Employee import Employee
from Date import Date

hire_date = Date()
hire_date.setMonth(10)
hire_date.setDay(10)
hire_date.setYear(2010)

emp = Employee()
emp.setFirstName('John')
emp.setLastName('Nicholson')
emp.setHireDate(hire_date)

print 'First Name: ' + emp.getFirstName()
print 'Last  Name: ' + emp.getLastName()
print 'Hire  Date: ' +  emp.getHireDate().toMDYString()
