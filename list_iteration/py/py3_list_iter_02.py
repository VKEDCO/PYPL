## list iteration methods in Py
## author: Vladimir Kulyukin

lst = [1, 2, 3, 4]

## use lazy range from 0 upto the length of lst - 1.
## index into a specific spot in lst.
for i in range(0, len(lst)):
    print(lst[i])
print('i=', i)  # i is bound to its last value in for-loop

## the above for-loop and print produce the following output:
## 1
## 2
## 3
## 4
## i= 3
