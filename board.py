#!/usr/bin/env python3.0
from piece import *
import copy

class InvalidMove(Exception): pass

class Board:
    """This is the board object that stores position of the board"""

    general = "帥"
    advisor = "士"
    elephant = "象"
    horse = "馬"
    chariot = "車"
    cannon = "砲"
    pawn = "卒"



    def __init__(self,coordinates=None):
        """set up the boards coordinates for pieces"""
        self.coordinates = [[None for i in range(9)] for j in range(10)]
#        self.turn = "w"
        self.newgameboard()

    def __repr__(self):
        """Print out the state of the board"""
        s = "\n"
        count = 0
        for row in self.coordinates:
            count +=1
            if count == 6:
                s+="==================\n"
            for piece in row:
                if piece:
                    s+=str(piece)
                else:
                    s+="  "
            s+="\n"
        return s

    def nextturn(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"
    
    def newgameboard(self):
        """Set the board to the start of a new game"""
        p = Piece
        #whites back row
        self.coordinates[0] = [Rook("w"),Horse("w"),Elephant("w"),
                               Advisor("w"),General("w"),Advisor("w"),
                               Elephant("w"),Horse("w"),Rook("w")]

        #black back row
        self.coordinates[9] = [Rook("b"),Horse("b"),Elephant("b"),
                               Advisor("b"),General("b"),Advisor("b"),
                               Elephant("b"),Horse("b"),Rook("b")]

        #white's pawns
        self.coordinates[3][0] = Pawn("w")
        self.coordinates[3][2] = Pawn("w")
        self.coordinates[3][4] = Pawn("w")
        self.coordinates[3][6] = Pawn("w")
        self.coordinates[3][8] = Pawn("w")

        #black's pawns
        self.coordinates[6][0] = Pawn("b")
        self.coordinates[6][2] = Pawn("b")
        self.coordinates[6][4] = Pawn("b")
        self.coordinates[6][6] = Pawn("b")
        self.coordinates[6][8] = Pawn("b")

        #white's cannons
        self.coordinates[2][1] = Cannon("w")
        self.coordinates[2][7] = Cannon("w")

        #black's cannons
        self.coordinates[7][1] = Cannon("b")
        self.coordinates[7][7] = Cannon("b")

        self.turn = "w"         # White starts

    def point(self,index):
        """Return the piece on a point, or return none"""
        if 0 <= index[0] <= 9 and 0 <= index[1] <= 8 :
            return self.coordinates[index[0]][index[1]]
        return None
    

    def move(self,current,new):
        """Move a piece from one spot to annother"""
        def validmove():
            if not self.point(current) : return False
            if new[0] > len(self.coordinates) : return False
            if new[1] > len(self.coordinates[0]) : return False
            return True
        if validmove():
            self.coordinates[new[0]][new[1]] = self.point(current)
            self.coordinates[current[0]][current[1]] = None
            self.nextturn()
        else:
            raise InvalidMove('Invalid move. No peice, or out of bounds')

    def occupied(self):
        """return a list of occupied spaces"""
        s = [(i,j) for i in range(10) for j in range(9)]
        return [p for p in s if self.point(p)]

    def side(self,color):
        """return all the spots occupied by a specific side"""
        s = [(i,j) for i in range(10) for j in range(9)]
        return [p for p in s if self.point(p) if self.point(p).color == color]


    def state(self):
        """Return the state of the board"""
        occ = self.occupied()
        s = {}
        for p in occ:
            s[p] = self.point(p)
        return s

    def findgeneral(self,color):
        """Returns the posistion of the general for a side"""
        def isgeneral(x):
            return isinstance(self.point(x),General)
        return next(filter(isgeneral,self.side(color)))

    def availiblemoves(self,location):
        """return the possible moves for a piece by location"""
        return self.point(location).possiblemoves(location,self)

    def allsidelegalmoves(self,color):
        """Returns a dictionary of all the legal moves for a side"""
        moves = {}

        # def legalmove(current,new):
        #     testboard = copy.deepcopy(self)
        #     testboard.move(current,new)
        #     if testboard.check(color):
        #         return False
        #     return True

        for piece in self.side(color):
            def legalmove(new):
                testboard = copy.deepcopy(self)
                testboard.move(piece,new)
                if testboard.check(color):
                    return False
                return True
            
            piecemoves = self.availiblemoves(piece)
            moves[piece] = list(filter(legalmove,piecemoves))
            # for candidatemove in piecemoves:
                
            #     if not legalmove(piece,candidatemove):
            #         piecemoves.remove(candidatemove)
            # moves[piece] = piecemoves
                
        return moves

    def allturnlegalmoves(self):
        return self.allsidelegalmoves(self.turn)

    def check(self,color):
        """Returns true if the given sides king is in check"""
        general = self.findgeneral(color)
        if color == "b": enemycolor = "w"
        if color == "w": enemycolor = "b"
        for opponent in self.side(enemycolor):
            if general in self.availiblemoves(opponent):
#                print("Check")
                return True
        return False
    
    def incheck(self):
        return self.check(self.turn)

    def checkmate(self,color):
        """If in check, make every possible move to see if we can get out of check"""
        if not self.check(color):
            return False
        moves = self.allsidelegalmoves(color)
        for piece in moves:
            for possiblemove in moves[piece]:
                testboard = copy.deepcopy(self)
                testboard.move(piece,possiblemove)
#                print(testboard) # for debugging
                if not testboard.check(color):
                    return False
        return True
    

if __name__ == "__main__" :
    """If running the board the directry run some tests"""
    b = Board()
    b.newgameboard()
    try: 
        b.move( (5,8),(5,8))
    except InvalidMove as e: 
        print(e)
    print(b)
    mypiece = b.point((6,8))
    
    for p in b.occupied():
        print(b.point(p),b.availiblemoves(p))
        
    print(b.check("b"))
    print(b.checkmate("w"))
    print(b.allsidelegalmoves("b"))

