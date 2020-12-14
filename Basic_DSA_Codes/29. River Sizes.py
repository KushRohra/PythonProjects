def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] == True:
                continue
            traverseNode(i, j, matrix, visited, sizes)


def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        i, j = nodesToExplore.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)

    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, matrix, visited):
    nodesToReturn = []
    X = [-1, 0, 0, 1]
    Y = [0, 1, -1, 0]
    for k in range(4):
        newX = i + X[k]
        newY = j + Y[k]
        if newX >= 0 and newX < len(matrix) and newY >= 0 and newY < len(matrix[0]) and matrix[newX][newY] == 1 and \
                visited[newX][newY] == False:
            nodesToReturn.append([newX, newY])
    return nodesToReturn
