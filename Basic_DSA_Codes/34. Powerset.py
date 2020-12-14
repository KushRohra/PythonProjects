# O(n*2^n) time | O(n*2^n) space
def powerset(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets


# O(n*2^n) time | O(n*2^n) space
def powerset(array, index=None):
    if index is None:
        index = len(array) - 1
    elif index < 0:
        return [[]]
    ele = array[index]
    subsets = powerset(array, index - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets
