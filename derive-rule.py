#!/usr/bin/env python
import sys
import math
rule = int(sys.argv[1])

for i in range(7,-1,-1):
  print i
  rem = rule % math.pow(2,i)
  if rem == rule:
    print "no"
  else:
    print "yes"
    rule = rem
  print
