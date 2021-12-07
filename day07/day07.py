#!/usr/bin/pypy3

import os, sys

crabs = open('input.txt', 'r').read().split(",")

crabs = list(map(int, crabs))

print(crabs)

crabs_min = crabs
crabs_min_fuel = 10000000000
crab_max = max(crabs)

for i in range(crab_max):
    fuel = sum([abs(j - i) for j in crabs])
    if fuel < crabs_min_fuel:
        crabs_min_fuel = fuel
        crabs_min = [abs(j - i) for j in crabs]

print("part 1:", crabs_min_fuel)

crabs_min_fuel = 10000000000

for i in range(crab_max):
    fuel = sum([(abs(j - i)*(abs(j - i)+1)/2) for j in crabs])
    if fuel < crabs_min_fuel:
        crabs_min_fuel = fuel
        crabs_min = [abs(j - i) for j in crabs]

print("part 2:", crabs_min_fuel)
