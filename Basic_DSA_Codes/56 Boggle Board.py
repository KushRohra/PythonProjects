def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(i, j, trie.root, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
    if visited[i][j]:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited[i][j] = True
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbors(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited[i][j] = False

def getNeighbors(i, j, board):
    neighbors = []
    n = len(board)
    m = len(board[0])
    coord = [[-1,-1], [-1,1], [1,1], [1,-1], [-1,0], [1,0], [0,-1], [0,1]]
    for x,y in coord:
        X = i + x
        Y = j + y
        if inBoard(X, Y, n, m):
            neighbors.append([X,Y])
    return neighbors

def inBoard(x, y, n, m):
    return x >= 0 and y >= 0 and x < n and y < m

class Trie:
    def __init__(self):
        self.root= {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = curren[letter]
        current[self.endSymbol] = word
