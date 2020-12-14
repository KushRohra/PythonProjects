# O(n^2) time | O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(range)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1
    return sum(rewards)


# O(n) time | O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    localMinIndexes = getLocalMinIndexes(scores)
    for localMinIndex in localMinIndexes:
        expandFromLocalMinIndex(localMinIndex, scores, rewards)
    return sum(rewards)


def getLocalMinIndexes(array):
    if len(array) == 1:
        return [0]
    localMinIndex = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            localMinIndex.append(i)
            continue
        if i == len(array - 1) and array[i] < array[i - 1]:
            localMinIndex.append(i)
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:
            localMinIndex.append(i)
    return localMinIndex


def expandFromLocalMinIndex(localMinIndex, scores, rewards):
    leftIndex = localMinIndex - 1
    while leftIndex >= 0 and scores[leftIndex] > scores[leftIndex + 1]:
        rewards[leftIndex] = max(rewards[leftIndex], rewards[leftIndex + 1] + 1)
        leftIndex -= 1
    rightIndex = localMinIndex + 1
    while rightIndex < len(scores) and scores[rightIndex] > scores[rightIndex - 1]:
        rewards[rightIndex] = rewards[rightIndex - 1] + 1
        rightIndex += 1


# O(n) time | O(n) space
def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1
    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)
    return sum(rewards)
