#!/usr/bin/env python
import sys

def collatz(x):
    i = 0
    while x != 1:
        if not x % 2:
            x = x/2
        else:
            x = (3 * x) + 1
        i += 1
    return i

if __name__ == '__main__':
    i = int(sys.argv[1])
    high = 0
    highesti = 0
    try:
        while True:
            n = collatz(i)
            if n > high:
                high = n
                highesti = i
                print high, highesti
            i += 1
    except:
        print '\nyou got to i =', i
