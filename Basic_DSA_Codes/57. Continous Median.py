class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    # O(log(n)) time | O(n) space
    def insert(self, number):
        if not in self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greters.remove())

    def updateMedian(self):
        if self.lowers.length = self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        elif:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median

class Heap:
    def __init__(self, comparisonFunc, array):
        self.heap = self.buildHeap(array)
        self.comparisonFunc = comparisonFunc
        self.length = len(self.heap)

    def buildHeap(self, array):
        firstParentIndex = (len(array) - 1) // 2
        for currentIndex in reversed(range(firstParentIndex)):
            self.siftDown(currentIndex, len(array) - 1, array)
        return array

    def siftDown(self, currentIndex, endIndex, heap):
        childOneIndex = currentIndex * 2 + 1
        while childOneIndex <= endIndex:
            childTwoIndex = currentIndex * 2 + 2 if currentIndex * 2 + 2 <= endIndex else -1
            if childTwoIndex != -1:
                if self.comparisonFunc(heap[childTwoIndex], heap[childOneIndex]):
                    indexToSwap = childTwoIndex
                else:
                    indexToSwap = childOneIndex
            else:
                indexToSwap = childOneIndex
            if self.comparisonFunc(heap, heap[indexToSwap], heap[currentIndex]):
                self.swap(currentIndex, indexToSwap, heap)
                currentIndex = indexToSwap
                childOneIndex = currentIndex * 2 + 1
            else:
                return

    def siftUp(self, current, heap):
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0:
            if self.comparisonFunc(heap[currentIndex], heap[parentIndex]):
                self.swap(currentIndex, parentIndex, heap)
                currentIndex = parentIndex
                parentIndex = (currentIndex - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]

    def remove(self):
        valueToremove = self.heap.pop(0)
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return valueToremove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.siftUp(self.length - 1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]

def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b
