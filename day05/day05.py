#!/usr/bin/pypy3

import os, sys

stuff = open('input.txt', 'r').read().splitlines()

size = 1000
coords = [ [0 for i in range(size)] for i in range(size) ]

for line in stuff:
    x, y = line.split(' -> ')
    x1, y1 = list(map(int,x.split(',')))
    x2, y2 = list(map(int,y.split(',')))

    if x1 == x2:
        for i in range(min([y1, y2]), max([y1, y2])+1):
            coords[x1][i] += 1
        
    elif y1 == y2:
        for i in range(min([x1, x2]), max([x1, x2])+1):
            coords[i][y1] += 1

iterator = 0

for row in coords:
    for col in row:
        if col > 1:
            iterator += 1

print("part 1:", iterator)

for line in stuff:
    x, y = line.split(' -> ')
    x1, y1 = list(map(int,x.split(',')))
    x2, y2 = list(map(int,y.split(',')))

    if (x1 - x2) == (y1 - y2):
        for i in range(min([x1,x2]), max([x1,x2])+1):
            coords[i][min([y1,y2])+i-min([x1,x2])] += 1

    elif (x1 - x2) == (y1 - y2) * -1:
        for i in range(min([x1,x2]), max([x1,x2])+1):
            coords[i][min([y1,y2])-i+max([x1,x2])] += 1

iterator = 0

for row in coords:
    for col in row:
        if col > 1:
            iterator += 1

print("part 2:", iterator)