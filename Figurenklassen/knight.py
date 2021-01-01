import allVariables


class knight:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture

    def possibleMoves(self, x, y):
        listOfPossibleMoves = []
        try:
            if allVariables.Field[x + 2][y + 1].color != self.color  and x+2 <= 7 and y+1 <= 7:
                listOfPossibleMoves.append([x + 2, y + 1])
        except AttributeError:
            listOfPossibleMoves.append([x + 2, y + 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 2][y + 1].color != self.color and x-2 >= 0 and y+1 <= 7:
                listOfPossibleMoves.append([x - 2, y + 1])
        except AttributeError:
            listOfPossibleMoves.append([x - 2, y + 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x + 2][y - 1].color != self.color and x+2 <= 7 and y-1 >= 0:
                listOfPossibleMoves.append([x + 2, y - 1])
        except AttributeError:
            listOfPossibleMoves.append([x + 2, y - 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 2][y - 1].color != self.color and x-2 >= 0 and y-1 >= 0:
                listOfPossibleMoves.append([x - 2, y - 1])
        except AttributeError:
            listOfPossibleMoves.append([x - 2, y - 1])
        except IndexError:
            pass
        try:
            if allVariables.Field[x + 1][y + 2].color != self.color and x+1 <= 7 and y+2 <= 7:
                listOfPossibleMoves.append([x + 1, y + 2])
        except AttributeError:
            listOfPossibleMoves.append([x + 1, y + 2])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 1][y + 2].color != self.color and x-1 >= 0 and y+2 <= 7:
                listOfPossibleMoves.append([x - 1, y + 2])
        except AttributeError:
            listOfPossibleMoves.append([x - 1, y + 2])
        except IndexError:
            pass
        try:
            if allVariables.Field[x + 1][y - 2].color != self.color and x+1 <= 7 and y-2 >= 0:
                listOfPossibleMoves.append([x + 1, y - 2])
        except AttributeError:
            listOfPossibleMoves.append([x + 1, y - 2])
        except IndexError:
            pass
        try:
            if allVariables.Field[x - 1][y - 2].color != self.color and x-1 >= 0 and y-2 >= 0:
                listOfPossibleMoves.append([x - 1, y - 2])
        except AttributeError:
            listOfPossibleMoves.append([x - 1, y - 2])
        except IndexError:
            pass
        return listOfPossibleMoves

    def getColor(self):
        return self.color

    def getTexture(self):
        return self.texture