# O(b^2 * r) time  | O(b) space
def apartmentHunting(blocks, reqs):
	maxDistanceAtBlocks = [float("-inf") for block in blocks]
	for i in range(len(blocks)):
		for req in reqs:
			closestReqDistance = float("inf")
			for j in range(len(blocks)):
				if blocks[j][req]:
					closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
			maxDistanceAtBlocks[i] = max(maxDistanceAtBlocks[i], closestReqDistance)
	return getIndexAtMinValue(maxDistanceAtBlocks)


def getIndexAtMinValue(array):
	indexAtMinValue = 0
	minValue = float("inf")
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			indexAtMinValue = i
	return indexAtMinValue


def distanceBetween(a, b):
	return abs(a - b)





# O(b * r) time | O(b * r) space
def apartmentHunting(blocks, reqs):
	minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
	maxDistanceAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
	return getIndexAtMinValue


def getMinDistances(blocks, req):
	minDistances = [0 for block in blocks]
	closestReqIndex = float("inf")
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestReqIndex = i
		minDistances[i] = distanceBetween(i, closestReqIndex)
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqIndex = i
		minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIndex))


def maxDistancesAtBlocks(blocks, minDistancesFromBlocks):
	maxDistancesAtBlocks = [0 for block in blocks]
	for i in range(len(blocks)):
		minDistancesAtBlocks = list(map(lambda distances: distances[i], minDistancesFromBlocks))
	maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], minDistancesAtBlocks)
return maxDistancesAtBlocks


def getIndexAtMinValue(array):
	indexAtMinValue = 0
	minValue = float("inf")
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			indexAtMinValue = i
	return indexAtMinValue


def distanceBetween(a, b):
	return abs(a - b)