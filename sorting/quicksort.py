#!/usr/bin/env python
import random

def quicksort(l):
    if len(l) <= 1:
        return l
    less = []
    greater = []
    pivot = l.pop(random.randint(1, len(l)-1))
    for x in l:
        if x <= pivot:
            less += [x]
        else:
            greater += [x]
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == '__main__':
    l = [random.randint(0, 1000) for i in range(100)]
    print quicksort(l)
