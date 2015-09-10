## list iteration methods in Py
## author: Vladimir Kulyukin

lst = [1, 2, 3, 4]

## use the fact that lists are iterables.
## the iterator variable x is iteratively bound to
## each element in lst.
 
for x in lst: print(x)
print('x=', x) # x stays bound to its last value in for-loop

## the for-loop and print above produce the following output: 
## 1
## 2
## 3
## 4
## x= 4
