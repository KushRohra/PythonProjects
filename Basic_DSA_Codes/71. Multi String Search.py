# 1st Soln : Brute Force
# O(bns) time | O(n) space
def multiStringSearch(bigString, smallStrings):
	return [isInBigString(bigString, smallString) for smallString in smallStrings]


def isInBigString(bigString, smallString):
	for i in range(len(bigString)):
		if i + len(smallString) > len(bigString):
			break;
		if isInBigStringHelper(bigString, smallString, i):
			return True
	return False


def isInBigStringHelper(bigString, smallString, startIndex):
	leftBigIndex = startIndex
	rightBigIndex = startIndex + len(smallString) - 1
	leftSmallIndex = 0
	rightSmallIndex = len(smallString) - 1
	while leftBigIndex <= rightBigIndex:
		if(
			bigString[leftBigIndex] != smallString[leftSmallIndex] or
			bigString[rightBigIndex] != smallString[rightSmallIndex]
			):
				return False
		leftBigIndex += 1
		rightBigIndex -= 1
		leftSmallIndex += 1
		rightSmallIndex -= 1
	return True





# 2nd solution : Modified Suffix Trie
# O(b^2 + ns) time | O(b^2 + n) space
def multiStringSearch(bigString, smallStrings):
	modifiedSuffixTrie = ModifiedSuffixTrie(bigString)
	return [modifiedSuffixTrie.contains(string) for string in smallStrings]


class ModifiedSuffixTrie:
	def __init__(self, string):
		self.root = {}
		self.populateModifiedSuffixTrieFrom(string)

	def populateModifiedSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubstringStartingAt(i, start)

	def insertSubstringStartingAt(self, i, string):
		node = self.root
		for j in range(i, len(string)):
			letter = string[i]
			if letter not in node:
				node[letter] = {}
			node = node[letter]

	def contains(self, string):
		node = self.root
		for letter in string:
			if letter not in node:
				return False
			node = node[letter]
		return True





# 3rd solution : Suffix Trie
# O(ns + bs) time | O(ns) space
def multiStringSearch(bigString, smallStrings):
	trie = Trie()
	for string in smallStrings:
		trie.insert(string)
	containedStrings = {}
	for i in range(len(bigString)):
		findSmallStringsIn(bigString, i, trie, containedStrings)
	return [string in containedStrings for string in smallStrings]


def findSmallStringsIn(string, startIndex, trie, containedStrings):
	currentNode = trie.root
	for i in range(startIndex, len(string)):
		currentChar = string[i]
		if currentChar not in currentNode:
			break
		currentNode = currentNode[currentChar]
		if trie.endSymbol in currentNode:
			containedStrings[currentNode[trie.endSymbol]] = True


class Trie:
	def __init__(self):
		self.root = {}
		self.endSymbol = "*"

	def insert(self, string):
		current = self.root
		for i in range(len(string)):
			if string[i] not in current:
				current[string[i]] = {}
			current = current[string[i]]
		current[self.endSymbol] = string