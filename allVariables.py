from Figurenklassen import pawn
from Figurenklassen import bishop
from Figurenklassen import king
from Figurenklassen import queen
from Figurenklassen import knight
from Figurenklassen import rook
import pygame

FieldPositions = [[[85, 647, 168, 730],  #Row1 definieren mit pixelwerten
                   [171, 647, 253, 730],
                   [256, 647, 338, 730],
                   [341, 647, 423, 730],
                   [426, 647, 508, 730],
                   [511, 647, 593, 730],
                   [597, 647, 678, 730],
                   [681, 647, 763, 730]],
                   [[85, 562, 168, 645],  #Row2 definieren mit pixelwerten
                   [171, 562, 253, 645],
                   [256, 562, 338, 645],
                   [341, 562, 423, 645],
                   [426, 562, 508, 645],
                   [511, 562, 593, 645],
                   [597, 562, 678, 645],
                   [681, 562, 763, 645]],
                   [[85, 476, 168, 558],  # Row3 definieren mit pixelwerten
                   [171, 476, 253, 558],
                   [256, 476, 338, 558],
                   [341, 476, 423, 558],
                   [426, 476, 508, 558],
                   [511, 476, 593, 558],
                   [597, 476, 678, 558],
                   [681, 476, 763, 558]],
                   [[85, 391, 168, 471],  # Row4 definieren mit pixelwerten
                   [171, 391, 253, 471],
                   [256, 391, 338, 471],
                   [341, 391, 423, 471],
                   [426, 391, 508, 471],
                   [511, 391, 593, 471],
                   [597, 391, 678, 471],
                   [681, 391, 763, 471]],
                   [[85, 306, 168, 384],  # Row5 definieren mit pixelwerten
                   [171, 306, 253, 384],
                   [256, 306, 338, 384],
                   [341, 306, 423, 384],
                   [426, 306, 508, 384],
                   [511, 306, 593, 384],
                   [597, 306, 678, 384],
                   [681, 306, 763, 384]],
                   [[85, 221, 168, 299],  # Row6 definieren mit pixelwerten
                   [171, 221, 253, 299],
                   [256, 221, 338, 299],
                   [341, 221, 423, 299],
                   [426, 221, 508, 299],
                   [511, 221, 593, 299],
                   [596, 221, 678, 299],
                   [681, 221, 763, 299]],
                   [[85, 135, 168, 212],  # Row7 definieren mit pixelwerten
                   [171, 135, 253, 212],
                   [256, 135, 338, 212],
                   [341, 135, 423, 212],
                   [426, 135, 508, 212],
                   [511, 135, 593, 212],
                   [596, 135, 678, 212],
                   [681, 135, 763, 212]],
                   [[85, 50, 168, 125],  # Row8 definieren mit pixelwerten
                   [171, 50, 253, 125],
                   [256, 50, 338, 125],
                   [341, 50, 423, 125],
                   [426, 50, 508, 125],
                   [511, 50, 593, 125],
                   [596, 50, 678, 125],
                   [681, 50, 763, 125]]]



whitePawnTexture = pygame.image.load("./textures/Bauer_1.png")
whiteKnightTexture = pygame.image.load("./textures/Springer_1.png")
whiteBishopTexture = pygame.image.load("./textures/Laeufer_1.png")
whiteQueenTexture = pygame.image.load("./textures/Dame_1.png")
whiteKingTexture = pygame.image.load("./textures/Koenig_1.png")
whiteRookTexture = pygame.image.load("./textures/Turm_1.png")
blackPawnTexture = pygame.image.load("./textures/Bauer_1_s.png")
blackKnightTexture = pygame.image.load("./textures/Springer_1_s.png")
blackBishopTexture = pygame.image.load("./textures/Laeufer_1_s.png")
blackQueenTexture = pygame.image.load("./textures/Dame_1_s.png")
blackKingTexture = pygame.image.load("./textures/Koenig_1_s.png")
blackRookTexture = pygame.image.load("./textures/Turm_1_s.png")
markTexture = pygame.image.load("./textures/markierung_1.png")
fieldTexture = pygame.image.load("./textures/Schachbrett_x512.png")

aPawnWhite = pawn.pawn("White", whitePawnTexture)
bPawnWhite = pawn.pawn("White", whitePawnTexture)
cPawnWhite = pawn.pawn("White", whitePawnTexture)
dPawnWhite = pawn.pawn("White", whitePawnTexture)
ePawnWhite = pawn.pawn("White", whitePawnTexture)
fPawnWhite = pawn.pawn("White", whitePawnTexture)
gPawnWhite = pawn.pawn("White", whitePawnTexture)
hPawnWhite = pawn.pawn("White", whitePawnTexture)
bKnightWhite = knight.knight("White", whiteKnightTexture)
gKnightWhite = knight.knight("White", whiteKnightTexture)
cBishopWhite = bishop.bishop("White", whiteBishopTexture)
fBishopWhite = bishop.bishop("White", whiteBishopTexture)
aRookWhite = rook.rook("White", whiteRookTexture)
hRookWhite = rook.rook("White", whiteRookTexture)
queenWhite = queen.queen("White", whiteQueenTexture)
kingWhite = king.king("White", whiteKingTexture)
aPawnBlack = pawn.pawn("Black", blackPawnTexture)
bPawnBlack = pawn.pawn("Black", blackPawnTexture)
cPawnBlack = pawn.pawn("Black", blackPawnTexture)
dPawnBlack = pawn.pawn("Black", blackPawnTexture)
ePawnBlack = pawn.pawn("Black", blackPawnTexture)
fPawnBlack = pawn.pawn("Black", blackPawnTexture)
gPawnBlack = pawn.pawn("Black", blackPawnTexture)
hPawnBlack = pawn.pawn("Black", blackPawnTexture)
bKnightBlack = knight.knight("Black", blackKnightTexture)
gKnightBlack = knight.knight("Black", blackKnightTexture)
cBishopBlack = bishop.bishop("Black", blackBishopTexture)
fBishopBlack = bishop.bishop("Black", blackBishopTexture)
aRookBlack = rook.rook("Black", blackRookTexture)
hRookBlack = rook.rook("Black", blackRookTexture)
queenBlack = queen.queen("Black", blackQueenTexture)
kingBlack = king.king("Black", blackKingTexture)
Field = [[aRookWhite, bKnightWhite, cBishopWhite, queenWhite, kingWhite, fBishopWhite, gKnightWhite, hRookWhite],
         [aPawnWhite, bPawnWhite, cPawnWhite, dPawnWhite, ePawnWhite, fPawnWhite, gPawnWhite, hPawnWhite],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [aPawnBlack, bPawnBlack, cPawnBlack, dPawnBlack, ePawnBlack, fPawnBlack, gPawnBlack, hPawnBlack],
         [aRookBlack, bKnightBlack, cBishopBlack, queenBlack, kingBlack, fBishopBlack, gKnightBlack, hRookBlack]]
FutureField = [[aRookWhite, bKnightWhite, cBishopWhite, queenWhite, kingWhite, fBishopWhite, gKnightWhite, hRookWhite],
         [aPawnWhite, bPawnWhite, cPawnWhite, dPawnWhite, ePawnWhite, fPawnWhite, gPawnWhite, hPawnWhite],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None],
         [aPawnBlack, bPawnBlack, cPawnBlack, dPawnBlack, ePawnBlack, fPawnBlack, gPawnBlack, hPawnBlack],
         [aRookBlack, bKnightBlack, cBishopBlack, queenBlack, kingBlack, fBishopBlack, gKnightBlack, hRookBlack]]