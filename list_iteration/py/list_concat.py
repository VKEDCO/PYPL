#/usr/bin/python

###############################
## List concatenation in Py2
## 
## author: vladimir kulyukin
###############################

lst1 = [1, 2]
lst2 = ['a', 'b', 'c']
lst3 = [5, 10, 'd', 'e']

def list_concat2(x, y):
    return x + y

def list_concat3(x, y, z):
    return x + y + z

print 'list_concat2(lst1, lst2) = ' + repr(list_concat2(lst1, lst2))
print 'list_concat3(lst1, lst2, lst3) = ' + repr(list_concat3(lst1, lst2, lst3))
