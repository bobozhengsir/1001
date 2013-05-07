#!/usr/bin/env python
# encoding: utf-8
"""
Programming Pearls
"""

from random import randint

def genshuf(m, n):
    """
    Author:
        Ashley Shepherd and Alex Woronow
    the result is idle
    """
    x = [i for i in range(n)]
    y = []
    for i in range(m):
        j = randint(i+1, n-1)
        x[i],x[j] = x[j],x[i]
        y.append(x[i])
    return y

def genknuth(m, n):
    """
    Author:
        Knuth
    the result is sorted
    """
    big_int = 2**64
    y = []
    for i in range(n):
        if randint(0, big_int) % (n-i) < m:
            y.append(i)
            m -= 1
    return y

if __name__ == '__main__':
    y1 = genshuf(10, 100)
    y2 = genknuth(10, 100)
    print y1
    print y2
