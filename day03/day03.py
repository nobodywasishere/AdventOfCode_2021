#!/usr/bin/pypy3

import os, sys
from statistics import mode

stuff = open('input.txt', 'r').read().splitlines()

for i in range(len(stuff)):
    stuff[i] = int(stuff[i],2)

gamma = 0
epsil = 0
s = 12

bits = [0 for i in range(s)]

for i in range(s):
    bits[i] = [(stuff[j] & 2**i) for j in range(len(stuff))]
    gamma += mode(bits[i])

print("part 1:", gamma*(2**s - 1 - gamma))


temp = stuff[:]

ox = 0
o2 = 0

for i in reversed(range(s)):
    count = [(temp[j] & 2**i) >> i for j in range(len(temp))]

    try:
        m = mode(count)
    except:
        m = 1

    temp = [j for j in temp if (j & 2**i) >> i == m]
    if len(temp) == 1:
        ox = temp[0]
        break

temp = stuff[:]

for i in reversed(range(s)):
    count = [(temp[j] & 2**i) >> i for j in range(len(temp))]

    try:
        m = int(not mode(count))
    except:
        m = 0

    temp = [j for j in temp if (j & 2**i) >> i == m]
    if len(temp) == 1:
        o2 = temp[0]

print("part 2:", ox*o2)
