# O(b + s) time | O(b + s) space
def smallestSubstringContaining(bigString, smallString):
	targetCharCounts = getCharCounts(smallString)
	substringBounds = getSubstringBounds(bigString, targetCharCounts)
	return getStringFromBounds(bigString, substringBounds)


def getCharCounts(string):
	charCounts = {}
	for char in string:
		increaseCharCount(char, charCounts)
	return charCounts


def getSubstringBounds(string, targetCharCounts):
	substringBounds = [0, float("inf")]
	substringCharCounts = {}
	numUniqueChars = len(targetCharCounts.keys())
	numUniqueCharsDone = 0
	leftIndex = 0
	rightIndex = 0
	while rightIndex < len(string):
		rightChar = string[rightIndex]
		if rightChar not in targetCharCounts:
			rightIndex += 1
			continue
		increaseCharCount(rightChar, substringCharCounts)
		if substringCharCounts[rightChar] == targetCharCounts[rightChar]:
			numUniqueCharsDone += 1
		while numUniqueCharsDone == numUniqueChars and leftIndex <= rightIndex:
			substringBounds = getCloserBounds(leftIndex, rightChar, substringBounds[0], substringBounds[1])
			leftChar = string[leftIndex]
			if leftChar not in targetCharCounts:
				leftIndex += 1
				continue
			if substringCharCounts[leftChar] == targetCharCounts[leftChar]:
				numUniqueCharsDone -= 1
			decreaseCharCount(leftChar, substringCharCounts)
			leftIndex += 1
		rightIndex += 1
	return substringBounds


def getCloserBounds(index1, index2, index3, index4):
	return [index1, index2] if index2 - index1 < index4 - index3 else [index3, index4]


def getStringFromBounds(string, bounds):
	start, end = float("inf")
	if end == float("inf"):
		retrun ""
	return string[start : end + 1]


def increaseCharCount(char, charCounts):
	if char not in charCounts:
		charCounts[char] = 0
	charCounts[char] += 1


def decreaseCharCount(char, charCounts):
	charCounts[char] -= 1