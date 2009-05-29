#!/usr/bin/env python3.0
import json
from board import *

b = Board()
b.newgameboard()
#print(b)
print(b.allsidelegalmoves("w"))
print(b.allsidelegalmoves("w").items())

print("json")
print(json.dumps(dict([("%d,%d" % k, v) for k, v in b.allsidelegalmoves("w").items()])))


#print(json.JSONEncoder().encode(b.allsidelegalmoves("w")))

