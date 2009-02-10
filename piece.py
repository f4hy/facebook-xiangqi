class Piece:

    character = {("g","w"): "將"}
    character[("a","w")] = "仕"
    character[("e","w")] = "相"
    character[("h","w")] = "馬"
    character[("r","w")] = "俥"
    character[("c","w")] = "炮"
    character[("p","w")] = "兵"

    character[("g","b")] = "帥"
    character[("a","b")] = "士"
    character[("e","b")] = "象"
    character[("h","b")] = "馬"
    character[("r","b")] = "車"
    character[("c","b")] = "砲"
    character[("p","b")] = "卒"

    "represents a playable peice on the board"
    def __init__(self,color="w"):
        self.color = color

    def possiblemoves(self,location,board):
        return []
#        return [(i,j) for i in range(10) for j in range(9)]

    def onboard(self,move):
        if 0 <= move[0] <= 9 and 0 <= move[1] <= 8 : return True
        return False

    def inpalace(self,move):
        black = [(i,j) for j in range(3,6) for i in range(0,4)]
        white = [(i,j) for j in range(3,6) for i in range(8,10)]
        if move in black or move in white: return True
        return False

    
    def south(self, location):
        i,j = location
        while i < 9:
            i +=1
            yield (i,j)

    def north(self, location):
        i,j = location
        while i >= 0:
            i -=1
            yield (i,j)

    def east(self, location):
        i,j = location
        while j >= 0:
            j -=1
            yield (i,j)

    def west(self, location):
        i,j = location
        while j < 8:
            j +=1
            yield (i,j)

    def enemey(self, otherpiece):
        if otherpiece:
            if self.color != otherpiece.color:
                return True
        return False

    def friendly(self, otherpiece):
        if otherpiece:
            if self.color == otherpiece.color:
                return True
        return False


class Pawn(Piece):
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "卒"
        else:
            return "兵"
        
    def possiblemoves(self,location,board):
        if self.color == "b":
            moves = [(location[0]-1,location[1])]
            if location[0] < 5:
                moves.append( (location[0]-1,location[1]+1) )
                moves.append( (location[0]-1,location[1]-1) )
        else:
            moves = [(location[0]+1,location[1])]
            if location[0] > 4:
                moves.append( (location[0]+1,location[1]+1) )
                moves.append( (location[0]+1,location[1]-1) )
        return moves

class Cannon(Piece):
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "砲"
        else:
            return "炮"
    def possiblemoves(self,location,board):
        def rookmoves(board,directiongenerator):
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
        moves.extend(rookmoves(board,self.north(location)))
        moves.extend(rookmoves(board,self.south(location)))
        moves.extend(rookmoves(board,self.east(location)))
        moves.extend(rookmoves(board,self.west(location)))
        return list(filter(self.onboard,moves))


class Rook(Piece):
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "車"
        else:
            return "俥"

    def possiblemoves(self,location,board):
        def rookmoves(board,directiongenerator):
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
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "馬"
        else:
            return "馬"

    def possiblemoves(self,location,board):
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
        return list(filter(self.onboard,moves))

class Elephant(Piece):
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "象"
        else:
            return "相"
    def possiblemoves(self,location,board):
        def thissideoftheriver(location):
            if self.color == "w" and location[0] < 5:
                return True
            if self.color == "b" and location[0] > 4:
                return True
            return False
        i,j = location
        moves = [(i+2,j+2),(i+2,j-2),(i-2,j-2),(i-2,j+2)]
        moves = filter(thissideoftheriver,moves)
        return list(filter(self.onboard,moves))


class Advisor(Piece):
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "士"
        else:
            return "仕"

    def possiblemoves(self,location,board):
        i,j = location
        moves = [(i+1,j+1),(i+1,j-1),(i-1,j-1),(i-1,j+1)]
        return list(filter(self.inpalace,moves))


class General(Piece):
    def __init__(self,color="w"):
        self.color = color

    def __repr__(self):
        if self.color == "b":
            return "帥"
        else:
            return "將"
        
    def possiblemoves(self,location,board):
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
        return list(moves)
#        return list(filter(self.inpalace,moves))

