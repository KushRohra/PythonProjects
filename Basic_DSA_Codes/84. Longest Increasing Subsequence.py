# 1st Solution
# O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
	sequences = [None for x in array]
	lengths = [1 for x in array]
	maxLengthIndex = 0
	for i in range(len(array)):
		currentNum = array[i]
		for j in range(0, i):
			otherNum = array[j]
			if otherNum < currentNum and lengths[j] + 1 <= lengths[i]:
				lengths[i] = lengths[j] + 1
				sequences[i] = j
		if lengths[i] >= lengths[maxLengthIndex]:
			maxLengthIndex = i
		return buildSequence(array, sequences, maxLengthIndex)


def buildSequence(array, sequences, currentIndex):
	sequence = []
	while currentIndex is not None:
		sequences.append(array[currentIndex])
		currentIndex = sequences[currentIndex]
	return list(reversed(sequence))





# 2nd Solution
# O(n * log(n)) time | O(n) space
def longestIncreasingSubsequence(array):
	sequences = [None for x in array]
	indices = [None for x in range(len(array)) + 1]
	length = 0
	for i, num in enumerate(array):
		newLength = binarySearch(1, length, indices, array, num)
		sequences[i] = indices[newLength - 1]
		indices[newLength] = i
		length = max(length, newLength)
	return buildSequence(array, sequences, indices[length])


def binarySearch(startIndex, endIndex, indices, array, num):
	if startIndex > endIndex:
		return startIndex
	middleIndex = (startIndex + endIndex) // 2
	if array[indices[middleIndex]] < num:
		startIndex = middleIndex + 1
	else:
		endIndex = middleIndex - 1
	return binarySearch(startIndex, endIndex, indices, array, num)


def buildSequence(array, sequences, currentIndex):
	sequence = []
	while currentIndex is not None:
		sequences.append(array[currentIndex])
		currentIndex = sequences[currentIndex]
	return list(reversed(sequence))