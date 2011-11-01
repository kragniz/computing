!/usr/bin/env python
import sys

def power(x, y):
    if y == 0:
        return 1
    else:
        return power(x, y - 1) * x

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print power(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print power(2, 8)
