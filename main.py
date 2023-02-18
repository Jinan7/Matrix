#Jinan
#first proj
import pygame, sys, random
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 380
BOARDWIDTH = 10
BOARDHEIGHT = 10
BOXSIZE = 40
GAPSIZE = 1
XMARGIN = int(WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2
YMARGIN = int(WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2


WHITE = [255, 255, 255]
BLACK = [0,  0,  0]


BGCOLOR = BLACK

def main():
    global DISPLAYSURF, FPSCLOCK

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FPSCLOCK =pygame.time.Clock()
    pygame.display.set_caption('Fading Boxes Animation')

    while True:
         DISPLAYSURF.fill(BGCOLOR)
         mainBoard = generateBoard()
         for event in pygame.event.get():
             if event.type == QUIT:
                 pygame.quit()
                 sys.exit()

         fadeAnimation(mainBoard)

def generateHue(RGBINDEX):
    colour1 = []
    colourTemplate = [0, 0, 0]
    for value in range(10, 255, 4):
        colourTemplate[RGBINDEX] = value
        colour = tuple(colourTemplate)
        colour1.append(colour)
    colour2 = colour1.copy()
    colour1.reverse()
    color1 = colour1 + colour2
    color2 = colour2 + colour1
    return (color1, color2)

def generateColours():
    red1, red2 = generateHue(0)
    green1, green2 = generateHue(1)
    blue1, blue2 = generateHue(2)
    colourSet = [red1, red2, green1, green2, blue1, blue2]
    random.shuffle(colourSet)
    return colourSet

def generateBoard():
    board =[]

    colourSet = generateColours()
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            random.shuffle(colourSet)
            order =colourSet[0]
            column.append(order)
        board.append(column)
    return board

def leftTopCoords(boxx, boxy):
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)

def drawBox(boxx, boxy, color):
    left, top = leftTopCoords(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, color, (left, top, BOXSIZE, BOXSIZE))

def drawBoard(board, i):
    DISPLAYSURF.fill(BGCOLOR)
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            drawBox(boxx, boxy, board[boxx][boxy][i])
    pygame.display.update()

def fadeAnimation(board):
    for i in range(len(board[0][0])):
        drawBoard(board, i)
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
