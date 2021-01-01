import allVariables


class rook:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture
        self.hasMoved = False

    def possibleMoves(self, x, y):
        listOfPossibleMoves = []
        tmpx = x + 1
        tmpy = y + 1

        #oben
        while tmpx < 8:
            if allVariables.Field[tmpx][y] is not None:
                if allVariables.Field[tmpx][y].color != self.color:
                    listOfPossibleMoves.append([tmpx, y])
                break
            listOfPossibleMoves.append([tmpx, y])
            tmpx = tmpx + 1
        tmpy = y - 1
        # links
        while tmpy >= 0:
            if allVariables.Field[x][tmpy] is not None:
                if allVariables.Field[x][tmpy].color != self.color:
                    listOfPossibleMoves.append([x, tmpy])
                break
            listOfPossibleMoves.append([x, tmpy])
            tmpy = tmpy - 1
        tmpx = x - 1
        # unten
        while tmpx >= 0:
            if allVariables.Field[tmpx][y] is not None:
                if allVariables.Field[tmpx][y].color != self.color:
                    listOfPossibleMoves.append([tmpx, y])
                break
            listOfPossibleMoves.append([tmpx, y])
            tmpx = tmpx - 1
        tmpy = y + 1
        # rechts
        while tmpy < 8:
            if allVariables.Field[x][tmpy] is not None:
                if allVariables.Field[x][tmpy].color != self.color:
                    listOfPossibleMoves.append([x, tmpy])
                break
            listOfPossibleMoves.append([x, tmpy])
            tmpy = tmpy + 1
        return listOfPossibleMoves

    def getColor(self):
        return self.color

    def getTexture(self):
        return self.texture