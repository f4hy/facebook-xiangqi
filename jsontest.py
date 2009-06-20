#!/usr/bin/env python3.0
import json
from board import *

def jsonmoves(board,side):
    return json.dumps(dict([("%d:%d" % k, v) for k, v in board.allsidelegalmoves(side).items()]))

def jsonstate(board):
    return json.dumps(dict([("%d:%d" % k, str(v)) for k, v in board.state().items()]))
    


b = Board()
b.newgameboard()

# print(b.side("w"))
# print(b.state())

print("帥")

print(jsonmoves(b,"w"))
print("-----")
print(b.state())
print(jsonstate(b))
