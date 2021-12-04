#!/usr/bin/pypy3

import os, sys

def check_board(board):
    for i in range(5):
        if sum(board[5*i:5*i+5]) == -5:
            return True
        if sum([board[i], board[i+5], board[i+10], board[i+15], board[i+20]]) == -5:
            return True
        
    return False

stuff = open('input.txt', 'r').read()[:-1]

stuff = stuff.split('\n\n')

nums = stuff[0]

del stuff[0]

for i in range(len(stuff)):
    temp = [j.split(' ') for j in stuff[i].split('\n')]
    stuff[i] = list(map(int, [k for l in temp for k in l]))

stuff2 = stuff[:]

nums = list(map(int, nums.split(',')))

winner = None

for curr in nums:
    if winner is not None:
        break
    for board_i in range(len(stuff)):
        board = stuff[board_i]
        if curr in board:
            stuff[board_i] = [-1 if t == curr else t for t in board]
        if check_board(stuff[board_i]):
            winner = stuff[board_i]
            winner_curr = curr
            
winner = [0 if t == -1 else t for t in winner]
print("part 1:", sum(winner)*winner_curr)

winner = None

for curr in nums:
    for board in stuff2:
        newboard = [-1 if t == curr else t for t in board]
        if check_board(newboard):
            stuff2 = [q for q in stuff2 if q != board]
            winner = newboard
            winner_curr = curr
        else:
            stuff2 = [newboard if q == board else q for q in stuff2]

winner = [0 if t == -1 else t for t in winner]
print("part 2:", sum(winner)*winner_curr)