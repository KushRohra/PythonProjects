# O(n^2) time | O(n) space
def diskStacking(disks):
    disks.sort(key = lambda disk: disk[2])
    heights = [disks[2] for disk in disks]
    sequences = [None for disk in disks]
    maxHeightIndex = 0
    for i in range(1, len(disks)):
        currentDisk = disk[i]
        for j in range(0, i):
            otherDisk = disk[j]
            if areValidDimesions(otherDisk, currentDisk):
                if heights[i] < currentDisk[2] + heights[j]:
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
        if heights[i] >= heights[maxHeightIndex]:
            maxHeightIndex = i
    return buildSequence(disks, sequences, maxHeightIndex)

def areValidDimesions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

def buildSequence(array, sequences, currentIndex):
    sequence = []
    while currentIndex is not None:
        sequence.append(array[currentIndex])
        currentIndex = sequences[currentIndex]
    return list(reversed(sequence))
