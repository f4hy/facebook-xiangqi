#!/usr/bin/env python3.0
import json
from board import *

def jsonmoves(board,side):
    return json.dumps(dict([("%d:%d" % k, v) for k, v in board.allsidelegalmoves(side).items()]))

def jsonstate(board):
    return json.dumps(dict([("%d:%d" % k, str(v)) for k, v in board.state().items()]))
    


b = Board()
b.newgameboard()

#print("Content-Type: text/html")
# print("<TITLE>CGI script output</TITLE>")
# print("<H1>This is my first CGI script</H1>")
# print("Hello, world!")
print("'" + jsonstate(b) + "'")
