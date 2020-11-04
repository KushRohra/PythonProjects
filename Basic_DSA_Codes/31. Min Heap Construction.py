class MinHeap:
	def __init__(self, array):
		self.heap = self.buildHeap(array)

	def buildHeap(self, array):
		firstParentIndex = (len(array) - 2) // 2
		for currentIndex in reversed(range(firstParentIndex)):
			self.shiftDown(currentIndex, len(array) - 1, array)
		return array

	def shiftDown(self, currentIndex, endIndex, heap):
		childOneIndex = currentIndex * 2 + 1
		while childOneIndex <= endIndex:
			childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
			if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
				indexToSwap = childTwoIndex
			else:
				indexToSwap = childOneIndex
			if heap[indexToSwap] < heap[currentIndex]:
				self.swap(currentIndex, indexToSwap, heap)
				currentIndex = indexToSwap
				childOneIndex = currentIndex * 2 + 1
			else:
				break

	def shiftUp(self, currentIndex, heap):
		parentIndex = (currentIndex - 1) // 2
		while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]:
			self.swap(currentIndex, parentIndex, heap)
			currentIndex = parentIndex
			parentIndex = (currentIndex - 1) // 2

	def peek(self):
		return self.heap[0]

	def remove(self):
		swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.shiftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove

	def insert(self, value):
		self.heap.append(value)
		self.shiftUp(len(self.heap) - 1, self.heap)

	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]