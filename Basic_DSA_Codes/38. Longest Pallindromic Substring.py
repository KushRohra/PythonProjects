# O(n^2) time | O(1) space
def longestPallindromicSubstring(string):
	currentLongest = [0, 1]
	for i in range(1, len(string)):
		odd = getlongestPallindromeFrom(string, i - 1, i + 1)
		even = getlongestPallindromeFrom(sting, i - 1, i)
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
	return string[currentLongest[0]:currentLongest[1]]

def getLongestPallindromeFrom(string, leftIndex, rightIndex):
	while leftIndex >= 0 and rightIndex < len(string):
		if string[leftIndex] != string[rightIndex]:
			break
		leftIndex += 1
		rightIndex -= 1
	return [leftIndex + 1, rightIndex]