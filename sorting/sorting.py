#!/usr/bin/env python

def bubble(l):
    swapped = False:
    for i in range(n):
        if l[i] > l[i+1]:
            l[i] ^= [l+1]
            l[i+1] ^= l[i]
            l[i] ^= l[i+1]
            swapped = True

