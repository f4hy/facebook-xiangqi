class Piece:
    """represents a playable chess peice, with shared properties of all pieces"""
    def __init__(self,color="w"):
        self.color = color

    def possiblemoves(self,location,board):
        """Return the places a piece can move"""
        return []
#        return [(i,j) for i in range(10) for j in range(9)]

    def onboard(self,move):
        """Retrun the moves that are on the board"""
        if 0 <= move[0] <= 9 and 0 <= move[1] <= 8 : return True
        return False

    def inpalace(self,move):
        """Return the points that are in the palace"""
        black = [(i,j) for j in range(3,6) for i in range(0,3)]
        white = [(i,j) for j in range(3,6) for i in range(7,10)]
        if move in black or move in white: return True
        return False

    def south(self, location):
        """A generator of moves in the southern direction"""
        i,j = location
        while i < 9:
            i +=1
            yield (i,j)

    def north(self, location):
        """A generator of moves in the northern direction"""
        i,j = location
        while i >= 0:
            i -=1
            yield (i,j)

    def east(self, location):
        """A generator of moves in the eastern direction"""
        i,j = location
        while j >= 0:
            j -=1
            yield (i,j)

    def west(self, location):
        """A generator of moves in the western direction"""
        i,j = location
        while j < 8:
            j +=1
            yield (i,j)

    def enemey(self, otherpiece):
        """Retrun true if the peice is an enemy"""
        if otherpiece:
            if self.color != otherpiece.color:
                return True
        return False

    def friendly(self, otherpiece):
        """Return true if a peice is friendly"""
        if otherpiece:
            if self.color == otherpiece.color:
                return True
        return False




class Pawn(Piece):
    """Pawn piece"""
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        """Print a pawn"""
        if self.color == "b":
            return "卒"
        else:
            return "兵"
        
    def possiblemoves(self,location,board):
        """return the moves for a pawn, forward for either black or white
        sideways after crossing the river"""
        if self.color == "b":
            moves = [(location[0]-1,location[1])]
            if location[0] < 5:
                moves.append( (location[0],location[1]+1) )
                moves.append( (location[0],location[1]-1) )
        else:
            moves = [(location[0]+1,location[1])]
            if location[0] > 4:
                moves.append( (location[0],location[1]+1) )
                moves.append( (location[0],location[1]-1) )

        def friendlypiece(candidatemove):
            return not self.friendly(board.point(candidatemove))

        moves = list(filter(friendlypiece,moves))
        return list(filter(self.onboard,moves))

class Cannon(Piece):
    """Cannon piece"""
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        """Print the cannon"""
        if self.color == "b":
            return "砲"
        else:
            return "炮"
    def possiblemoves(self,location,board):
        """The squares the cannon can move to"""
        def cannonmoves(board,directiongenerator):
            """The odd jumping capture of a cannon"""
            jumping = False
            moves = []
            row,column = location
            for spot in directiongenerator:
                point = board.point(spot)
                if jumping:
                    if point:
                        if point.color is not self.color:
                            moves.append(spot)
                        break
                else:
                    if point:
                        jumping = True
                    else:
                        moves.append( spot )
            return moves

        moves = []
        moves.extend(cannonmoves(board,self.north(location)))
        moves.extend(cannonmoves(board,self.south(location)))
        moves.extend(cannonmoves(board,self.east(location)))
        moves.extend(cannonmoves(board,self.west(location)))
        return list(filter(self.onboard,moves))

class Rook(Piece):
    """rook piece"""
    def __init__(self,color="w"):
        self.color = color
        
    def __repr__(self):
        if self.color == "b":
            return "車"
        else:
            return "俥"

    def possiblemoves(self,location,board):
        """The squares rook can move to"""
        def rookmoves(board,directiongenerator):
            """Line of moves till hitting a peice"""
            moves = []
            row,column = location
            for spot in directiongenerator:
                point = board.point(spot)
                if point:
                    if point.color is self.color:
                        break
                    else:
                        moves.append( spot )
                        break
                else:
                    moves.append( spot )
            return moves

        moves = []
        moves.extend(rookmoves(board,self.north(location)))
        moves.extend(rookmoves(board,self.south(location)))
        moves.extend(rookmoves(board,self.east(location)))
        moves.extend(rookmoves(board,self.west(location)))
        return list(filter(self.onboard,moves))

class Horse(Piece):
    """The horse piece, like a knight"""
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "馬"
        else:
            return "馬"

    def possiblemoves(self,location,board):
        """Return the points a horse can move to"""
        moves =[]
        i,j = location
            #north
        if not board.point((i-1,j)):
            moves.extend( [(i-2,j-1),(i-2,j+1)] )
        if not board.point((i+1,j)):
            moves.extend( [(i+2,j-1),(i+2,j+1)] )
        if not board.point((i,j-1)):
            moves.extend( [(i-1,j-2),(i+1,j-2)] )
        if not board.point((i,j+1)):
            moves.extend( [(i-1,j+2),(i+1,j+2)] )

        def friendlypiece(candidatemove):
            return not self.friendly(board.point(candidatemove))
        moves = list(filter(self.onboard,moves))
        moves = list(filter(friendlypiece,moves))
        
        return moves

class Elephant(Piece):
    """Elephant piece"""
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "象"
        else:
            return "相"
    def possiblemoves(self,location,board):
        """Return the points an elephant can move to"""
        def thissideoftheriver(location):
            """Return if a spot is on our side of the river"""
            if self.color == "w" and location[0] < 5:
                return True
            if self.color == "b" and location[0] > 4:
                return True
            return False
        i,j = location
        moves = [(i+2,j+2),(i+2,j-2),(i-2,j-2),(i-2,j+2)]

        def friendlypiece(candidatemove):
            return not self.friendly(board.point(candidatemove))
        moves = list(filter(friendlypiece,moves))

        moves = filter(thissideoftheriver,moves)



        return list(filter(self.onboard,moves))


class Advisor(Piece):
    """The palace advisor peice"""
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "士"
        else:
            return "仕"

    def possiblemoves(self,location,board):
        """Can move diagonaly within the palace"""
        i,j = location
        moves = []
        for x in [(i+1,j+1),(i+1,j-1),(i-1,j-1),(i-1,j+1)]:
            if not self.friendly(board.point(x)):
                moves.append(x)
        return list(filter(self.inpalace,moves))


class General(Piece):
    """General Piece, like the king"""
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "將"
        else:
            return "帥"
        
    def possiblemoves(self,location,board):
        """Can move n/s/e/w within the palace"""
        def kingmoves(directiongenerator):
            try:
                candidatemove = next(directiongenerator)
            except:
                return []
            if self.inpalace(candidatemove):
                if not self.friendly(board.point(candidatemove)):
                    return [candidatemove]
            return []
        moves = []
        moves.extend(kingmoves(self.north(location)))
        moves.extend(kingmoves(self.south(location)))
        moves.extend(kingmoves(self.east(location)))
        moves.extend(kingmoves(self.west(location)))
#        return list(moves)
        return list(filter(self.inpalace,moves))

