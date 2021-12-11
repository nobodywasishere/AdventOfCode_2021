#!/usr/bin/pypy3

import os, sys
from rich import print as pprint
import numpy as np

stuff = open('input.txt', 'r').read().split('\n')

stuff = [list(map(int,list(thing))) for thing in stuff]

cleanstuff = stuff[:]

def print_stuff(stuff):
    for i in stuff:
        print(''.join(map(str, i)))
    print()

flashes = 0
flashed = []

def flashSurr(y, x, first=False):
    global flashes, flashed
    global stuff
    global prev
    if not first:
        stuff[y][x] += 1
    if stuff[y][x] > 9 or first:
        flashed.append([y,x])
        stuff[y][x] = 0
        flashes += 1
        if x > 0 and [y,x-1] not in flashed:
            flashSurr(y, x-1)
        if x < len(stuff[0])-1 and [y,x+1] not in flashed:
            flashSurr(y, x+1)
        if y > 0 and [y-1,x] not in flashed:
            flashSurr(y-1, x)
        if y < len(stuff)-1 and [y+1,x] not in flashed:
            flashSurr(y+1, x)

        if x > 0 and y > 0 and [y-1,x-1] not in flashed:
            flashSurr(y-1, x-1)
        if x < len(stuff[0])-1 and y > 0 and [y-1, x+1] not in flashed:
            flashSurr(y-1, x+1)
        if x > 0 and y < len(stuff)-1 and [y+1, x-1] not in flashed:
            flashSurr(y+1, x-1)
        if x < len(stuff[0])-1 and y < len(stuff)-1 and [y+1, x+1] not in flashed:
            flashSurr(y+1, x+1)

for step in range(100):
    prev = []
    flashed = []
    for i in range(len(stuff)):
        stuff[i] = [j+1 for j in stuff[i]]

    for i in range(len(stuff)):
        for j in range(len(stuff[0])):
            if stuff[i][j] > 9:
                stuff[i][j] = 0
                prev.append([i,j])
                flashed.append([i,j])
                flashSurr(i, j, first=True)

    # print(prev)
    # print(flashed)
    # print_stuff(stuff)
    # input()

print("part 1:", flashes)

iter = 0

stuff = cleanstuff

while not all([all([j == 0 for j in i]) for i in stuff]):
    prev = []
    flashed = []
    for i in range(len(stuff)):
        stuff[i] = [j+1 for j in stuff[i]]

    for i in range(len(stuff)):
        for j in range(len(stuff[0])):
            if stuff[i][j] > 9:
                stuff[i][j] = 0
                prev.append([i,j])
                flashed.append([i,j])
                flashSurr(i, j, first=True)

    iter += 1

print("part 2:", iter)
