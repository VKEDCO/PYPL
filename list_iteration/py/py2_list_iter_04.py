## list iteration methods in Py
## author: Vladimir Kulyukin

lst = [1, 2, 3, 4]

## destructively modifying lst by setting them to
## their square roots.
for i in xrange(0, len(lst)):
    lst[i] **= .5
for x in lst: print x

## output of the last for-loop is
## 1.0
## 1.41421356237
## 1.73205080757
## 2.0
