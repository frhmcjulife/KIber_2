import allVariables

class queen:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture

    def possibleMoves(self, x, y):
        listOfPossibleMoves = []
        tmpx = x + 1
        tmpy = y + 1

        # rechts oben
        while tmpx < 8 and tmpy < 8:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    listOfPossibleMoves.append([tmpx, tmpy])
                break
            listOfPossibleMoves.append([tmpx, tmpy])
            tmpx = tmpx + 1
            tmpy = tmpy + 1
        tmpx = x + 1
        tmpy = y - 1
        # links oben
        while tmpx < 8 and tmpy >= 0:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    listOfPossibleMoves.append([tmpx, tmpy])
                break
            listOfPossibleMoves.append([tmpx, tmpy])
            tmpx = tmpx + 1
            tmpy = tmpy - 1
        tmpx = x - 1
        tmpy = y - 1
        # links unten
        while tmpx >= 0 and tmpy >= 0:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    listOfPossibleMoves.append([tmpx, tmpy])
                break
            listOfPossibleMoves.append([tmpx, tmpy])
            tmpx = tmpx - 1
            tmpy = tmpy - 1
        tmpx = x - 1
        tmpy = y + 1
        # rechts unten
        while tmpx >= 0 and tmpy < 8:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    listOfPossibleMoves.append([tmpx, tmpy])
                break
            listOfPossibleMoves.append([tmpx, tmpy])
            tmpx = tmpx - 1
            tmpy = tmpy + 1
        tmpx = x + 1
        # oben
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