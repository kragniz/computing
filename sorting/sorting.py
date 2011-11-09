#!/usr/bin/env python
import random

def bubble(l):
    swapped = True 
    swaps = 0 #the number of swaps taken
    while swapped:
        swapped = False
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                swapped = True
                swaps += 1

                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l, swaps


def insertion(l):
    swaps = 0

    for j in [i+1 for i in range(len(l)-1)]:
        key = l[j]
        i = j-1
        while i >= 0 and l[i] > key:
            swaps += 1
            l[i+1] = l[i]
            i = i-1
        l[i+1] = key
    return l, swaps


def test(n):
    for i in range(n):
        l = [random.randint(1, 1000) for j in range(i)]
        l2 = list(l)

        sortedList, swaps = bubble(l)
        print sortedList
        print 'took', swaps, 'swaps for bubble with', i, 'length'
        sortedList, swaps = insertion(l2)
        print sortedList
        print 'took', swaps, 'swaps for insertion with', i, 'length'

if __name__ == '__main__':
    test(200)
