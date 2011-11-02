#!/usr/bin/env python
import sys

class hanoi(object):
    def __init__(self, n):
        self.A = [i + 1 for i in range(n)]
        self.B = []
        self.C = []

    def __str__(self):
        return 'A:' + str(self.A) + ' B:' + \
                str(self.B) + ' C:' + \
                str(self.C)

    def move(self, n):


if __name__ == '__main__':
    h = hanoi(10)
    print h
