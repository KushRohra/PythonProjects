# O(n) time | O(d) space where d is the height of the tree 
def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))


def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    return validateBSTHelper(tree.left, minValue, tree.value) and validateBSTHelper(tree.right, tree.value, maxValue)
