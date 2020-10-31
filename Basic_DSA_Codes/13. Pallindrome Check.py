# O(n^2) time | O(n) space
def isPallindrome(string):
    reversedString = ""
    for i in range(len(string)):
        reversedString += string[i]
    return string == reversedString


# O(n) time | O(n) space
def isPallindrome(string):
    reversedChars = []
    for i in range(len(string)):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)


# O(n) time | O(n) space
def isPallindrome(string, i=0):
    j = len(string) - i - 1
    return True if i >= j else string[i] == string[j] and isPallindrome(string, i + 1)


# O(n) time | O(n) space
def isPallindrome(string, i=0):
    j = len(string) - i - 1
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPallindrome(string, i + 1)


# O(n) time | O(1) space
def isPallindrome(string):
    leftIndex = 0
    rightIndex = len(string) - 1
    while leftIndex < rightIndex:
        if string[leftIndex] != string[rightIndex]:
            return False
        leftIndex += 1
        rightIndex += 1
    return True
