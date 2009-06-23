#!/usr/bin/env python3.0
import json
import cgi
import pickle
from board import *

import cgitb                    # for debuging
cgitb.enable()


def jsonmoves(board,side):
    """return a json string with all of the moves for the given side"""
    return json.dumps(dict([("%d:%d" % k, v) for k, v in board.allsidelegalmoves(side).items()]))

def jsonstate(board):
    """return a json string representing the current state of the board"""
    return json.dumps(dict([("%d:%d" % k, str(v)) for k, v in board.state().items()]))

print("Content-Type: text/plain\n")
    
form = cgi.FieldStorage()       # get fields pased by url (get?)

id = form.getvalue("id",None)



if not id:
    b = Board()
    b.newgameboard()



turn = form.getvalue("turn","w")

if (turn == "b"):               # WTF! why is this needed!
    turn = "b"
else:
    turn = "w"

print("'{positions:" + jsonstate(b) + ", moves:"+ jsonmoves(b,turn)+"}'")

myfile = open("testfile","wb")
pickle.dump(b,myfile)
myfile.close()
