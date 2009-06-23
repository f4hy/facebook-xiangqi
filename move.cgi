#!/usr/bin/env python3.0
import json
import cgi
import pickle
from board import *

import cgitb                    # for debuging
cgitb.enable()


    
form = cgi.FieldStorage()       # get fields pased by url (get?)

gameid = form.getvalue("gameid",None)

new = form.getvalue("to", "")
old = form.getvalue("from", "")

myold = (int(old[0]),int(old[1]))
mynew = (int(new[0]),int(new[1]))

# testfile = open("mytestfile","w")
# # testfile.write(type(old))
# testfile.write("\n"
# )
# testfile.write("\n")
# testfile.write(str(type(old[0])))
# testfile.write("\n")
# testfile.write(str(myold))
# testfile.write("\n")
# testfile.write("testing")
# testfile.write("\n")
# testfile.write("old " + str(old[0]) + " " + str(old[1])  + " new" + str(new[0]) + " game id?" + str(gameid) +  "\n") 
# testfile.write("\n")
# testfile.close()


readfile = open("games/" + str(gameid),"rb")
b = pickle.load(readfile)
readfile.close()



b.move( myold,mynew)

writefile = open("games/" + gameid,"wb")
pickle.dump(b,writefile)
writefile.close()
