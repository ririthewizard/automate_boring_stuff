import random, time, copy

WIDTH = 60
HEIGHT = 20

board = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(" ")
    board.append(column)

while True:
    print("\n\n\n\n\n")
    currentBoard = copy.deepcopy(board)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentBoard[x][y], end="")
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            upCoord = (y + 1) % HEIGHT
            downCoord = (y - 1) % HEIGHT

            numNeighbors = 0
            if currentBoard[leftCoord][upCoord] == "#":
                numNeighbors += 1
            if currentBoard[x][upCoord] == "#":
                numNeighbors += 1
            if currentBoard[rightCoord][upCoord] == "#":
                numNeighbors += 1
            if currentBoard[rightCoord][y] == "#":
                numNeighbors += 1
            if currentBoard[rightCoord][downCoord] == "#":
                numNeighbors += 1
            if currentBoard[x][downCoord] == "#":
                numNeighbors += 1
            if currentBoard[leftCoord][downCoord] == "#":
                numNeighbors += 1
            if currentBoard[leftCoord][y] == "#":
                numNeighbors += 1
            
            if currentBoard[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                board[x][y] == "#"
            elif currentBoard[x][y] == " " and numNeighbors == 3:
                board[x][y] == "#"
            else:
                board[x][y] = " "
    
    time.sleep(1)

            