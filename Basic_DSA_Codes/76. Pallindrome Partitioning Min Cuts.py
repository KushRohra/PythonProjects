# 1st solution
# O(n^3) time | O(n^2) space
def pallindromePartitioningMinCuts(string):
	pallindromes = [[False for i in string] for j in string]
	for i in range(len(string)):
		for j in range(len(string)):
			pallindromes[i][j] = isPallindrome(string[i:j + 1])
	cuts = [float("inf") for i in string]
	for i in range(len(string)):
		if pallindromes[0][i]:
			cuts[i] = 0
		else:
			cuts[i] = cuts[i- 1] + 1
			for j in range(1, i):
				if pallindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
					cuts[i] = cuts[j - 1] + 1
	return cuts[-1]


def isPallindrome(string):
	leftIndex = 0
	rightIndex = len(string - 1)
	while leftIndex < rightIndex:
		if string[leftIndex] != string[rightIndex]:
			return False
		leftIndex += 1
		rightIndex -= 1
	return True




# 2nd solution
# O(n^2) time | O(n^2) space
def pallindromePartitioningMinCuts(string):
	pallindromes = [[False for i in string] for j in string]
	for i in range(len(string)):
		pallindromes[i][i] = True
	for length in range(2, len(string) + 1):
		for i in range(0, len(string) - length + 1):
			j = i + length - 1
			if length == 2:
				pallindromes[i][j] = string[i] == string[j]
			else:
				pallindromes[i][j] = string[i] == string[j] and pallindromes[i + 1][j - 1]
	cuts = [float("inf") for i in string]
	for i in range(len(string)):
		if pallindromes[0][i]:
			cuts[i] = 0
		else:
			cuts[i] = cuts[i- 1] + 1
			for j in range(1, i):
				if pallindromes[j][i] and cuts[j - 1] + 1 < cuts[i]:
					cuts[i] = cuts[j - 1] + 1
	return cuts[-1]
