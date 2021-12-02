#!/usr/bin/pypy3

import os, sys

stuff = open('input.txt', 'r').read().splitlines()

h = 0
d = 0

for i in stuff:
    act, val = i.split(' ')
    if act == "forward":
        h += int(val)
    elif act == "down":
        d += int(val)
    elif act == "up":
        d -= int(val)

print("part 1:", h*d)

a = 0
h = 0
d = 0

for i in stuff:
    act, val = i.split(' ')
    if act == "forward":
        h += int(val)
        d += a*int(val)
    elif act == "down":
        a += int(val)
    elif act == "up":
        a -= int(val)

print("part 2:", h*d)