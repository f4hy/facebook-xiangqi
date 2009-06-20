#!/usr/bin/env python3.0
import json
import cgi
import pickle
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


form = cgi.FieldStorage()
turn = form.getvalue("turn","w")

if (turn == "b"):               # WTF! why is this needed!
    turn = "b"
else:
    turn = "w"

print("'{positions:" + jsonstate(b) + ", moves:"+ jsonmoves(b,turn)+"}'")

myfile = open("testfile","wb")
pickle.dump(b,myfile)
myfile.close()
