#!/usr/bin/pypy3

import os, sys

stuff = open('input.txt', 'r').read()

fish = list(map(int, stuff.split(',')))

for day in range(80):

    for i, f in enumerate(fish):
        fish[i] -= 1

        if f == 0:
            fish[i] = 6
            fish.append(9)

print("part 1:", len(fish))

fish = list(map(int, stuff.split(',')))

fish = [
    fish.count(0),
    fish.count(1),
    fish.count(2),
    fish.count(3),
    fish.count(4),
    fish.count(5),
    fish.count(6),
    fish.count(7),
    fish.count(8),
    fish.count(9),
]

for day in range(256):
    temp = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish[6]
    fish[6] = fish[7] + temp
    fish[7] = fish[8]
    fish[8] = temp

print("part 2:", sum(fish))