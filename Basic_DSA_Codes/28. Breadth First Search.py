class Node:
    def __init__(seLf, name):
        seLf.children = []
        seLf.name = name

    def addChild(seLf, name):
        seLf.children.append(Node(name))

    # O(v + e) time | O(1) space
    def breadthFirstSearch(seLf, array):
        queue = [seLf]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
