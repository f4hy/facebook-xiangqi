#!/usr/bin/env python3.0
import json
import cgi
import pickle
import uuid
from board import *

import cgitb                    # for debuging
cgitb.enable()


def jsonprepmoves(board):
    """return a json string with all of the moves for the side whose turn it is"""
    return dict([("%d:%d" % k, v) for k, v in board.allturnlegalmoves().items()])

def jsonprepstate(board):
    """return a json string representing the current state of the board"""
    return dict([("%d:%d" % k, str(v)) for k, v in board.state().items()])

print("Content-Type: text/plain\n")
    
form = cgi.FieldStorage()       # get fields pased by url (get?)

gameid = form.getvalue("gameid",None)

filename = None

if not gameid:
    gameid = str(int(uuid.uuid4()))
    b = Board()
else:
    readfile = open("games/" + str(gameid),"rb")
    b =  pickle.load(readfile)
    readfile.close()
    #b = Board()


# turn = form.getvalue("turn","w")

# if (turn == "b"):               # WTF! why is this needed!
#     turn = "b"
# else:
#     turn = "w"

myjson = {}
myjson["positions"] = jsonprepstate(b)
myjson["moves"] = jsonprepmoves(b)
myjson["id"] = gameid
myjson["check"] = b.incheck()
myjson["checkmate"] = b.checkmate(b.turn)

print(json.dumps(myjson))
#print('{"positions":' + jsonstate(b) + ', "moves":'+ jsonmoves(b)+', "id":' + json.dumps(gameid) + "}")

writefile = open("games/" + gameid,"wb")
pickle.dump(b,writefile)
writefile.close()
