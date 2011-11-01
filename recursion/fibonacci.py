#!/usr/bin/env python
import sys, time

class fibonacci(object):
    def __init__(self):
        self.numbers = {}

    def getNth(self, n):
        if n in self.numbers:
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
            if n - 2 > 1:
                del self.numbers[n - 2]
            self.setNth(n, nthFib)
            return nthFib


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 10

    f = fibonacci()
    startT = time.time()
    for i in range(n):
        print f.fib(i)
        if i == n-1:
            print f.fib(i)
    endT = time.time()
    t = endT - startT
    print 'generated all the fibonacci numbers up to', n, '- this took', t, 'seconds'
