import pygame
import allVariables


#Variables
Turn = "White"
nowClicked = [None, None]
title = "Chess"
fps = 10


def updateFieldRefactored(window):
    window.blit(allVariables.fieldTexture, (50, 15))
    if nowClicked[0] != None:
        window.blit(allVariables.markTexture, (allVariables.FieldPositions[nowClicked[0]][nowClicked[1]][0], allVariables.FieldPositions[nowClicked[0]][nowClicked[1]][1]))
        for i in allVariables.Field[nowClicked[0]][nowClicked[1]].possibleMoves(nowClicked[0], nowClicked[1]):
            window.blit(allVariables.markTexture, (allVariables.FieldPositions[i[0]][i[1]][0], allVariables.FieldPositions[i[0]][i[1]][1]))
    for i in range(0, 8):
        for j in range(0, 8):
            if allVariables.Field[i][j] != None:
                texture = allVariables.Field[i][j].getTexture()
                window.blit(texture, (allVariables.FieldPositions[i][j][0], allVariables.FieldPositions[i][j][1]))

def ifCLickRefactored():
    global nowClicked
    global Turn
    mouse = pygame.mouse.get_pos()
    for i in range(0, 8): #Looks which Field is Clicked
        for j in range(0, 8):
            if allVariables.FieldPositions[i][j][1] < mouse[1] < allVariables.FieldPositions[i][j][3]:
                if allVariables.FieldPositions[i][j][0] < mouse[0] < allVariables.FieldPositions[i][j][2]:
                    if nowClicked[0] == None: #Marks if nothing is marked
                        try:
                            if Turn == allVariables.Field[i][j].getColor():
                                nowClicked = [i, j]
                        except AttributeError:
                            pass
                        break
                    else: # Marks if somthing is marked
                        if nowClicked[0] == i and nowClicked[1] == j:
                            nowClicked = [None, None]
                        elif allVariables.Field[i][j] != None:
                            if Turn == allVariables.Field[i][j].getColor():
                                nowClicked = [i, j]
                        if nowClicked[0] is not None: #Makes a move
                            if allVariables.Field[nowClicked[0]][nowClicked[1]].possibleMoves(nowClicked[0], nowClicked[1]) is not None:
                                for k in allVariables.Field[nowClicked[0]][nowClicked[1]].possibleMoves(nowClicked[0], nowClicked[1]):
                                    if type(allVariables.Field[nowClicked[0]][nowClicked[1]]) == type(allVariables.kingWhite) and i == 0 and j == 6 and allVariables.Field[nowClicked[0]][nowClicked[1]].possibleCastleShort == True:
                                        allVariables.Field[i][j] = allVariables.Field[nowClicked[0]][nowClicked[1]] #Verschiebt die Figur
                                        allVariables.Field[nowClicked[0]][nowClicked[1]] = None
                                        allVariables.Field[0][5] = allVariables.Field[nowClicked[0]][7]
                                        allVariables.Field[nowClicked[0]][7] = None
                                        nowClicked = [None, None]
                                        Turn = "Black"  # Changes Turns
                                        break
                                    if type(allVariables.Field[nowClicked[0]][nowClicked[1]]) == type(allVariables.kingWhite) and i == 0 and j == 2 and allVariables.Field[nowClicked[0]][nowClicked[1]].possibleCastleLong == True:
                                        allVariables.Field[i][j] = allVariables.Field[nowClicked[0]][nowClicked[1]]
                                        allVariables.Field[nowClicked[0]][nowClicked[1]] = None
                                        allVariables.Field[0][3] = allVariables.Field[nowClicked[0]][0]
                                        allVariables.Field[nowClicked[0]][0] = None
                                        nowClicked = [None, None]
                                        Turn = "Black" # Changes Turns
                                        break
                                    if type(allVariables.Field[nowClicked[0]][nowClicked[1]]) == type(allVariables.kingBlack) and i == 7 and j == 2 and allVariables.Field[nowClicked[0]][nowClicked[1]].possibleCastleLong == True:
                                        allVariables.Field[i][j] = allVariables.Field[nowClicked[0]][nowClicked[1]]
                                        allVariables.Field[nowClicked[0]][nowClicked[1]] = None
                                        allVariables.Field[7][3] = allVariables.Field[nowClicked[0]][0]
                                        allVariables.Field[nowClicked[0]][0] = None
                                        nowClicked = [None, None]
                                        Turn = "White" # Changes Turns
                                        break
                                    if type(allVariables.Field[nowClicked[0]][nowClicked[1]]) == type(allVariables.kingWhite) and i == 7 and j == 6 and allVariables.Field[nowClicked[0]][nowClicked[1]].possibleCastleShort == True:
                                        allVariables.Field[i][j] = allVariables.Field[nowClicked[0]][nowClicked[1]]
                                        allVariables.Field[nowClicked[0]][nowClicked[1]] = None
                                        allVariables.Field[7][5] = allVariables.Field[nowClicked[0]][7]
                                        allVariables.Field[nowClicked[0]][7] = None
                                        nowClicked = [None, None]
                                        Turn = "White"  # Changes Turns
                                        break
                                    if k == [i, j]:
                                        allVariables.FutureField[i][j] = allVariables.FutureField[nowClicked[0]][nowClicked[1]]
                                        allVariables.FutureField[nowClicked[0]][nowClicked[1]] = None
                                        if type(allVariables.Field[nowClicked[0]][nowClicked[1]]) in (type(allVariables.kingWhite),
                                                                                                      type(allVariables.aRookBlack),
                                                                                                      type(allVariables.hRookBlack),
                                                                                                      type(allVariables.aRookWhite),
                                                                                                      type(allVariables.hRookWhite),
                                                                                                      type(allVariables.kingBlack)):
                                            allVariables.Field[nowClicked[0]][nowClicked[1]].hasMoved = True
                                        allVariables.Field[i][j] = allVariables.Field[nowClicked[0]][nowClicked[1]]
                                        allVariables.Field[nowClicked[0]][nowClicked[1]] = None
                                        nowClicked = [None, None]
                                        if Turn == "White": #Changes Turns
                                            Turn = "Black"
                                        else:
                                            Turn = "White"
                                        return




def start(): # startfunktion die alles vorbereitet und die main schleife laufen lässt
    pygame.init()
    global fenster
    fenster = pygame.display.set_mode((1400, 800))
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    aktive = True
    while aktive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aktive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ifCLickRefactored()
        pygame.display.flip()
        clock.tick(fps)
        updateFieldRefactored(fenster)


if __name__ == '__main__':
    start()