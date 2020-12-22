# O(nlog(n)) time | O(log(n)) space
def quickSort(array):
	qucickSortHelper(array, 0, len(array) - 1)
	return array


def qucickSortHelper(array, startIndex, endIndex):
	if startIndex >= endIndex:
		return
	pivotIndex = startIndex
	leftIndex = startIndex + 1
	rifgtIndex = endIndex
	while rifgtIndex >= leftIndex:
		if array[leftIndex] > array[pivotIndex] and array[rightIndex] < array[pivotIndex]:
			swap(leftIndex, rightIndex, array)
		if array[leftIndex] <= array[pivotIndex]:
			leftIndex += 1
		if array[rightIndex] >= array[pivotIndex]:
			rightIndex -= 1
	swap(pivotIndex, rightIndex, array)
	leftSubarrayIsSmaller = rightIndex - 1 -startIndex < endIndex - (rightIndex + 1)
	if leftSubarrayIsSmaller:
		qucickSortHelper(array, startIndex, rightIndex - 1)
		qucickSortHelper(array, rightIndex + 1, endIndex)
	else:
		qucickSortHelper(array, rightIndex + 1, endIndex)
		qucickSortHelper(array, startIndex, rightIndex - 1)

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]