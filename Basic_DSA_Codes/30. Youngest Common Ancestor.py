# This method is applicable only and only when the links of a tree are bidirectional

# O(d) time where d is the max depth of the 2 nodes | O(1) space
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne = getDescendandtDepth(descendantOne, topAncestor)
	depthTwo = getDescendandtDepth(descendantTwo, topAncestor)
	if depthOne > depthTwo:
		return backtrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
	else:
		return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)

def getDescendantDepth(descendant, topAncestor):
	depth = 0
	while descendant != topAncestor:
		depth += 1
		descendant = descendant.ancestor
	return depth 

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
	while diff > 0:
		lowerDescendant = lowerDescendant.ancestor
	while lowerDescendant != higherDescendant:
		lowerDescendant = lowerDescendant.ancestor
		higherDescendant = higherDescendant.ancestor
	return lowerDescendant