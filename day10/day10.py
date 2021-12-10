#!/usr/bin/pypy3

import os, sys
from rich import print as pprint
import numpy as np

stuff = open('input.txt', 'r').read().split('\n')

corr = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

corrv = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

pts = 0
incomplete = []

for line in stuff:
    stack = []
    out = []
    err = False
    for b in line:
        # print(b, ''.join(stack))
        if b in corr.keys():
            stack.append(b)
            out.append(b)
        elif b in corrv.keys():
            if corr[stack[-1]] == b:
                stack.pop()
                out.append(b)
            else:
                # print(f'Expected {corr[stack[-1]]} but got {b} instead')
                if b == ')':
                    pts += 3
                elif b == ']':
                    pts += 57
                elif b == '}':
                    pts += 1197
                elif b == '>':
                    pts += 25137
                err = True
                break
    if not err:
        incomplete.append(line)

print("part 1:", pts)

pts = 0

out = []

for line in incomplete:
    stack = []
    expect = []
    for b in line:
        if b in corr.keys():
            stack.append(b)
            expect.append(corr[b])
        elif b in corrv.keys():
            if corr[stack[-1]] == b:
                stack.pop()
                expect.pop()

    out.append(reversed(expect))

scores = []

for thing in out:
    pts = 0
    for char in thing:
        pts *= 5
        if char == ')':
            pts += 1
        elif char == ']':
            pts += 2
        elif char == '}':
            pts += 3
        elif char == '>':
            pts += 4

    scores.append(pts)

print("part 2:", sorted(scores)[int(len(scores)/2)])