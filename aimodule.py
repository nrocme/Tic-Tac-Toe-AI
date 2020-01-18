#!/usr/bin/env python3

import sys
from random import choice

winners = ( (0,1,2), (3,4,5), (6,7,8), (0,3,6),
            (1,4,7), (2,5,8), (0,4,8), (2,4,6))

squareorder = [4, 0, 2, 6, 8, 1, 3, 5, 7]

# pattern means row, column, diagonal

def phase1(board, who):
    moves = [x for x in range(9) if board[x] == 0]
    return choice(moves)

def phase2(board, who):
    opp = 3 - who          # opp is the other player
#
# first check is we can win
#
    for pat in winners:
        s = [board[x] for x in pat]    # values in the square for this pattern
        if opp in s:                   # is the other play in this pattern
            continue
        if len([x for x in pat if board[x] == who]) == 2:
            return pat[s.index(0)]
#
# next check is we can prevent the other player from winning
#
    for pat in winners:
        s = [board[x] for x in pat]    # values in the square for this pattern
        if who in s:                   # is the other play in this pattern
            continue
        if len([x for x in pat if board[x] == opp]) == 2:
            return pat[s.index(0)]
    for x in squareorder:
        if board[x] == 0:
            return x
    print("Error in phase2: no available moves?", file=sys.stderr)
    return -1


if __name__ == "__main__":

    pass
