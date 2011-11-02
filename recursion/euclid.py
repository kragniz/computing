#!/usr/bin/env python

import sys

def e(x, y):
    if y == 0:
        return x
    else:
        return e(y, x % y)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print e(10, 6)
    else:
        print e(int(sys.argv[1]), int(sys.argv[2]))
