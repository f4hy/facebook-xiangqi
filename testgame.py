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

def makerandommove():
    
    mymoves = b.allsidelegalmoves(next(turn))
    mypiece = random.choice(list(mymoves))
    mymove = random.choice(mymoves[mypiece])
    print(b.point(mypiece),mymove)
    b.move(mypiece,mymove)
    print(b)

for x in range(30):
    makerandommove()