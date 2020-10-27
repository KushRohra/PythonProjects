import queue
import random


def createMaze():
    spaces = 1
    while spaces < 2:
        print("The total no of cells should be more than 2")
        rows = int(input("Enter the no of rows for your maze: "))
        cols = int(input("Enter the no of columns for your maze: "))
        spaces = rows * cols
        print()

    maze = [[" " for i in range(cols)] for j in range(rows)]

    # Getting a random start and end point in a matrix
    startPos = random.randint(0, spaces - 1)
    startPosX = int(startPos / cols)
    startPosY = int(startPos % cols)

    endPos = random.randint(0, spaces - 1)
    while endPos == startPos:
        endPos = random.randint(0, spaces)
    endPosX = int(endPos / cols)
    endPosY = int(endPos % cols)

    maze[startPosX][startPosY] = "O"
    maze[endPosX][endPosY] = "X"

    # Generating Some Obstacles
    no_of_Obstacles = int(spaces / 3)
    while no_of_Obstacles > 0:
        randomPos = random.randint(0, spaces - 1)
        randomPosX = int(randomPos / cols)
        randomPosY = int(randomPos % cols)
        if maze[randomPosX][randomPosY] == " ":
            maze[randomPosX][randomPosY] = "#"
            no_of_Obstacles -= 1

    return maze


# BFS Code for traversal
def findPath(maze, i, j, endPosX, endPosY, rows, cols):
    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]

    q = queue.Queue()
    q.put([i, j, 0])

    visited = [[False for i in range(cols)] for j in range(rows)]

    visited[i][j] = True

    while q:
        currX, currY, dist = q.get()
        if currX == endPosX and currY == endPosY:
            return [True, dist]
        for i in range(4):
            row = currX + rowNum[i]
            col = currY + colNum[i]
            if isValid(row, col, rows, cols) and maze[row][col] != "#" and visited[row][col] == False:
                visited[row][col] = True
                q.put([row, col, dist+1])

    return [False, -1]


def isValid(i, j, rows, cols):
    if i >=0 and j>=0 and i<rows and j<cols:
        return True
    return False


def findPos(maze, char):
    i = 0
    for row in maze:
        j = 0
        for x in row:
            if x == char:
                return [i, j]
            j += 1
        i += 1
    return [-1, -1]


maze = createMaze()

startPosX, startPosY = findPos(maze, "O")
endPosX, endPosY = findPos(maze, "X")
rows = len(maze)
cols = len(maze[0])

for row in maze:
    print(row)

foundPath, distance = findPath(maze, startPosX, startPosY, endPosX, endPosY, rows, cols)

if foundPath:
    print("Found Path at a distance of "+str(distance))
else:
    print("Path not found")