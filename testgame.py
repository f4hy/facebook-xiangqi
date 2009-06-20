#!/usr/bin/env python3.0
from board import *
import random 

b = Board()
b.newgameboard()
print(b)

def genturn():
    t = "w"
    while True:
        if t is "w":
            t ="b"
        else:
            t = "w"
        yield t

turn = genturn()

print(next(turn))
print(next(turn))
print(next(turn))

if []:
    print()

def makerandommove():

    t = next(turn)
    mymoves = b.allsidelegalmoves(t)
    if not mymoves:
        print(mymoves)
    mypiece = None
    while not mypiece:
        mypiece = random.choice(list(mymoves))
    if mymoves[mypiece]:
        mymove = random.choice(mymoves[mypiece])
        print(b.point(mypiece),mymove)
        b.move(mypiece,mymove)
    else: print("pass")
    if b.checkmate(t):
        print("checkmate!")
        quit()
    print(b)

for x in range(300):
    makerandommove()

print(b)
