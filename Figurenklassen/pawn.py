import allVariables

class pawn:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture

    def possibleMoves(self, x, y):
        listOfPossibleMoves = []
        if self.color == "White":
            if x == 1 and allVariables.Field[x + 1][y] is None and allVariables.Field[x+2][y] is None:
                listOfPossibleMoves.append([x+2, y])
            if allVariables.Field[x+1][y] is None:
                listOfPossibleMoves.append([x+1, y])
            try:
                if allVariables.Field[x+1][y+1] is not None:
                    if allVariables.Field[x + 1][y +1].color != self.color:
                        listOfPossibleMoves.append([x+1, y+1])
            except IndexError:
                pass
            try:
                if allVariables.Field[x+1][y-1] is not None:
                    if allVariables.Field[x+1][y-1].color != self.color:
                        listOfPossibleMoves.append([x+1, y-1])
            except IndexError:
                pass

            return listOfPossibleMoves

        else:
            if x == 6 and allVariables.Field[x - 1][y] is None and allVariables.Field[x - 2][y] is None:
                listOfPossibleMoves.append([x - 2, y])
            if allVariables.Field[x - 1][y] is None:
                listOfPossibleMoves.append([x - 1, y])
            try:
                if allVariables.Field[x - 1][y + 1] is not None:
                    if allVariables.Field[x - 1][y + 1].color != self.color:
                        listOfPossibleMoves.append([x - 1, y + 1])
            except IndexError:
                pass
            try:
                if allVariables.Field[x - 1][y - 1] is not None:
                    if allVariables.Field[x - 1][y - 1].color != self.color:
                        listOfPossibleMoves.append([x - 1, y - 1])
            except IndexError:
                pass

            return listOfPossibleMoves


    def getColor(self):
        return self.color

    def getTexture(self):
        return self.texture
