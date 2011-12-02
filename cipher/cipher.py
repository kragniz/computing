#!/usr/bin/env python

def vigenere(s, key):
    s = [ord(c) for c in s]
    key = [ord(c)-97 for c in s.lower()]

    for i, c in enumerate(s):
        #print i, c
        print chr((key[i % len(key)] + c))


if __name__ == '__main__':
    vigenere('hello my fine friend', 'thekey')
