import allVariables


class bishop:
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
                    if self.color == "White":
                        if not allVariables.kingBlack.isCheck("Black", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                    else:
                        if not allVariables.kingWhite.isCheck("White", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                break
            if self.color == "White":
                if not allVariables.kingBlack.isCheck("Black", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            else:
                if not allVariables.kingWhite.isCheck("White", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            tmpx = tmpx + 1
            tmpy = tmpy + 1
        tmpx = x + 1
        tmpy = y - 1
        # links oben
        while tmpx < 8 and tmpy >= 0:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    if self.color == "White":
                        if not allVariables.kingBlack.isCheck("Black", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                    else:
                        if not allVariables.kingWhite.isCheck("White", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                break
            allVariables.FutureField[x][y] = allVariables.FutureField[tmpx][tmpy]
            allVariables.FutureField[tmpx][tmpy] = None
            if self.color == "White":
                if not allVariables.kingBlack.isCheck("Black", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            else:
                if not allVariables.kingWhite.isCheck("White", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            tmpx = tmpx + 1
            tmpy = tmpy - 1
        tmpx = x - 1
        tmpy = y - 1
        # links unten
        while tmpx >= 0 and tmpy >= 0:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    if self.color == "White":
                        if not allVariables.kingBlack.isCheck("Black", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                    else:
                        if not allVariables.kingWhite.isCheck("White", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                break
            if self.color == "White":
                if not allVariables.kingBlack.isCheck("Black", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            else:
                if not allVariables.kingWhite.isCheck("White", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            tmpx = tmpx - 1
            tmpy = tmpy - 1
        tmpx = x - 1
        tmpy = y + 1
        # rechts unten
        while tmpx >= 0 and tmpy < 8:
            if allVariables.Field[tmpx][tmpy] is not None:
                if allVariables.Field[tmpx][tmpy].color != self.color:
                    if self.color == "White":
                        if not allVariables.kingBlack.isCheck("Black", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                    else:
                        if not allVariables.kingWhite.isCheck("White", True):
                            listOfPossibleMoves.append([tmpx, tmpy])
                            allVariables.FutureField = allVariables.Field
                break
            if self.color == "White":
                if not allVariables.kingBlack.isCheck("Black", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            else:
                if not allVariables.kingWhite.isCheck("White", True):
                    listOfPossibleMoves.append([tmpx, tmpy])
                    allVariables.FutureField = allVariables.Field
            tmpx = tmpx - 1
            tmpy = tmpy + 1
        return listOfPossibleMoves

    def getColor(self):
        return self.color

    def getTexture(self):
        return self.texture