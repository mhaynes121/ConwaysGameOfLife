# Conway's Game of Life
import random
import time
import os
import sys

from lifeForm import lifeform

gameboard = []
modifiedGameboard = []
debugMode = False
boardRows = 0
boardCols = 0

# replace existing gameboard with modified version
def copyGameboard(fromBoard, toBoard) -> None:
    toBoard.clear()
    row = 0
    col = 0
    while row < len(fromBoard):
        colData = []
        col = 0
        while col < len(fromBoard[0])-1:
            colData.append(fromBoard[row][col])
            col += 1
        row += 1
        toBoard.append(colData)

# create a rows x cols grid of dead lifeforms.
def populateGameboard(rows:int, cols:int) -> None:
    row = 0
    col = 0
    while row < rows:
        i1 = []
        col = 0
        while col < cols:
            i1.append(lifeform(row, col, 0, False))
            col += 1
        row += 1
        gameboard.append(i1)   
    copyGameboard(gameboard, modifiedGameboard)

# create the initial lifeform(s)
def bigBang(lifeSeeds:int=1) -> None: 
    curSeed = 0
    maxX = len(gameboard)-1
    maxY = len(gameboard[0])-1

    while curSeed < lifeSeeds:
        random.seed()
        xpos = random.randrange(0, maxX, 1)
        ypos = random.randrange(0, maxY, 1)
        modifiedGameboard[xpos][ypos].beginLife()
        curSeed += 1
    copyGameboard(modifiedGameboard, gameboard)

# displays the gameboard with life status for each lifeform
def showLife() -> None: 
    os.system('cls')
    i = 0
    while i < len(gameboard):
        j = 0
        while j < len(gameboard[0]):
            gameboard[i][j].printSelf(debugMode)
            if j == len(gameboard[0])-1:
                print('\n')
            j += 1
        i += 1

# determine who lives and dies
def evolveLife() -> None:
    # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    # Any live cell with two or three live neighbors lives on to the next generation.
    # Any live cell with more than three live neighbors dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
    rows = 0
    while rows <= (len(gameboard)-1):
        cols = 0
        while cols <= (len(gameboard[0])-1):
            newLF = modifiedGameboard[rows][cols]
            oldLF = gameboard[rows][cols] 

            if oldLF.neighbors < 2 or oldLF.neighbors > 3:
                newLF.endLife()
            elif oldLF.neighbors == 3 and oldLF.isAlive() is False:
                newLF.beginLife()
            cols +=1
        rows += 1

# lets see if there are any lifeforms around us
def census(gameBoard) -> None:
    rows = 0
    while rows <= (len(gameBoard)-1):
        cols = 0
        while cols <= (len(gameBoard[0])-1):
            curLF = gameboard[rows][cols]
            neighborCount = 0 
            if curLF.ypos > 0 and gameBoard[rows][cols-1].isAlive():
                neighborCount += 1
            if curLF.ypos < len(gameboard[0])-1 and gameBoard[rows][cols+1].isAlive():
                neighborCount += 1
            if curLF.xpos < len(gameboard)-1 and gameBoard[rows+1][cols].isAlive():
                neighborCount += 1
            if curLF.xpos > 0 and gameBoard[rows-1][cols].isAlive():
                neighborCount += 1
            if (curLF.xpos > 0 and curLF.ypos > 0) and gameBoard[rows-1][cols-1].isAlive():
                neighborCount += 1
            if (curLF.xpos > 0 and curLF.ypos < len(gameboard[0])-1) and gameBoard[rows-1][cols+1].isAlive():
                neighborCount += 1
            if (curLF.xpos < len(gameboard)-1 and curLF.ypos < len(gameboard[0])-1) and gameBoard[rows+1][cols+1].isAlive():
                neighborCount += 1
            if (curLF.xpos < len(gameboard)-1 and curLF.ypos > 0) and gameBoard[rows+1][cols-1].isAlive():
                neighborCount += 1
            curLF.neighbors = neighborCount
            cols += 1
        rows +=1

# main game loop
#   populate the gameboard
#   start the world into motion with a big bang (# of seeds to plant)
#   perform a census to see how many neighbors each lifeform has
#   showLife() to display the world
#   begin the game loop 
#       perform a census to update neighbor count
#       evolve life to create, sustain, destroy lifeforms
#       copy modified gameboard to existing one
#       showLife() to display the updated world
def main():
    try:
        populateGameboard(boardRows, boardCols)
        #populateGameboard(25, 75)
        totalLifeForms = len(gameboard) * len(gameboard[0])
        bigBang(random.randrange(int((totalLifeForms*.25)), int((totalLifeForms*.40)), 1))
        census(gameboard)
        showLife()
        pretime = time.time()
        while (True):
            posttime = time.time()
            if posttime - pretime > 1:
                pretime = time.time()
                # evolve life a generation
                evolveLife()
                copyGameboard(modifiedGameboard, gameboard)
                census(gameboard)
                showLife()            
                #input('Press key to continue...')
    except KeyboardInterrupt:
        os.system('cls')
        print('We hope you had fun watching your world evolve! See you again, soon!')
        sys.exit()
    
if __name__ == "__main__":
    boardRows = int(sys.argv[1])
    boardCols = int(sys.argv[2])
    debugMode = True if (sys.argv[3].lower() == 'true' or sys.argv[3].lower() == 't' or sys.argv[3] == '1') else False
    main()