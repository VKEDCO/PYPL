#!/usr/bin/python
## print integers from STDIN that are >= sys.argv[1]
import sys
thresh = int(sys.argv[1])
for n in [int(x) for x in sys.stdin.readlines() if int(x) >= thresh]:
    print n
