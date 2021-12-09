#!/usr/bin/pypy3

import os, sys
from itertools import permutations
from rich import print as pprint
import numpy as np

stuff = open('input.txt', 'r').read().split('\n')

# print(stuff)

# print(len(stuff), len(stuff[0]))

mins = []

for i in range(len(stuff)):
    for j in range(len(stuff[i])):
        if j > 0:
            l = int(stuff[i][j-1]) 
        else:
            l = 9
        if j < len(stuff[i]) - 1:
            r = int(stuff[i][j+1])
        else:
            r = 9
        if i > 0:
            u = int(stuff[i-1][j])
        else:
            u = 9
        if i < len(stuff) - 1:
            d = int(stuff[i+1][j])
        else:
            d = 9

        c = int(stuff[i][j])

        # print(u, d, l, r, stuff[i][j], '\n')

        if min([u, d, l, r]) > c:
            # print(f"min found at {i},{j}")
            mins.append([c, i, j])

# print(mins)

risk = 0

for m in mins:
    risk += m[0] + 1

print('part 1:', risk)


def print_basin(basin, x, y):
    # os.system('clear')
    arr = [[' ' for a in range(x)] for b in range(y)]
    for ch in range(len(basin)):
        for cc in basin[ch]:
            if arr[cc[0]][cc[1]] != ' ':
                # raise ValueError(f'Duplicate coords: {cc[0]},{cc[1]}')
                arr[cc[0]][cc[1]] = 'X'
            else:
                arr[cc[0]][cc[1]] = str(hex(ch % 16)[2:])

    for b in range(y):
        print(''.join(arr[b]))
    print()

basinc = []

maxi = len(stuff)
maxj = len(stuff[0])

for i in range(len(stuff)):
    for j in range(len(stuff[i])):
        if [i, j] in basinc:
            continue

        if stuff[i][j] == '9':
            continue

        cc = [ i,  j]
        # print(cc)
        pc = []
        if j > 0 and stuff[i][j-1] != '9':
            pc.append([i, j-1])
        if i > 0 and stuff[i-1][j] != '9':
            pc.append([i-1, j])
        if j < maxj - 1 and stuff[i][j+1] != '9':
            pc.append([i, j+1])
        if i < maxi - 1 and stuff[i+1][j] != '9':
            pc.append([i+1, j])

        found = False
        for b in range(len(basinc)):
            if any([c in basinc[b] for c in pc]):
                found = True
                if cc not in basinc[b]:
                    basinc[b].append(cc)
                for c in pc:
                    if c not in basinc[b]:
                        basinc[b].append(c)
                break
        if not found:
            # print(f'basin for coord {cc} not found')
            basinc.append([cc])
        # print(basinc)
        # print_basin(basinc, maxj, maxi)
        # input()

# print(basinc)
# print_basin(basinc, maxj, maxi)

basinm = [basinc[0][:]]

for q in range(len(basinc)):
    # print('basinm:',basinm)
    # # print('basinc[q]:',basinc[q])
    found = False
    for r in range(len(basinm)):
        # print('search:',[g == h for g in basinc[q] for h in basinm[r]])
        if any([g == h for g in basinc[q] for h in basinm[r]]):
            # print('appending to basin ' + str(r))
            found = True
            for t in basinc[q]:
                if t not in basinm[r]:
                    basinm[r].append(t)
    if not found:
        # print('adding basin')
        basinm.append(basinc[q])
    # print_basin(basinm, maxj, maxi)
    # input()
    # print()

# print(basinm)
# print_basin(basinm, maxj, maxi)

# print(sorted([len(b) for b in basinm]))
print('part 2:', np.product(sorted([len(b) for b in basinm])[-3:]))

