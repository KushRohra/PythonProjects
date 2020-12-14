# O(nLog(n)) + O(mLog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    indexOne = 0
    indexTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        firstNum = arrayOne[indexOne]
        secondNum = arrayTwo[indexTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            indexOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indexTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair
