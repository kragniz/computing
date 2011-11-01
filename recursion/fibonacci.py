#!/usr/bin/env python
import sys

class cache(object):
    def __main__(self):


def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 10

    for i in range(n):
        print f(i),
