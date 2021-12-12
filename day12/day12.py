#!/usr/bin/pypy3

import os, sys
from rich import print as pprint
import numpy as np

stuff = open('input.txt', 'r').read().split('\n')

nav = {}

count = 0

def subnav(past, loc):
    global count
    fwd = nav[loc]
    pre = '+'*(len(past)-1)
    # print('fwd:', fwd)
    # print('past:', past)
    for d in fwd:
        if d in past and d.islower():
            # print('cant revisit cave')
            continue
        elif d == 'end':
            # print('reached end')
            print('-'.join(past + ['end']))
            count += 1
            continue
        elif d == 'start':
            # print('cant go back to start')
            continue
        else:
            print(pre, 'visiting cave ' + str(d))
            # past = past[:]
            # past.append(d)
            subnav2(past[:] + [d], d)


def subnav2(past, loc):
    global count
    fwd = nav[loc]
    pre = '+'*(len(past)-1)
    # print('fwd:', fwd)
    # print('past:', past)
    for d in fwd:
        e = [i for i in past if i.islower() and i not in ['start', 'end']]
        dups = e != list(set(e))
        if past.count(d) > 0 and d.islower() and dups:
            # print('cant revisit cave')
            continue
        elif d == 'end':
            # print('reached end')
            print('-'.join(past + ['end']))
            count += 1
            continue
        elif d == 'start':
            # print('cant go back to start')
            continue
        else:
            # print(pre, 'visiting cave ' + str(d))
            # past = past[:]
            # past.append(d)
            subnav2(past[:] + [d], d)

for line in stuff:
    src, dest = line.split('-')

    if src in nav:
        nav[src].append(dest)
    else:
        nav[src] = [dest]
    
    if dest in nav:
        if src not in nav[dest]:
            nav[dest].append(src)
    else:
        nav[dest] = [src]



pprint(nav)
subnav(['start'], 'start')
print(count)

count = 0
small = False
subnav2(['start'], 'start')
print(count)
