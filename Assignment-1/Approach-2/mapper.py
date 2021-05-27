#!/usr/bin/python

from __future__ import print_function, division
import sys
import math

def calculate_term(n):
    pi = 1
    for i in range(n , 0, -1):
        if i > 1:
            f = 2
            for j in range(1,i):
                if j < i:
                    f = 2 + math.sqrt(f)
            pi *= f/2
    return pi

n = int(sys.argv[1])
recursion_limit = sys.getrecursionlimit()
denominator = 1

for i in range(1, n):
  if i >= recursion_limit:
    sys.setrecursionlimit(2 * i)
  denominator = (calculate_term(i) * math.sqrt(2)) / 2

print(denominator)
