import allVariables


class king:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture
        self.hasMoved = False
        self.possibleCastleShort = False
        self.possibleCastleLong = False

    def possibleMoves(self, x, y):
        listOfPossibleMoves = []
        try:
            if allVariables.Field[x + 1][y].color != self.color and x + 1 <= 7:
                listOfPossibleMoves.append([x + 1, y])
        except AttributeError:
            if x + 1 <= 7:
                listOfPossibleMoves.append([x + 1, y])
        except IndexError:
            pass
        try:
            if allVariables.Field[x + 1][y - 1].color != self.color and x + 1 <= 8 and y - 1 >= 0:
                listOfPossibleMoves.append([x + 1, y - 1])
        except AttributeError:
            if x + 1 <= 8 and y - 1 >= 0:
                listOfPossibleMoves.append([x + 1, y - 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x + 1][y + 1].color != self.color and x + 1 <= 7 and y + 1 <= 7:
                listOfPossibleMoves.append([x + 1, y + 1])
        except AttributeError:
            if  x + 1 <= 7 and y + 1 <= 7:
                listOfPossibleMoves.append([x + 1, y + 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 1][y].color != self.color and x - 1 >= 0:
                listOfPossibleMoves.append([x - 1, y])
        except AttributeError:
            if x - 1 >= 0:
                listOfPossibleMoves.append([x - 1, y])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 1][y - 1].color != self.color and x - 1 >= 0 and y - 1 >= 0:
                listOfPossibleMoves.append([x - 1, y - 1])
        except AttributeError:
            if x - 1 >= 0 and y - 1 >= 0:
                listOfPossibleMoves.append([x - 1, y - 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 1][y + 1].color != self.color and x - 1 >= 0 and y + 1 <= 7:
                listOfPossibleMoves.append([x - 1, y + 1])
        except AttributeError:
            if x - 1 >= 0 and y + 1 <= 7:
                listOfPossibleMoves.append([x - 1, y + 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x][y - 1].color != self.color and y - 1 >= 0:
                listOfPossibleMoves.append([x, y - 1])
        except AttributeError:
            if y - 1 >= 0:
                listOfPossibleMoves.append([x, y - 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x][y + 1].color != self.color and y + 1 <= 7:
                listOfPossibleMoves.append([x, y + 1])
        except AttributeError:
            if y + 1 <= 7:
                listOfPossibleMoves.append([x, y + 1])
        if self.color == "White":
            if allVariables.Field[0][5] is None and allVariables.Field[0][6] is None and self.hasMoved == False and type(
                    allVariables.Field[0][7]) == type(allVariables.hRookWhite) and allVariables.Field[0][7].hasMoved == False:
                self.possibleCastleShort = True
                listOfPossibleMoves.append([0, 6])
            else:
                self.possibleCastleShort = False
            if allVariables.Field[0][1] is None and allVariables.Field[0][2] is None and self.hasMoved == False and type(
                    allVariables.Field[0][0]) == type(allVariables.hRookWhite) and allVariables.Field[0][0].hasMoved == False:
                self.possibleCastleLong = True
                listOfPossibleMoves.append([0, 2])
            else:
                self.possibleCastleLong = False
        else:
            if allVariables.Field[7][1] is None and allVariables.Field[7][2] is None and self.hasMoved == False and type(
                    allVariables.Field[7][0]) == type(allVariables.aRookBlack) and allVariables.Field[7][0].hasMoved == False:
                self.possibleCastleLong = True
                listOfPossibleMoves.append([7, 2])
            else:
                self.possibleCastleLong = False
            if allVariables.Field[7][5] is None and allVariables.Field[7][6] is None and self.hasMoved == False and type(
                    allVariables.Field[7][7]) == type(allVariables.hRookBlack) and allVariables.Field[7][7].hasMoved == False:
                self.possibleCastleShort = True
                listOfPossibleMoves.append([7, 6])
        return listOfPossibleMoves

    def getColor(self):
        return self.color

    def getTexture(self):
        return self.texture

    def isCheck(self, color, future):
        if not future:
            if color == "White":
                for i in range(0, 8):
                    for j in range(0, 8):
                        if type(allVariables.Field[i][j]) == type(allVariables.kingWhite):
                            x = i
                            y = j
                            break
                    else:
                        continue
                    break
            else:
                for i in range(0, 8):
                    for j in range(0, 8):
                        if type(allVariables.Field[i][j]) == type(allVariables.kingBlack):
                            x = i
                            y = j
                            break
            for i in range(0, 8):
                for j in range(0, 8):
                    if allVariables.Field[i][j] is not None:
                        if allVariables.Field[i][j].color != color:
                            if allVariables.Field[i][j].possibleMoves(i, j) is not None:
                                for k in allVariables.Field[i][j].possibleMoves(i, j):
                                    if k == [x, y]:
                                        print("check")
                                        return True
            return False
        else:
            if color == "White":
                for i in range(0, 8):
                    for j in range(0, 8):
                        if type(allVariables.FutureField[i][j]) == type(allVariables.kingWhite):
                            x = i
                            y = j
                            break
                    else:
                        continue
                    break
            else:
                for i in range(0, 8):
                    for j in range(0, 8):
                        if type(allVariables.FutureField[i][j]) == type(allVariables.kingBlack):
                            x = i
                            y = j
                            break
            for i in range(0, 8):
                for j in range(0, 8):
                    if allVariables.FutureField[i][j] is not None:
                        if allVariables.FutureField[i][j].color != color:
                            if allVariables.FutureField[i][j].possibleMoves(i, j) is not None:
                                for k in allVariables.FutureField[i][j].possibleMoves(i, j):
                                    if k == [x, y]:
                                        print("check")
                                        return True
            return False
