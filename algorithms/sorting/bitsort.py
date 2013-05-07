#!/usr/bin/env python
# encoding: utf-8
"""
Bit Sort(from the book <<Programming Pearls>>)
Author: 
    ?
"""

from bitarray import bitarray
from random import randint

def bit_sort(L, n):
    assert(len(L) < n)
    bitarr = bitarray(n)
    bitarr.setall(False)
    for i in L:
        bitarr[i] = True
    ms = [i for i in range(n) if bitarr[i]]
    return ms

def genshuf(m, n):
    x = [i for i in range(n)]
    y = []
    for i in range(m):
        j = randint(i+1, n-1)
        x[i],x[j] = x[j],x[i]
        y.append(x[i])
    return y

if __name__ == '__main__':
    L = genshuf(100000, 10000000)
    bs = bit_sort(L, 10000000)
    ps = sorted(L)
    for i in range(100000):
        if bs[i] != ps[i]:
            print "Sorry"
    print "End"

