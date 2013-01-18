## bugs to vladimir dot kulyukin at gmail dot com

lst = [1, 2, 3, 4]

## use the fact that lists are iterables.
## the iterator variable x is iteratively bound to
## each element in lst.
 
for x in lst: print x
print 'x=', x, "\n" # x stays bound to its last value in for-loop

## the for-loop and print above produce the following output: 
## 1
## 2
## 3
## 4
## x= 4


## use lazy range from 0 upto the length of lst - 1.
## index into a specific spot in lst.
for i in xrange(0, len(lst)):
    print lst[i]
print 'i=', i, "\n"  # i is bound to its last value in for-loop

## the above for-loop and print produce the following output:
## 1
## 2
## 3
## 4
## i= 3

## non-lazy version of the index range. produces the same
## output ast the for loop with xrange above.
for i in range(0, len(lst)):
    print lst[i]
print 'i=', i, "\n"

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




