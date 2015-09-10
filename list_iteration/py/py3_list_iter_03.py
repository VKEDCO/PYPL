## list iteration methods in Py
## author: Vladimir Kulyukin

lst = [1, 2, 3, 4]

## non-lazy version of the index range. produces the same
## output as the for loop with xrange above.
for i in range(0, len(lst)):
    print(lst[i])
print('i=', i)
