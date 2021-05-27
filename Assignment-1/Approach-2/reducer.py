#!/usr/bin/python

from __future__ import print_function, division
import sys

numerator = 2
denominator = float(1)
instances = 0
pi = 0

for line in sys.stdin:
  denominator = float(line)
  pi += (numerator/denominator)
  instances += 1

print(pi/instances)
