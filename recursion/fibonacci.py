#!/usr/bin/env python
import sys

class fibonacci(object):
    def __init__(self):
        self.numbers = {}

    def getNth(self, n):
        if self.numbers.has_key(n):
            return self.numbers[n]
        else:
            return False

    def setNth(self, n, v):
        self.numbers[n] = v

    def fib(self, n):
        v = self.getNth(n)
        if v:
            return v
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            nthFib = self.fib(n - 1) + self.fib(n - 2)
            self.setNth(n, nthFib)
            return nthFib


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 10

    f = fibonacci()
    for i in range(n):
        print f.fib(i),
