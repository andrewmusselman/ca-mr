#!/usr/bin/env python
import sys
o = '@'
z = '.'
rules_arr = [(o,o,o),(z,z,o),(z,o,z),(z,o,o),(o,z,z),(o,z,o),(o,o,z),(o,o,o)]
rules = {}
import math
rule = int(sys.argv[1])
rules = {}
for i in range(7,-1,-1):
  rem = rule % math.pow(2,i)
  if rem != rule:
    rules[rules_arr[i]] = True
    rule = rem

for line in sys.stdin:
  line = line.strip()
  out = ''
  l = len(line)
  for i in range(0,l):
    if (line[(i-1)%l],line[i],line[(i+1)%l]) in rules:
      out += o
    else:
      out += z
print out
