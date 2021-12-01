#!/usr/bin/pypy3

import os, sys

stuff = open('input.txt', 'r').read().splitlines()

stuff = list(map(int, stuff))

inc = 0

for i in range(1, len(stuff)):
    if stuff[i-1] < stuff[i]:
        inc += 1

print(f"part 1: {inc}")

inc = 0

for i in range(1, len(stuff) - 2):
    if sum(stuff[i-1:i+2]) < sum(stuff[i:i+3]):
        inc += 1

print(f"part 2: {inc}")