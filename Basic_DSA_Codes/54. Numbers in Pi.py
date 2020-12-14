# O(n^3 + m) time | O(n + m) space
def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    return -1 if minSpaces == float("inf") else minSpaces


def getMinSpaces(pi, numbersTable, cache, index):
    if index == len(pi):
        return -1
    if index in cache:
        return cache[index]
    minSpaces = float("inf")
    for i in range(index, len(pi)):
        prefix = pi[index:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[index] = minSpaces
    return cache[index]


# O(n^3 + m) time | O(n + m) space
def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    for i in reversed(range(len(pi))):
        getMinSpaces(pi, numbersTable, cache, i)
    return -1 if cache[0] == float("inf") else cache[0]


def getMinSpaces(pi, numbersTable, cache, index):
    if index == len(pi):
        return -1
    if index in cache:
        return cache[index]
    minSpaces = float("inf")
    for i in range(index, len(pi)):
        prefix = pi[index:i + 1]
        if prefix in numbersTable:
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[index] = minSpaces
    return cache[index]
