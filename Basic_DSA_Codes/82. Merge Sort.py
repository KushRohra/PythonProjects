# 1st solution
# O(n * log(n)) time | O(n * log(n)) space
def mergeSort(array):
	if len(array) == 1:
		return array
	middleIndex = len(array) // 2
	leftHalf = array[:middleIndex]
	rightHalf = array[middleIndex:]
	return mergeSortedArray(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArray(leftHalf, rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	k = i = j = 0
	while i <  len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] <= rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = rightHalf[j]
			j += 1
		k += 1
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i += 1
		k += 1
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j += 1
		k += 1
	return sortedArray




# 2nd Solution
# O(n * log(n)) time | O(n) space
def mergeSort(array):
	if len(array) == 1:
		return array
	auxillaryArray = array[:]
	mergeSortHelper(array, 0, len(array) - 1, auxillaryArray)


def mergeSortHelper(mainArray, startIndex, endIndex, auxillaryArray):
	if startIndex == endIndex:
		return 
	middleIndex = (startIndex + endIndex) // 2
	mergeSortHelper(auxillaryArray, startIndex, middleIndex, mainArray)
	mergeSortHelper(auxillaryArray, middleIndex + 1, startIndex, mainArray)
	domerge(mainArray, startIndex, middleIndex, endIndex, auxillaryArray)


def domerge(mainArray, startIndex, middleIndex, endIndex, auxillaryArray):
	k = startIndex
	i = startIndex
	j = middleIndex + 1
	while i <= middleIndex and j <= endIndex:
		if auxillaryArray[i] <= auxillaryArray[j]:
			mainArray[k] = auxillaryArray[i]
			i += 1
		else:
			mainArray[k] = auxillaryArray[j]
			j += 1
		k += 1
	while i <= middleIndex:
		mainArray[k] = auxillaryArray[i]
		i += 1
		k += 1
	while j <= endIndex:
		mainArray[k] = auxillaryArray[j]
		j += 1
		k += 1