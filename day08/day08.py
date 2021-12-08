#!/usr/bin/pypy3

import os, sys
from itertools import permutations

stuff = open('input.txt', 'r').read().split('\n')
# print(stuff)

# def intl(ll):
#     return list(map(int, ll))

# stuff = intl(stuff)

iter = 0

for line in stuff:
    matters = line.split(' | ')[1].split(' ')

    for thing in matters:
        # print(thing, len(thing))
        if len(thing) in [2, 4, 3, 7]:
            iter += 1

print("part 1:", iter)

iter = 0

d = {
    '0': 'abcefg',
    '1': 'cf',
    '2': 'acdeg',
    '3': 'acdfg',
    '4': 'bcdf',
    '5': 'abdfg',
    '6': 'abdefg',
    '7': 'acf',
    '8': 'abcdefg',
    '9': 'abcdfg',
}
d = {k:''.join(sorted(v)) for k, v in d.items()}

b = {
    'abcefg'  : '0',
    'cf'      : '1',
    'acdeg'   : '2',
    'acdfg'   : '3',
    'bcdf'    : '4',
    'abdfg'   : '5',
    'abdefg'  : '6',
    'acf'     : '7',
    'abcdefg' : '8',
    'abcdfg'  : '9',
}

l = {
    'a': '',
    'b': '',
    'c': '',
    'd': '',
    'e': '',
    'f': '',
    'g': '',
}

for line in stuff:
    found = False
    matters = line.split(' | ')
    inmatters = matters[0].split(' ')
    otmatters = matters[1].split(' ')

    inmatters = [''.join(sorted(list(x))) for x in inmatters]
    otmatters = [''.join(sorted(list(x))) for x in otmatters]

    matters = inmatters + otmatters

    # print(matters)

    iter_n = 0
    iter_c = 0
    iter_l = 0
    iter_m = 0

    for p in permutations('abcdefg'):
        l = {chr(97+x):i for x, i in enumerate(''.join(p))}
        matters = [''.join(sorted([l[c] for c in thing]))
                   for thing in inmatters + otmatters]

        if all([a in d.values() for a in matters]):
            # print("found")
            otmatters = [''.join(sorted([l[c] for c in thing]))
                         for thing in otmatters]
            # print(otmatters)

            otnum = ''.join([b[i] for i in otmatters])
            iter += int(otnum)

            found = True
            break
    
    if not found:
        print('not found')

        print(line)

        print(iter_n)
        print(iter_c)
        print(iter_l)
        print(iter_m)
        print()


print("part 2:", iter)
